# Welcome to FasterPay Python SDK

FasterPay Python SDK enables you to integrate the FasterPay's Checkout Page seamlessly without having the hassle of integrating everything from Scratch.
Once your customer is ready to pay, FasterPay will take care of the payment, notify your system about the payment and return the customer back to your Thank You page.

## Downloading the FasterPay Python SDK

```sh
$ git clone https://github.com/FasterPay/fasterpay-python.git
```

## Installing the FasterPay Python SDK.
```sh
$ cd fasterpay-Python
$ sudo python setup.py install
```

## Initiating Payment Request using Python SDK

```python
from fasterpay.gateway import Gateway

if __name__ == "__main__":

  gateway = Gateway("<your private key>", "<your public key>", True)

  parameters = {
        "payload": {
            "description": "Golden Ticket",
            "amount": "0.01",
            "currency": "EUR",
            "merchant_order_id": str(random.randint(1000, 9999)),
            "success_url": "https://4f9f73c1.ngrok.io/success",
            "sign_version": "v2",
            "pingback_url": "https://4f9f73c1.ngrok.io/pingback",
        }
    }

  paymentForm = gateway.payment_form().build_form(parameters)
  print paymentForm
```

For more information on the API Parameters, refer to our entire API Documentation [here](https://docs.fasterpay.com/api#section-custom-integration)

## Handling FasterPay Pingbacks

```python
from flask import request
from fasterpay.gateway import FP_Gateway
gateway = Gateway("<your private key>", "<your public key>", True)
pingback_data = request.get_data()
if request.headers.get("X-Fasterpay-Signature-Version") == "v2":
    headers = {
        "X-Fasterpay-Signature": str(request.headers.get("X-Fasterpay-Signature")),
        "X-Fasterpay-Signature-Version": str(request.headers.get("X-Fasterpay-Signature-Version"))
    }
else:
    headers = {
        "X-ApiKey": str(request.headers.get("X-ApiKey"))
    }

if gateway.pingback().validate(pingback_data, headers) is True:
    return "OK"
else:
    return "NOK"
```

## FasterPay Test Mode
FasterPay has a Sandbox environment called Test Mode. Test Mode is a virtual testing environment which is an exact replica of the live FasterPay environment. This allows businesses to integrate and test the payment flow without being in the live environment. Businesses can create a FasterPay account, turn on the **Test Mode** and begin to integrate the widget using the test integration keys.

### Initiating FasterPay Gateway in Test-Mode
```python
from fasterpay.gateway import Gateway
gateway = Gateway("<your private key>", "<your public key>", True)
```

### Questions?
* Common questions are covered in the [FAQ](https://www.fasterpay.com/support).
* For integration and API questions, feel free to reach out Integration Team via [integration@fasterpay.com](mailto:integration@fasterpay.com)
* For business support, email us at [merchantsupport@fasterpay.com](mailto:merchantsupport@fasterpay.com)
* To contact sales, email [sales@fasterpay.com](mailto:sales@fasterpay.com).
