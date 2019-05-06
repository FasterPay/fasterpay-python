#!/usr/bin/python

from fasterpay.gateway import Gateway
from random import randint

if __name__ == "__main__":

    gateway = Gateway("t_ff9cb7bb402405b742341330a817b1", "t_f2883f81526dfd32d2ded7778d1999")

    response = gateway.subscription().cancel(order_id=1168)

    print response