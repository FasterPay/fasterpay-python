#!/usr/bin/python
from config import Config
from validator.signature import Signature
from validator.pingback import Pingback
from request.paymentform import PaymentForm


class Gateway:

    def __init__(self, private_key, public_key, api_url=None, api_version=None):
        self.config = Config(private_key, public_key, api_url, api_version)

    def payment_form(self):
        return PaymentForm(self)

    def signature(self):
        return Signature(self)

    def pingback(self):
        return Pingback(self)

    def get_config(self):
        return self.config



