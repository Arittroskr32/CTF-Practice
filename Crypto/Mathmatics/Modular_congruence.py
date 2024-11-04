
print(" Sameple : 11 ≡ x mod 6 ")

# Input from user
a = int(input("Enter the value for 'a' (e.g., 11): "))

m = int(input("Enter the modulus 'm' (e.g., 6): "))

# Solve the modular congruence
x = a % m

# Displaying the result
print(f"The solution to {a} ≡ x (mod {m}) is x = {x}")
