
class PaymentForm:

    def __init__(self, gateway):
        self.gateway = gateway

    def build_form(self, parameters):
        payload = parameters.get("payload")
        payload.update({"api_key": self.gateway.config.get_public_key()})

        if "sign_version" in payload:
            hash = self.gateway.signature().calculate_hash(payload, payload.get("sign_version"))
        else:
            hash = self.gateway.signature().calculate_hash(payload)

        payload.update({"hash": hash})

        form = '<form align="center" method="post" action="' + self.gateway.config.get_api_url() + '/payment/form">'
        for param in payload:
            form  += '<input type="hidden" name="' + param + '" value="' + str(payload[param]) + '" />'

        form += '<input type="Submit" value="Pay Now" id="fasterpay-submit"/></form>'

        if "auto_submit_form" in parameters:
            form += "<script type=\"text/javascript\">document.getElementById(\"fasterpay-submit\").click(); </script>"

        return form