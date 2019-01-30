#!/usr/bin/python

import urllib
import hashlib
from config import FP_Config

class FP_Gateway:

    def __init__(self, privateKey, publicKey, apiUrl=None, apiVersion = None):
        self.fpConfig = FP_Config(privateKey, publicKey, apiUrl, apiVersion)

    def ksort(self, params):
        return [(k, params[k]) for k in sorted(params.keys())]

    def generate_signature(self, payload=None):
        payload.update({'api_key': self.fpConfig.get_public_key()})
        urlencodedParams = urllib.urlencode(self.ksort(payload))
        urlencodedParams += self.fpConfig.get_private_key()
        print urlencodedParams
        return hashlib.sha256(urlencodedParams.encode()).hexdigest()

    def initiate_transaction(self, payload):
        signature = self.generate_signature(payload)
        formHtml = self.build_form_html(payload, signature)
        return formHtml

    def build_form_html(self, params, signature):
        formHtml = "<form method=\"POST\" action=\"{}\" id=\"payment-form\"> \
					<input type=\"hidden\" name=\"description\" value=\"{}\" /> \
					<input type=\"hidden\" name=\"amount\" value=\"{}\" /> \
					<input type=\"hidden\" name=\"currency\" value=\"{}\" /> \
					<input type=\"hidden\" name=\"api_key\" value=\"{}\" /> \
					<input type=\"hidden\" name=\"merchant_order_id\" value=\"{}\" /> \
					<input type=\"hidden\" name=\"success_url\" value=\"{}\" /> \
					<input type=\"hidden\" name=\"hash\" value=\"{}\" /> \
				</form> \
				<script type=\"text/javascript\"> \
					document.getElementById(\"payment-form\").submit(); \
				</script>"

        return formHtml.format(self.fpConfig.get_api_url(), params.get("description"), params.get("amount"),
                      params.get("currency"), self.fpConfig.get_public_key(), params.get("merchant_order_id"), params.get("success_url"), signature)

    def validate_pingback(self, pingbackdata, headers):
        if "X-Apikey" in headers.keys():
            if headers.get("X-Apikey") == self.fpConfig.get_private_key():
                return True
        return False

    def acknowledge_pingback(self):
        return "OK"
