
import urllib
import hashlib, hmac


class Signature:

    def __init__(self, gateway):
        self.gateway = gateway

    def ksort(self, params):
        return [(k, params[k]) for k in sorted(params.keys())]

    def calculate_hash(self, params, scheme = "v1"):
        if scheme is "v1":
            urlencoded_params = urllib.urlencode(self.ksort(params)) + self.gateway.config.get_private_key()
            return hashlib.sha256(urlencoded_params.encode()).hexdigest()
        else:
            encoded_string = ''
            for k, v in self.ksort(params):
                encoded_string += k+"="+v+";"
            return hmac.new(self.gateway.config.get_private_key(), encoded_string, digestmod=hashlib.sha256).hexdigest()

    def calculate_pingback_hash(self, pingbackdata, is_string=True):
        if is_string is True:
            return hmac.new(self.gateway.config.get_private_key(), pingbackdata, digestmod=hashlib.sha256).hexdigest()
