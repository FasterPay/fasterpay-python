#!/usr/bin/python
import urllib
import urlparse
from fasterpay.gateway import FP_Gateway

fpGateway = FP_Gateway("<your private key>", "<your public key")

if __name__ == "__main__":
    pingback_data = urlparse.parse_qs("event=payment&payment_order%5Bid%5D=8057&payment_order%5Bmerchant_order_id%5D=w_903234503&payment_order%5Bpayment_system%5D=1&payment_order%5Bstatus%5D=successful&payment_order%5Bpaid_amount%5D=0.01&payment_order%5Bpaid_currency%5D=EUR&payment_order%5Bmerchant_net_revenue%5D=-0.2908&payment_order%5Bmerchant_rolling_reserve%5D=0.0005&payment_order%5Bfees%5D=0.3003&payment_order%5Bdate%5D%5Bdate%5D=2018-12-14+12%3A25%3A58.000000&payment_order%5Bdate%5D%5Btimezone_type%5D=3&payment_order%5Bdate%5D%5Btimezone%5D=UTC&user%5Bfirstname%5D=F&user%5Blastname%5D=P&user%5Busername%5D=F-P-1%40my.passport.io&user%5Bcountry%5D=IN&user%5Bemail%5D=faster%40fasterpay.co.in&with_risk_check=0");
    headers = {
        "X-ApiKey": "<your public key>"
    }

    if fpGateway.validate_pingback(pingback_data, headers) is True:
        fpGateway.acknowledge_pingback()
    else:
        print "NOK"
