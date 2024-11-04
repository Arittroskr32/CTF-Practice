from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def extract_rsa_key_parameters(pem_file_path):
    # Read the PEM file
    with open(pem_file_path, 'rb') as pem_file:
        pem_data = pem_file.read()
    
    # Load the public key
    public_key = serialization.load_pem_public_key(pem_data, backend=default_backend())
    
    # Extract modulus and public exponent
    numbers = public_key.public_numbers()
    modulus = numbers.n
    exponent = numbers.e
    
    return modulus, exponent

def main():
    # Specify the path to your PEM file here using forward slashes or raw string
    pem_file_path = '/home/devil/CTF Istruction Files/CRYPTO/Data Formats/transparency_afff0345c6f99bf80eab5895458d8eab.pem'
    
    # Extract RSA parameters
    modulus, exponent = extract_rsa_key_parameters(pem_file_path)
    
    print("Modulus:", modulus)
    print("Exponent:", exponent)

if __name__ == '__main__':
    main()
