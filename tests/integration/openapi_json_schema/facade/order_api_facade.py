from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True, slots=True)
class RequestItemFacade:
    sku: str
    quantity: int


@dataclass(frozen=True, kw_only=True, slots=True)
class RequestCustomerFacade:
    email: str


@dataclass(frozen=True, kw_only=True, slots=True)
class RequestBodyFacade:
    order_id: str
    customer: RequestCustomerFacade
    items: list[RequestItemFacade]


@dataclass(frozen=True, kw_only=True, slots=True)
class ResponseLineFacade:
    total_amount: str


@dataclass(frozen=True, kw_only=True, slots=True)
class ResponseDataFacade:
    order_id: str
    lines: list[ResponseLineFacade]


@dataclass(frozen=True, kw_only=True, slots=True)
class ResponseBodyFacade:
    status: str
    data: ResponseDataFacade


@dataclass(frozen=True, kw_only=True, slots=True)
class RequestPayloadFacade:
    body: RequestBodyFacade


@dataclass(frozen=True, kw_only=True, slots=True)
class ResponsePayloadFacade:
    body: ResponseBodyFacade


@dataclass(frozen=True, kw_only=True, slots=True)
class ApiValidationFacade:
    request: RequestPayloadFacade
    response: ResponsePayloadFacade
