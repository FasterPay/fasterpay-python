#!/usr/bin/python

from fasterpay.gateway import Gateway
import random

if __name__ == "__main__":

    gateway = Gateway("t_ff9cb7bb402405b742341330a817b1", "t_f2883f81526dfd32d2ded7778d1999")

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
