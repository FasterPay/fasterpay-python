
class PaymentForm:

    def __init__(self, gateway):
        self.gateway = gateway

    def build_form(self, parameters):
        parameters.update({"api_key": self.gateway.config.get_public_key()})
        parameters.update({"hash": self.gateway.signature().calculate_hash(parameters)})

        form = '<form align="center" method="post" action="' + self.gateway.config.get_api_url() + '/payment/form">'
        for param in parameters:
            form  += '<input type="hidden" name="' + param + '" value="' + str(parameters[param]) + '" />'

        form += '<input type="Submit" value="Pay Now"/></form>'
        return form
