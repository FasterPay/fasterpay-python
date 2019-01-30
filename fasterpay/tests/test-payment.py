#!/usr/bin/python

from fasterpay.gateway import Gateway

if __name__ == "__main__":

    gateway = Gateway("<your private key>", "<your public key>")

    payload = {
        "description": "Golden Ticket",
        "amount": "0.01",
        "currency": "EUR",
        "merchant_order_id": "w_09809127072",
        "success_url": "http://localhost:12345/success.php"
    }

    paymentForm = gateway.payment_form().build_form(payload)

    print paymentForm
