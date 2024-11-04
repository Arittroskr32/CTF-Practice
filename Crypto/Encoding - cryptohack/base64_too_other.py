import base64

def base64_to_ascii(base64_string):
    # Decode base64 to bytes, then to ASCII
    bytes_data = base64.b64decode(base64_string)
    return bytes_data.decode('ascii', errors='ignore')

def base64_to_hex(base64_string):
    # Decode base64 to bytes, then to hexadecimal
    bytes_data = base64.b64decode(base64_string)
    return bytes_data.hex()

def base64_to_binary(base64_string):
    # Decode base64 to bytes, then convert each byte to binary and join
    bytes_data = base64.b64decode(base64_string)
    return ''.join(bin(byte)[2:].zfill(8) for byte in bytes_data)

def base64_to_decimal(base64_string):
    # Decode base64 to bytes, convert bytes to a hexadecimal string, then to decimal
    hex_string = base64_to_hex(base64_string)
    return int(hex_string, 16)

# Input base64 string
base64_string = "Y3J5cHRve1lvdV93aWxsX2JlX3dvcmtpbmdfd2l0aF9oZXhfc3RyaW5nc19hX2xvdH0="

# Perform conversions
ascii_value = base64_to_ascii(base64_string)
hex_value = base64_to_hex(base64_string)
binary_value = base64_to_binary(base64_string)
decimal_value = base64_to_decimal(base64_string)

# Print results
print(f"ASCII: {ascii_value}")
print(f"Hexadecimal: {hex_value}")
print(f"Binary: {binary_value}")
print(f"Decimal: {decimal_value}")
