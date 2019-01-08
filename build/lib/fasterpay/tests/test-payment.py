#!/usr/bin/python

from fasterpay.gateway import FP_Gateway

if __name__ == "__main__":

    fpGateway = FP_Gateway("84f22520d6208411f830ef975d5c8f9e", "5045152577cf9ee9794919b32e4205c5")

    payload = {
        "description": "Golden Ticket",
        "amount": "0.01",
        "currency": "EUR",
        "merchant_order_id": "w_09809127072",
        "success_url": "http://localhost:12345/success.php"
    }

    paymentForm = fpGateway.initiate_transaction(payload)

    print paymentForm
