#!/usr/bin/python

import urllib
import hashlib
from config import FP_Config


class FP_Gateway:

    charge_fields = {
                        "required": ["description", "amount", "currency", "api_key", "merchant_order_id"],
                        "optional": ["success_url", "email", "first_name", "last_name", "city", "zip"]
                    }
    subscription_fields = {
                        "required": ["description", "amount", "currency", "api_key", "merchant_order_id", "recurring_name", "recurring_sku_id", "recurring_period"],
                        "optional": ["success_url", "email", "first_name", "last_name", "city", "zip", "recurring_trial_amount", "recurring_trial_period", "recurring_duration"]
                    }

    def __init__(self, private_key, public_key, api_url=None, api_version=None):
        self.fpConfig = FP_Config(private_key, public_key, api_url, api_version)

    def ksort(self, params):
        return [(k, params[k]) for k in sorted(params.keys())]

    def generate_signature(self, payload=None):
        payload.update({'api_key': self.fpConfig.get_public_key()})
        urlencoded_params = urllib.urlencode(self.ksort(payload)) + self.fpConfig.get_private_key()
        return hashlib.sha256(urlencoded_params.encode()).hexdigest()

    def initiate_payment(self, payload):
        return self.build_form_html(payload)

    def initiate_subscription(self, payload):
        return self.build_form_html(payload, True)

    def build_form_html(self, params, is_subscription=False):
        form_html = self.get_form_html()
        form_fields = self.generate_form_fields(params, is_subscription)
        if form_fields is not "":
            return form_html.format( self.fpConfig.get_api_url(),
                                     form_fields,
                                     self.fpConfig.get_public_key(),
                                     self.generate_signature(params))
        else:
            return "<h2> There was a Error Initiating Payment / Subscription </h2>"

    def get_form_html(self):
        html = "<form method=\"POST\" action=\"{}\" id=\"payment-form\"> \
                {} \
                <input type=\"hidden\" name=\"api_key\" value=\"{}\" /> \
                <input type=\"hidden\" name=\"hash\" value=\"{}\" /> \
            </form> \
            <script type=\"text/javascript\"> \
                document.getElementById(\"payment-form\").submit(); \
            </script>"

        return html

    def generate_form_fields(self, params, is_subscription=False):
        form_fields = ""
        fields_array = self.subscription_fields if is_subscription is True else self.charge_fields;

        try:
            # Parse Required fields
            for field in fields_array.get("required"):
                if field != "api_key":
                    form_fields += "<input type=\"hidden\" name=\"" + field + "\" value=\"" + params.get(field) + "\" /> "

            # Parse Optional Fields
            for field in fields_array.get("optional"):
                if field in params.keys():
                    form_fields += "<input type=\"hidden\" name=\"" + field + "\" value=\"" + params.get(field) + "\" /> "
        except (KeyError, TypeError):
            form_fields = ""

        return form_fields

    def validate_pingback(self, pingbackdata, headers):
        if "X-Apikey" in headers.keys():
            if headers.get("X-Apikey") == self.fpConfig.get_private_key():
                return True
        return False

    def acknowledge_pingback(self):
        return "OK"
