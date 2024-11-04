from math import gcd

# Function to find modular inverse
def mod_inverse(g, p):
    # Check if modular inverse exists
    if gcd(g, p) != 1:
        return None  # No solution if gcd(g, p) is not 1
    # Using pow to calculate modular inverse
    return pow(g, -1, p)

# Input from user
g = int(input("Enter the value of 'g': "))
a = int(input("Enter the value of 'a': "))
p = int(input("Enter the modulus 'p': "))

# Calculate modular inverse of g mod p
inverse_g = mod_inverse(g, p)

# If inverse exists, calculate d
if inverse_g is not None:
    d = (inverse_g * a) % p
    print(f"The value of d such that {g} * d ≡ {a} (mod {p}) is: d = {d}")
else:
    print(f"No solution exists for {g} * d ≡ {a} (mod {p}) because gcd({g}, {p}) ≠ 1.")
