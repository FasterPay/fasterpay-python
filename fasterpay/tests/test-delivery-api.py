#!/usr/bin/bash

from fasterpay.gateway import Gateway

if __name__ == "__main__":

    # Initialize the Gateway
    gateway = Gateway("<YOUR PRIVATE KEY>", "<YOUR PUBLIC KEY>", True)

    # Prepare Delivery Information
    deliveryInfo = {
        "payment_order_id": "98271",
        "merchant_order_id": "1572519862",
        "type": "digital",
        "public_key": gateway.get_config().get_public_key(),
        "status": "order_placed",
        "refundable": 1,
        "details": "Order placed today",
        "shipping_address[email]": "prashant@paymentwall.com"
    }

    deliverResponse = gateway.transaction().deliver(deliveryInfo)

    print deliverResponse