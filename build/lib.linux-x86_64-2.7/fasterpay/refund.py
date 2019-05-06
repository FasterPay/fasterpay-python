#!/usr/bin/python

import requests


class Refund:

    def __init__(self, gateway):
        self.gateway = gateway

    def process(self, order_id=None, amount=None):
        response = requests.post(self.gateway.config.get_api_url() + "/payment/" + str(order_id) + "/refund",
                                 data={"amount": amount},
                                 headers={"X-ApiKey": self.gateway.config.get_private_key()})

        return response.json()
