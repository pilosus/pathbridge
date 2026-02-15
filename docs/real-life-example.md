# Real-life Example

Full working example code: [HMRC Main Tax Return integration](https://github.com/pilosus/pathbridge/tree/main/tests/integration/uk_main_tax_return).

## What this example is about

This integration models HMRC Self Assessment XML using the Main Tax Return schema
(MTR v1.1). The schema file lives in the example and is treated as source of truth.

## Step 1. Generate destination dataclasses from XSD

We use `xsdata` to generate Python dataclasses from the HMRC schema:

```bash
uv run xsdata generate schema/MTR-v1-1.xsd --package destination
```

These generated classes mirror XML 1:1, which is ideal for serialization but less
ideal as an internal application API.

## Step 2. Keep a facade model for your internal API

In a real application, we usually do not expose generated destination dataclasses
directly. Instead we use facade dataclasses to:

- keep internal API stable even if external schema changes
- control naming and field shapes for application code
- use app-friendly types and structures

Then we map facade -> destination in a converter.

## Step 3. See what HMRC validation errors look like

A real error example from the tests:

```text
location:
/hd:GovTalkMessage[1]/hd:Body[1]/MTR:IRenvelope[1]/MTR:MTR[1]/MTR:SA103S[1]/MTR:BusinessDetails[1]/MTR:BusinessDescription[1]

message:
Invalid content found at element 'BusinessDescription'
```

This path is in HMRC XML terms, not in your facade model terms.

## Step 4. Use PathBridge to translate into facade-shaped errors

```python
from pathbridge import compile_rules, to_marshmallow, translate_location
from pathbridge.extras import build_rules, make_shape
from tests.integration.uk_main_tax_return.converter.mtr_converter import to_mtr_v1_1
from tests.integration.uk_main_tax_return.destination import mtr_v1_1 as destination
from tests.integration.uk_main_tax_return.facade import mtr_facade as facade

shape = make_shape(facade.MTR, list_len=10)
rules = build_rules(
    destination_module=destination,
    facade_to_destination=to_mtr_v1_1,
    facade_shape=shape,
    facade_root_tag="mtr",
    destination_prefix="MTR",
)
compiled = compile_rules(rules)

location = "/hd:GovTalkMessage[1]/hd:Body[1]/MTR:IRenvelope[1]/MTR:MTR[1]/MTR:SA103S[1]/MTR:BusinessDetails[1]/MTR:BusinessDescription[1]"
message = "Invalid content found at element 'BusinessDescription'"

facade_path = translate_location(location, compiled)
# "mtr/sa103s[0]/business_details/business_description"

errors = to_marshmallow([(location, message)], compiled)
# {
#   "mtr": {
#     "sa103s": {
#       0: {
#         "business_details": {
#           "business_description": ["Invalid content found at element 'BusinessDescription'"]
#         }
#       }
#     }
#   }
# }
```

This is the key payoff: external XPath errors are transformed into internal,
facade-aligned validation errors your application can return directly.
