from __future__ import annotations

import re

from .types import (
    CompiledRulesT,
    CompiledRuleT,
    FacadePathT,
    FacadePathTemplateT,
    LocationT,
    MarshmallowValidationErrorT,
    RawRulesMapT,
)

#
# Public API
#


def compile_rules(rules: RawRulesMapT) -> CompiledRulesT:
    """
    Compile mappings of {destination_path -> facade_path} into case-insensitive
    regex matchers and facade templates with capture placeholders like '{i0-1}'.

    - Destination path is typically XPath-like with one-based indices and optional prefixes
    - Each step tolerates an optional namespace prefix and case-insensitive names
    - Any arbitrary leading prefixes are skipped (e.g., '/hd:GovTalkMessage[1]/.../IRenvelope[1]/')
    - Every captured index is available as a named group 'iK'; facade templates use '{iK-1}'
    """
    compiled: list[CompiledRuleT] = []
    for dest, facade in rules.items():
        pattern_str, _, name_to_caps = _dest_segments_with_captures(dest)
        template = _build_facade_template(facade, name_to_caps)
        pat = re.compile(pattern_str, re.IGNORECASE | re.UNICODE)
        compiled.append((pat, template))
    return compiled


def translate_location(
    location: LocationT, compiled_rules: CompiledRulesT
) -> FacadePathT | None:
    """
    Return a first matching facade path (e.g., 'mtr/sa103s[6]/foo/bar') if any rule matches the given location.
    If no matches found return None.
    """
    for pat, template in compiled_rules:
        match = pat.match(location)
        if match:
            return _render_template(template, match)
    return None


def insert_error(
    root: MarshmallowValidationErrorT, facade_path: FacadePathT | None, message: str
) -> None:
    """
    Insert `message` into a nested dict at `facade_path`.

    Example result shape:
      {'mtr': {'sa103s': {6: {'net_profit_or_loss': ['...']}}}}
    """
    if not facade_path:
        return

    parts = _split_path(facade_path)
    node: MarshmallowValidationErrorT = root  # current nesting

    for idx, part in enumerate(parts):
        match = _FACADE_STEP_REGEX.match(part)
        if not match:
            # Fallback: treat the entire token as a plain key
            key = part
            is_last = idx == len(parts) - 1
            if is_last:
                leaf = node.setdefault(key, [])
                if isinstance(leaf, list):
                    leaf.append(message)
                else:
                    node[key] = [message]
            else:
                node = node.setdefault(key, {})  # type: ignore[assignment]
            continue

        name = match.group("name")
        idx_str = match.group("idx")
        is_last = idx == len(parts) - 1

        if idx_str is None:
            # plain object step
            if is_last:
                leaf = node.setdefault(name, [])
                if isinstance(leaf, list):
                    leaf.append(message)
                else:
                    node[name] = [message]
            else:
                next_node = node.get(name)
                if not isinstance(next_node, dict):
                    next_node = {}
                    node[name] = next_node
                node = next_node
        else:
            # indexed collection step
            idx = int(idx_str)
            bucket = node.get(name)
            if not isinstance(bucket, dict):
                bucket = {}
                node[name] = bucket
            next_node = bucket.get(idx)
            if is_last:
                if isinstance(next_node, list):
                    next_node.append(message)
                else:
                    bucket[idx] = [message]
            else:
                if not isinstance(next_node, dict):
                    next_node = {}
                    bucket[idx] = next_node
                node = next_node


#
# Const
#

# Placeholder like {i0-1} or {i3} (we support both; -1 means convert 1-based -> 0-based)
_PLACEHOLDER_REGEX = re.compile(r"\{i(?P<n>\d+)(?P<delta>-1)?\}")

# Token parser for facade paths like 'mtr/sa103s[6]/foo/bar'
_FACADE_STEP_REGEX = re.compile(r"^(?P<name>[^/\[\]]+)(?:\[(?P<idx>\d+)\])?$")

# Matches one step of an XPath-like path, with an optional namespace prefix and optional [index]
# Examples it should match:
#   MTR:Sa103S[7]
#   Sa103S[1]
#   hd:Body[1]
#   NetBusinessLossForTax[2]
#   SelfEmployment[*]  (wildcard)
#   Key[@Type='UTR']   (predicate)
_STEP_REGEX = re.compile(
    r"""
    ^                                    # start of segment
    (?:(?P<prefix>[A-Za-z][\w.-]*)\:)?   # optional ns prefix (e.g. 'MTR:')
    (?P<name>[A-Za-z_][\w.-]*)           # local name
    (?:\[(?P<idx>\d+|\*|@[^\]]+)\])?     # optional [index], [*] wildcard, or [@predicate]
    $                                    # end of segment
    """,
    re.VERBOSE,
)

# Allow arbitrary leading prefixes like /hd:GovTalkMessage[1]/.../
# before the destination root. Anchor at start, optionally skip any prefix.
_PREFIX_SKIP = r"^.*?"

# Optional namespace prefix on each step
_NS_OPT = r"(?:[A-Za-z][\w.-]*:)?"

#
# Helpers: path parsing, normalization, etc.
#


def _render_template(
    template: FacadePathTemplateT, match: re.Match[str]
) -> FacadePathT:
    def sub_one(mm: re.Match[str]) -> str:
        n = int(mm.group("n"))
        group_name = f"i{n}"
        raw = match.group(group_name)
        if raw is None:
            # If a referenced capture was not present, keep as-is
            return mm.group(0)
        val = int(raw)
        if mm.group("delta"):
            val -= 1
        return str(val)

    return _PLACEHOLDER_REGEX.sub(sub_one, template)


def _split_path(path: str) -> list[str]:
    """
    Split a path like 'MTR:MTR[1]/MTR:Sa103S[7]/MTR:Foo[1]' into segments
    """
    p = path.strip("/")
    return [s for s in p.split("/") if s]


def _normalize_name(s: str) -> str:
    """
    Normalize a step name for comparison (case-insensitive)
    """
    return re.sub(r"[^A-Za-z0-9]+", "", s).lower()


def _dest_segments_with_captures(
    dest: str,
) -> tuple[str, list[tuple[str, str | None]], dict[str, list[int]]]:
    """
    Build a tolerant regex for the destination path and produce a mapping from
    normalized local-names to the capture indices we assign.

    Returns:
      pattern_str, segments, name_to_capture_indices

    Where:
      segments = list of (local_name, idx_str_or_None)
      name_to_capture_indices maps normalized local-name -> [capture_ordinals]
    """
    segments = _split_path(dest)
    regex_parts: list[str] = []
    name_to_caps: dict[str, list[int]] = {}
    cap_counter = 0

    for raw_segment in segments:
        match = _STEP_REGEX.match(raw_segment)
        if not match:
            # Be conservative: treat as literal name without index
            name, idx_val = raw_segment, None
        else:
            name = match.group("name")
            idx_val = match.group("idx")  # could be digit, '*', or '@...'

        norm = _normalize_name(name)
        if idx_val == "*":
            # Wildcard: capture any numeric index
            cap_name = f"i{cap_counter}"
            cap_counter += 1
            name_to_caps.setdefault(norm, []).append(int(cap_name[1:]))
            regex_parts.append(rf"/{_NS_OPT}{re.escape(name)}\[(?P<{cap_name}>\d+)\]")
        elif idx_val is not None and idx_val.isdigit():
            # Explicit numeric index must match exactly as written.
            regex_parts.append(rf"/{_NS_OPT}{re.escape(name)}\[{re.escape(idx_val)}\]")
        elif idx_val is not None and idx_val.startswith("@"):
            # XPath predicate like [@Type='UTR']: match it literally (escaped)
            regex_parts.append(rf"/{_NS_OPT}{re.escape(name)}\[{re.escape(idx_val)}\]")
        else:
            # No index or unrecognized: tolerate presence/absence of [n]
            regex_parts.append(rf"/{_NS_OPT}{re.escape(name)}(?:\[\d+\])?")

    # Anchor, permit any leading prefix, and force end-of-string
    pattern = _PREFIX_SKIP + "".join(regex_parts) + r"$"
    # Also return segments parsed into (local_name, idx_str_or_None)
    parsed_segments: list[tuple[str, str | None]] = []
    for raw_segment in segments:
        match = _STEP_REGEX.match(raw_segment)
        if match:
            parsed_segments.append((match.group("name"), match.group("idx")))
        else:
            parsed_segments.append((raw_segment, None))
    return pattern, parsed_segments, name_to_caps


#
# Facade template construction
#

_FACADE_INDEX_REGEX = re.compile(r"(?P<name>[^/\[\]]+)\[(?P<idx>\d+)\]")


def _build_facade_template(
    facade: FacadePathT,
    name_to_caps: dict[str, list[int]],
) -> FacadePathTemplateT:
    """
    Replace numeric indices in the facade path with placeholders that reference
    the right destination capture groups by normalized element name.

    Example:
      facade: 'mtr/sa103s[0]/profits_losses_nics_and_cis/net_business_loss_for_tax'
      name_to_caps: {'mtr': [0], 'sa103s': [1], 'profitslossesnicsandcis': [2], ...}

      -> 'mtr/sa103s[{i1-1}]/profits_losses_nics_and_cis/net_business_loss_for_tax'
    """
    used_per_name: dict[str, int] = {}

    def repl(m: re.Match[str]) -> str:
        local = m.group("name")
        norm = _normalize_name(local)
        indices = name_to_caps.get(norm)
        if indices:
            # Use the next available capture index for this element name
            used = used_per_name.get(norm, 0)
            # Guard in case of more facade indices than captures of same name
            idx_ord = indices[used] if used < len(indices) else indices[-1]
            used_per_name[norm] = min(used + 1, len(indices))
            return f"{local}" + f"[{{i{idx_ord}-1}}]"
        # If we cannot bind by name, leave the original numeric index as-is
        return m.group(0)

    return _FACADE_INDEX_REGEX.sub(repl, facade)
