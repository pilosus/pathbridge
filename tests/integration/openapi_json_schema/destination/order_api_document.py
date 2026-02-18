from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CustomerObject:
    email: str = field(metadata={"name": "email"})


@dataclass
class RequestItemObject:
    sku: str = field(metadata={"name": "sku"})
    qty: int = field(metadata={"name": "qty"})


@dataclass
class RequestBodyObject:
    order_id: str = field(metadata={"name": "orderId"})
    customer: CustomerObject = field(metadata={"name": "customer"})
    items: list[RequestItemObject] = field(
        default_factory=list, metadata={"name": "items"}
    )


@dataclass
class RequestObject:
    body: RequestBodyObject = field(metadata={"name": "body"})


@dataclass
class ResponseLineObject:
    total_amount: str = field(metadata={"name": "totalAmount"})


@dataclass
class ResponseDataObject:
    order_id: str = field(metadata={"name": "orderId"})
    lines: list[ResponseLineObject] = field(
        default_factory=list, metadata={"name": "lines"}
    )


@dataclass
class ResponseBodyObject:
    status: str = field(metadata={"name": "status"})
    data: ResponseDataObject = field(metadata={"name": "data"})


@dataclass
class ResponseObject:
    body: ResponseBodyObject = field(metadata={"name": "body"})


@dataclass
class ValidationDocument:
    request: RequestObject = field(metadata={"name": "request"})
    response: ResponseObject = field(metadata={"name": "response"})

    class Meta:
        name = "validation"
