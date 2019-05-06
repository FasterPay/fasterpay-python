#!/usr/bin/python

from fasterpay.gateway import Gateway

if __name__ == "__main__":

    gateway = Gateway("<your private key>", "<your public key>")

    refundResponse = gateway.refund().process(1167, 0.01)

    print refundResponse
