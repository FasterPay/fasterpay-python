#!/usr/bin/python

from fasterpay.gateway import Gateway

if __name__ == "__main__":

    gateway = Gateway("<your private key>", "<your public key>", True)

    payload = {
        "description": "Golden Ticket",
        "amount": "10",
        "currency": "EUR",
        "merchant_order_id": "w_09809127072",
        "success_url": "http://localhost:12345/success.php",
        "recurring_name": "Test FP Recurring",
        "recurring_sku_id": "fp_test_recurring",
        "recurring_period": "10d",
        "recurring_trial_amount": "1",
        "recurring_trial_period": "3d",
        "recurring_duration": 0
    }

    paymentForm = gateway.payment_form().build_form(payload)

    print paymentForm
