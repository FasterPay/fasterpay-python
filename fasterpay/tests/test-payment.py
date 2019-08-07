#!/usr/bin/python

from fasterpay.gateway import Gateway
import random

if __name__ == "__main__":
    gateway = Gateway("4a6608170097835d0fbb856662e99da3", "e416c4de8ffd2b198d83713b8d232fab", True)

    parameters = {
        "payload": {
            "description": "Test product description",
            "amount": "0.01",
            "currency": "EUR",
            "merchant_order_id": str(random.randint(1000, 9999)),
            "success_url": "http://localhost:12345/success.php",
            "sign_version": "v2"
        }
    }
    paymentForm = gateway.payment_form().build_form(parameters)

    print paymentForm
