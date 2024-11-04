
print(" Input looks like a ^ n mod m = answer ")

# Input from user
a = int(input("Enter the base 'a': "))
n = int(input("Enter the exponent 'n': "))
m = int(input("Enter the modulus 'm': "))

# Calculating a^n mod m
result = pow(a, n, m)

# Displaying the result
print(f"The value of {a}^{n} mod {m} is: {result}")
