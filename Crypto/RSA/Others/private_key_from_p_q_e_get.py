from sympy import mod_inverse

# Given values
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537

# Calculate φ(N)
phi_N = (p - 1) * (q - 1)

# Calculate the private key d as the modular inverse of e mod φ(N)
d = mod_inverse(e, phi_N)
print("d = ",d)
