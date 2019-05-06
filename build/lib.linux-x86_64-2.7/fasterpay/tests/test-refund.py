#!/usr/bin/python

from fasterpay.gateway import Gateway

if __name__ == "__main__":

    gateway = Gateway("t_ff9cb7bb402405b742341330a817b1", "t_f2883f81526dfd32d2ded7778d1999")

    refundResponse = gateway.refund().process(1167, 0.01)

    print refundResponse
