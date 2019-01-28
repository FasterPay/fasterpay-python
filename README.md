# Welcome to FasterPay Python SDK.

FasterPay Python SDK enables you to integrate the FasterPay's Checkout Page seamlessly without having the hassle of integrating everything from Scratch.
Once your customer is ready to pay, FasterPay will take care of the payment, notify your system about the payment and return the customer back to your Thank You page.

## Initiating Payment Request using Python SDK.

```python
from fasterpay.gateway import Gateway

if __name__ == "__main__":

  gateway = Gateway("<your private key>", "<your public key>")

  payload = {
      "description": "Golden Ticket",
      "amount": "0.01",
      "currency": "EUR",
      "merchant_order_id": "xxxxx",
      "success_url": "https://yourcompanywebsite.com/success"
  }

paymentForm = gateway.payment_form().build_form(payload)

print paymentForm
```

For more information on the API Parameters, refer to our entire API Documentation [here](https://docs.fasterpay.com/api#section-custom-integration)

## Handling FasterPay Pingbacks

```python
from flask import request
from fasterpay.gateway import FP_Gateway
gateway = Gateway("<your private key>", "<your public key>")
if gateway.pingback().validate({"apiKey": request.headers.get("X-ApiKey")}) is True:
  print "OK"
else:
  print "NOK"
```

### Questions?
* Common questions are covered in the [FAQ](https://www.fasterpay.com/support).
* For integration and API questions, feel free to reach out Integration Team via [integration@fasterpay.com](mailto:integration@fasterpay.com)
* For business support, email us at [merchantsupport@fasterpay.com](mailto:merchantsupport@fasterpay.com)
* To contact sales, email [sales@fasterpay.com](mailto:sales@fasterpay.com).
