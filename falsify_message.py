from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


GENERATE_PRIVATE_KEY = False
DERIVE_PUBLIC_KEY_FROM_PRIVATE_KEY = False
PRIVATE_KEY_FILE = "bukenyakey.pem"
public_key = "bukenyakey.pub"
message = b'Bukenya hates cats'
signature = b'Fake Signature'

with open(PRIVATE_KEY_FILE, "rb") as key_file:
    public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend())

public_key.verify(
    signature,
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH),
                    hashes.SHA256()
)
print(signature)