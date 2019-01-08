#!/usr/bin/python

from fasterpay.gateway import FP_Gateway

if __name__ == "__main__":

    fpGateway = FP_Gateway("<your private key>", "<your public key")

    payload = {
        "description": "Golden Ticket",
        "amount": "0.01",
        "currency": "EUR",
        "merchant_order_id": "w_09809127072",
        "success_url": "http://localhost:12345/success.php"
    }

    paymentForm = fpGateway.initiate_transaction(payload)

    print paymentForm
