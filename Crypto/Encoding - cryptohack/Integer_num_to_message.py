# Import the necessary function from PyCryptodome
from Crypto.Util.number import long_to_bytes

# Function to convert an integer to a message
def integer_to_message(number):
    # Convert the integer to bytes
    byte_representation = long_to_bytes(number)
    
    # Decode the bytes to a string (message)
    decoded_message = byte_representation.decode('utf-8', errors='ignore')  # Using 'ignore' to skip decoding errors
    return decoded_message

# Given integer
number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer to a message
message = integer_to_message(number)
print("Decoded Message:", message)
