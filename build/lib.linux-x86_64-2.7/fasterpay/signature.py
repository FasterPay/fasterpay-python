
import urllib
import hashlib

class Signature:

    def __init__(self, gateway):
        self.gateway = gateway

    def ksort(self, params):
        return [(k, params[k]) for k in sorted(params.keys())]

    def calculate_hash(self, params):
        urlencoded_params = urllib.urlencode(self.ksort(params)) + self.gateway.config.get_private_key()
        return hashlib.sha256(urlencoded_params.encode()).hexdigest()
