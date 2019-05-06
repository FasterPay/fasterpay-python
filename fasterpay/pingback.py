

class Pingback:

    def __init__(self, gateway):
        self.gateway = gateway

    def validate(self, params):

        if len(params) == 0:
            return False

        if "apiKey" not in params.keys():
            return False

        if params.get("apiKey") == self.gateway.config.get_private_key():
            return True

        return False