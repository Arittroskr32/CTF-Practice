import base64

def dec_to_hex(decimal_value):
    # Convert decimal to hex and ensure two-character hex format
    return format(decimal_value, '02x')

def hex_to_ascii(hex_string):
    # Convert combined hex string to bytes, then decode to ASCII
    bytes_data = bytes.fromhex(hex_string)
    return bytes_data.decode('ascii', errors='ignore')

def hex_to_binary(hex_string):
    # Convert combined hex string to binary
    return ''.join(bin(int(hex_string[i:i+2], 16))[2:].zfill(8) for i in range(0, len(hex_string), 2))

def hex_to_decimal(hex_string):
    # Convert combined hex string to decimal
    return int(hex_string, 16)

def hex_to_base64(hex_string):
    # Convert combined hex string to bytes, then encode to base64
    bytes_data = bytes.fromhex(hex_string)
    return base64.b64encode(bytes_data).decode('ascii')



# Input array of decimal values
# decimal_values = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

decimal_values = [72, 69, 76, 76, 79] # give values here




# Convert each decimal to hex and join into a single hex string
hex_values = ''.join(dec_to_hex(value) for value in decimal_values)
print(f"Combined Hexadecimal String: {hex_values}")

# Perform conversions on the combined hex string
ascii_value = hex_to_ascii(hex_values)
binary_value = hex_to_binary(hex_values)
decimal_value = hex_to_decimal(hex_values)
base64_value = hex_to_base64(hex_values)

# Print results
print(f"ASCII: {ascii_value}")
print(f"Binary: {binary_value}")
print(f"Decimal: {decimal_value}")
print(f"Base64: {base64_value}")
