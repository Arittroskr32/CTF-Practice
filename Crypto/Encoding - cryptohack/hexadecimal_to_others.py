import base64

def hex_to_ascii(hex_string):
    # Convert hex string to bytes, then decode to ASCII
    bytes_data = bytes.fromhex(hex_string)
    return bytes_data.decode('ascii', errors='ignore')

def hex_to_binary(hex_string):
    # Convert hex string to binary, 8 bits for each hex byte
    return ''.join(bin(int(hex_string[i:i+2], 16))[2:].zfill(8) for i in range(0, len(hex_string), 2))

def hex_to_decimal(hex_string):
    # Convert hex string to decimal
    return int(hex_string, 16)

def hex_to_base64(hex_string):
    # Convert hex string to bytes, then encode to base64
    bytes_data = bytes.fromhex(hex_string)
    return base64.b64encode(bytes_data).decode('ascii')

# Input hexadecimal string
# hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
hex_string = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

# Perform conversions
ascii_value = hex_to_ascii(hex_string)
binary_value = hex_to_binary(hex_string)
decimal_value = hex_to_decimal(hex_string)
base64_value = hex_to_base64(hex_string)

# Print results
print(f"ASCII: {ascii_value}")
print(f"Binary: {binary_value}")
print(f"Decimal: {decimal_value}")
print(f"Base64: {base64_value}")
