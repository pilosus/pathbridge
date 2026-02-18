from __future__ import annotations

import tests.integration.openapi_json_schema.destination.order_api_document as destination
import tests.integration.openapi_json_schema.facade.order_api_facade as facade


def _normalize_email(value: str) -> str:
    return value.strip().lower()


def to_order_api_validation_document(
    data: facade.ApiValidationFacade,
) -> destination.ValidationDocument:
    request_body = data.request.body
    response_body = data.response.body
    response_data = response_body.data

    return destination.ValidationDocument(
        request=destination.RequestObject(
            body=destination.RequestBodyObject(
                order_id=request_body.order_id,
                customer=destination.CustomerObject(
                    email=_normalize_email(request_body.customer.email)
                ),
                items=[
                    destination.RequestItemObject(
                        sku=item.sku,
                        qty=item.quantity,
                    )
                    for item in request_body.items
                ],
            ),
        ),
        response=destination.ResponseObject(
            body=destination.ResponseBodyObject(
                status=response_body.status,
                data=destination.ResponseDataObject(
                    order_id=response_data.order_id,
                    lines=[
                        destination.ResponseLineObject(total_amount=line.total_amount)
                        for line in response_data.lines
                    ],
                ),
            )
        ),
    )
