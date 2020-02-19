#!/usr/bin/python
import requests


class Transaction:

    def __init__(self, gateway):
        self.gateway = gateway

    def refund(self, order_id=None, amount=None):
        refund_response = self.do_http_post_request(
            self.gateway.config.get_api_url() + "/payment/" + str(order_id) + "/refund",
            {"amount": amount},
            {"X-ApiKey": self.gateway.config.get_private_key()})
        return refund_response

    def deliver(self, delivery_info):
        delivery_response = self.do_http_post_request(self.gateway.config.get_api_url() + "/api/v1/deliveries",
                                                      delivery_info,
                                                      {"X-ApiKey": self.gateway.config.get_private_key()})
        return delivery_response

    @staticmethod
    def do_http_post_request(url, data, headers):
        response = requests.post(url, data=data, headers=headers)
        return response.json()
