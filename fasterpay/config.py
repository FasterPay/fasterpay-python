#!/usr/bin/python

class Config:

    def __init__(self, privateKey, publicKey, apiUrl = None, apiVersion = None):
        self.publicKey = publicKey
        self.privateKey = privateKey
        if apiUrl is not None :
            self.API_BASE_URL = apiUrl
        else:
            self.API_BASE_URL = "http://develop.pay2.fasterpay.bamboo.stuffio.com"

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
