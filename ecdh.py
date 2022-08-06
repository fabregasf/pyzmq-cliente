from secrets import token_bytes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey as ecpk
from base64 import b64encode
from Crypto.Cipher import AES

class ECDH:
    # ECDH parameters
    curve = "SECP256K1"
    tipo = "ecdh"

    def __init__(self):
        self.diffieHellman = ec.generate_private_key(ec.SECP256K1(), default_backend())
        self.public_key = self.diffieHellman.public_key()
        self.IV = token_bytes(16)

    def encrypt(self, public_key, secret):
        shared_key = self.diffieHellman.exchange(ec.ECDH(), public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=None,
            backend=default_backend()
        ).derive(shared_key)

        AES_OBJ = AES.new(derived_key, AES.MODE_CFB, iv=self.IV, segment_size=128)
        decrypt = AES_OBJ.encrypt(secret)

        return decrypt

    def decrypt(self, public_key, secret, iv):
        shared_key = self.diffieHellman.exchange(ec.ECDH(), public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=None,
            backend=default_backend()
        ).derive(shared_key)

        decrypt_cipher = AES.new(public_key, AES.MODE_CFB, iv=self.IV, segment_size=128)
        plain_text = decrypt_cipher.decrypt(secret)

        ecpk.public_
        return plain_text

    def debugClass(self):
        return self.curve



    