#!/usr/bin/python

from fasterpay.gateway import Gateway
import random

if __name__ == "__main__":
    gateway = Gateway("<your private key>", "<your public key>", True)

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
