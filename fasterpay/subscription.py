#!/usr/bin/python

import requests


class Subscription:

    def __init__(self, gateway):
        self.gateway = gateway

    def cancel(self, order_id=None):
        response = requests.post(self.gateway.config.get_api_url() + "/api/subscription/" + str(order_id) + "/cancel",
                                 data={},
                                 headers={"X-ApiKey": self.gateway.config.get_private_key()})

        return response.json()
