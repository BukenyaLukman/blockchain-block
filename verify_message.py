from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

## GENERATE PRIVATE KEY
## private_key = rsa.generate_private_key(
# public_exponent = 65537,
# key_size = 2048,
# backend = default_backend()
# )

# Configuration
GENERATE_PRIVATE_KEY = False
DERIVE_PUBLIC_KEY_FROM_PRIVATE_KEY = False
PRIVATE_KEY_FILE = "bukenyakey.pem"
PUBLIC_KEY_FILE = "bukenyakey.pub"
MESSAGE = b"Bukenya likes cat"


# Message validation executed by other people
public_key.verify(
    signature,
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256())