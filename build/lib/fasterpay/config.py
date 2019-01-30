#!/usr/bin/python

class FP_Config:

    def __init__(self, privateKey, publicKey, apiUrl = None, apiVersion = None):
        self.publicKey = publicKey
        self.privateKey = privateKey
        if apiUrl is not None :
            self.apiUrl = apiUrl
        else:
            self.apiUrl = "http://develop.pay2.fasterpay.bamboo.stuffio.com/payment/form"

        if apiVersion is not None :
            self.apiVersion = apiVersion
        else:
            self.apiVersion = "1.0.0"

    def get_public_key(self):
        return self.publicKey

    def get_private_key(self):
        return self.privateKey

    def get_api_url(self):
        return self.apiUrl

    def get_api_version(self):
        return self.apiVersion
