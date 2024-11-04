from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# Load PEM data from a file
with open("private_key_filename_give_here.pem", "rb") as pem_file:
    pem_data = pem_file.read()

# Load the private key
private_key = serialization.load_pem_private_key(
    pem_data,
    password=None,  # Use a password if the key is encrypted
    backend=default_backend()
)

# Extract the private numbers
private_numbers = private_key.private_numbers()
d = private_numbers.d  # This is the private key component 'd'

# Display 'd' as a decimal integer
print("Private Key 'd' as a decimal integer:", d)
