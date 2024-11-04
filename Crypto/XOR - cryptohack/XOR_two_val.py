import re
import base64

def detect_type(value):
    # Check for binary
    if re.fullmatch(r'[01]+', value):
        return 'binary'
    
    # Check for decimal
    elif re.fullmatch(r'\d+', value):
        return 'decimal'
    
    # Check for hexadecimal
    elif re.fullmatch(r'([0-9a-fA-F]+)', value):
        return 'hexadecimal'
    
    # Check for Base64
    elif re.fullmatch(r'^[A-Za-z0-9+/]+={0,2}$', value):
        return 'base64'
    
    # If it's ASCII, assume it doesn't match any of the above
    return 'ascii'

def convert_to_int(value, value_type):
    if value_type == 'binary':
        return int(value, 2)
    elif value_type == 'decimal':
        return int(value)
    elif value_type == 'hexadecimal':
        return int(value, 16)
    elif value_type == 'base64':
        decoded_bytes = base64.b64decode(value)
        return int.from_bytes(decoded_bytes, 'big')
    elif value_type == 'ascii':
        return int.from_bytes(value.encode(), 'big')

def xor_values(val1, val2):
    return val1 ^ val2

def format_output(result):
    # Convert integer result to different formats
    binary_result = bin(result)
    hex_result = hex(result)
    decimal_result = str(result)
    base64_result = base64.b64encode(result.to_bytes((result.bit_length() + 7) // 8, 'big')).decode()
    try:
        ascii_result = result.to_bytes((result.bit_length() + 7) // 8, 'big').decode('utf-8', 'ignore')
    except:
        ascii_result = "Cannot convert to ASCII."

    return binary_result, ascii_result, hex_result, base64_result, decimal_result

def main():
    # Get inputs
    input1 = input("Enter the first value: ")
    input2 = input("Enter the second value: ")

    # Detect types
    type1 = detect_type(input1)
    type2 = detect_type(input2)

    print(f"Detected types: {type1}, {type2}")

    # Convert both inputs to integers
    int1 = convert_to_int(input1, type1)
    int2 = convert_to_int(input2, type2)

    # Perform XOR
    xor_result = xor_values(int1, int2)

    # Format and display output
    binary_result, ascii_result, hex_result, base64_result, decimal_result = format_output(xor_result)
    print("Binary Output:", binary_result)
    print("ASCII Output:", ascii_result)
    print("Hexadecimal Output:", hex_result)
    print("Base64 Output:", base64_result)
    print("Decimal Output:", decimal_result)

# Run the main function
main()
