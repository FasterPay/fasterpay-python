#!/usr/bin/python

class Config:

    def __init__(self, privateKey, publicKey, is_test = False, apiVersion = None):
        self.publicKey = publicKey
        self.privateKey = privateKey
        if is_test is True :
            self.API_BASE_URL = "http://pay.fasterpay.com"
        else:
            self.API_BASE_URL = "http://pay.sandbox.fasterpay.com"

        if apiVersion is not None :
            self.VERSION = apiVersion
        else:
            self.VERSION = "1.0.0"

    def get_public_key(self):
        return self.publicKey

    def get_private_key(self):
        return self.privateKey

    def get_api_url(self):
        return self.API_BASE_URL

    def get_api_version(self):
        return self.VERSION
