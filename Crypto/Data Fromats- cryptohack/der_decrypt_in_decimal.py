
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

# Load DER data from a file
with open("2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der", "rb") as der_file:
    der_data = der_file.read()

# Load the DER-encoded x509 certificate
cert = x509.load_der_x509_certificate(der_data, default_backend())

# Extract the public key
public_key = cert.public_key()

# Ensure the public key is RSA, then extract the modulus
if isinstance(public_key, rsa.RSAPublicKey):
    modulus = public_key.public_numbers().n
    print("Modulus as a decimal integer:", modulus)
else:
    print("The certificate does not contain an RSA public key.")
