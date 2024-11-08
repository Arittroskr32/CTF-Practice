# Given values
n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767
e = 1
ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485

# Step 1: Since e = 1, decryption is trivial; the message is the ciphertext modulo n
decrypted_message = ct % n

# Step 2: Print in various formats
# Hexadecimal format
hex_message = hex(decrypted_message)

# ASCII format (if the message is in ASCII)
try:
    ascii_message = bytes.fromhex(hex_message[2:]).decode('utf-8', errors='ignore')
except ValueError:
    ascii_message = "Non-printable ASCII"

# Decimal (integer) format
decimal_message = decrypted_message

# Long integer to bytes
message_bytes = decimal_message.to_bytes((decimal_message.bit_length() + 7) // 8, byteorder='big')

# Bytes to long integer format
long_from_bytes = int.from_bytes(message_bytes, byteorder='big')

# Output the different formats
print("Decrypted message in Hexadecimal format:", hex_message)
print("Decrypted message in ASCII format:", ascii_message)
print("Decrypted message in Decimal format:", decimal_message)
print("Decrypted message in Bytes format:", message_bytes)
print("Decrypted message (Bytes to Long):", long_from_bytes)
