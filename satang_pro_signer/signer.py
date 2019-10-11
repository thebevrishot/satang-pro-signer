import hashlib
import hmac

from satang_pro_signer import preparer

class Signer:
    def __init__(self, secret: bytes):
        self.secret = secret

    def sign(self, obj) -> bytes:

        parsed = preparer.Preparer(obj).encode()
        msg = bytes(parsed, encoding='utf-8')

        return hmac.digest(self.secret, msg, 'sha512')