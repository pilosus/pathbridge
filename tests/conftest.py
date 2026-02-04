import pytest

from pathbridge.types import RawRulesMapT


@pytest.fixture()
def xpath_rules() -> RawRulesMapT:
    """
    Destination locations are XPath-like (not regex).
    Facade locations are your user-facing “facade schema” paths.
    """
    return {
        # SA100 personal details
        "/GovTalkMessage/Body/IRenvelope/IRbody/SA100/YourName/FirstName": "/taxpayer/name/first",
        "/GovTalkMessage/Body/IRenvelope/IRbody/SA100/YourName/Surname": "/taxpayer/name/last",
        # Header keys: make one rule more specific than the other to test precedence
        "/GovTalkMessage/Body/IRenvelope/IRheader/Keys/Key[@Type='UTR']": "/taxpayer/utr",
        "/GovTalkMessage/Body/IRenvelope/IRheader/Keys/Key": "/taxpayer/key",
        # Repeating nodes (index wildcard)
        "/GovTalkMessage/Body/IRenvelope/IRbody/SA103S/SelfEmployment[*]/BusinessName": "/self_employment/[i]/business_name",
        "/GovTalkMessage/Body/IRenvelope/IRbody/SA103S/SelfEmployment[*]/Turnover": "/self_employment/[i]/turnover",
        "/GovTalkMessage/Body/IRenvelope/IRbody/SA103S/SelfEmployment[*]/Expenses/Total": "/self_employment/[i]/expenses/total",
        # Another repeating structure
        "/GovTalkMessage/Body/IRenvelope/IRbody/SA100/Income/Interest[*]/Amount": "/income/interest/[i]/amount",
    }
