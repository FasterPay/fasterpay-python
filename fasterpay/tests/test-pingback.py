#!/usr/bin/python

import urlparse
from fasterpay.gateway import Gateway

gateway = Gateway("4a6608170097835d0fbb856662e99da3", "e416c4de8ffd2b198d83713b8d232fab", True)

if __name__ == "__main__":
    pingback_data = '{"event":"payment","payment_order":{"id":13330,"merchant_order_id":"9654","payment_system":1,"status":"successful","paid_amount":0.01,"paid_currency":"EUR","merchant_net_revenue":-0.26079999999999998,"merchant_rolling_reserve":0.00050000000000000001,"fees":0.27029999999999998,"date":{"date":"2019-07-11 09:44:16.000000","timezone_type":3,"timezone":"UTC"}},"user":{"firstname":"Prashant","lastname":"D","username":"Prashant-D-1@my.passport.io","country":"IN","email":"prashant+testing@paymentwall.com"},"with_risk_check":false,"pingback_ts":1562838308}'
    headers = {
        "X-Fasterpay-Signature": "288f5edb0e1fb702f910b724c76819c4f925f28348e7b03bf5a4209d0b35d150",
        "X-Fasterpay-Signature-Version": "v2"
    }

    if gateway.pingback().validate(pingback_data, headers) is True:
        print "OK"
    else:
        print "NOK"
