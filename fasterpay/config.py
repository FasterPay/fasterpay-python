#!/usr/bin/python


class Config:

    def __init__(self, private_key, public_key, is_test=False, api_version=None):
        self.public_key = public_key
        self.private_key = private_key
        if is_test is True:
            self.API_BASE_URL = "https://pay.fasterpay.com"
        else:
            self.API_BASE_URL = "https://pay.sandbox.fasterpay.com"

        if api_version is not None:
            self.VERSION = api_version
        else:
            self.VERSION = "1.0.0"

    def get_public_key(self):
        return self.public_key

    def get_private_key(self):
        return self.private_key

    def get_api_url(self):
        return self.API_BASE_URL

    def get_api_version(self):
        return self.VERSION
