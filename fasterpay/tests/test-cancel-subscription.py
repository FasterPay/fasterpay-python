#!/usr/bin/python

from fasterpay.gateway import Gateway
from random import randint

if __name__ == "__main__":

    gateway = Gateway("<your private key>", "<your public key>")

    response = gateway.subscription().cancel(order_id=1171)

    print response