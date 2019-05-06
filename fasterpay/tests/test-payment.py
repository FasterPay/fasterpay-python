#!/usr/bin/python

from fasterpay.gateway import Gateway
import random

if __name__ == "__main__":
    gateway = Gateway("<your private key>", "<your public key>")

    parameters = {
        "payload": {
            "description": "Golden Ticket",
            "amount": "0.01",
            "currency": "EUR",
            "merchant_order_id": random.randint(1000, 9999),
            "success_url": "http://localhost:12345/success.php",
        },
        "auto_submit_form": True
    }

    paymentForm = gateway.payment_form().build_form(parameters)

    print paymentForm
