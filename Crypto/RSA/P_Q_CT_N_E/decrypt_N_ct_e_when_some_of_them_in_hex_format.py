from Crypto.Util.number import long_to_bytes
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# n, ct, e in hexadecimal format

n = 0x4ca21ede37e3d6a63bcee5f9120d0989f0143aae915302f346e8abbb840a72fb56d1487528ca75195b7832628389092c4e893fa4a6c9b0114266e805b12dc08d
e = 0x10001
c = 0x249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28

# factordb in decimal not in hexadecimal
p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
q = 77342270837753916396402614215980760127245056504361515489809293852222206596161

assert n == p * q

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

key = RSA.construct((n, e, d))
cipher = PKCS1_OAEP.new(key)
plaintext = cipher.decrypt(long_to_bytes(c))

print(plaintext)