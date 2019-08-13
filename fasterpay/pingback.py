


class Pingback:

    def __init__(self, gateway):
        self.gateway = gateway

    def validate(self, pingbackdata, headers):
        if len(headers) == 0:
            return False

        if len(pingbackdata) == 0:
            return False

        if headers.get("X-Fasterpay-Signature-Version") == "v2":
            generated_hash = self.gateway.signature().calculate_pingback_hash(pingbackdata)
            if generated_hash == headers.get("X-Fasterpay-Signature"):
                return True
        else:
            if headers.get("X-ApiKey") == self.gateway.config.get_private_key():
                return True

        return False
