# Get user input for the encrypted message and flag format
encrypted_msg_input = input("Enter the encrypted hex message ( e.g., 0e0b213f... ) : ")
flag_format_input = input("Enter the flag format (e.g., crypto{  ) : ")

# Convert the hex input to bytes
encrypted_msg = bytes.fromhex(encrypted_msg_input)

# Convert flag format input to bytes
flag_format = flag_format_input.encode()  # Encoding the string to bytes

# Calculate the key
key = [o1 ^ o2 for (o1, o2) in zip(encrypted_msg, flag_format)] + [ord("y")]

# Decrypt the flag
flag = []
key_len = len(key)
for i in range(len(encrypted_msg)):
    flag.append(encrypted_msg[i] ^ key[i % key_len])

# Convert the decrypted flag to a string
flag = "".join(chr(o) for o in flag)

# Print the result
print("Flag:")
print(flag)
