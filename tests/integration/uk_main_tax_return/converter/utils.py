import base64
import datetime
from decimal import Decimal

from xsdata.models.datatype import XmlDate


def xml_date_or_none(value: datetime.date | None) -> XmlDate | None:
    return None if value is None else XmlDate.from_date(value)


def xml_period_or_none(value: int) -> str | None:
    return None if value is None else str(value)


def decimal_str_or_none(value: Decimal | None) -> str | None:
    # NB! f-string specifier applied banking rounding to 2 decimal places
    # Make sure you apply desired rounding before calling this function
    return None if value is None else f"{value:.2f}"


def decode_attachment(content: str) -> bytes:
    return base64.b64decode(content)
