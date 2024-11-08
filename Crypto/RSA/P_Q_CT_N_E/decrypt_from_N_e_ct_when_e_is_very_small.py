#!/usr/bin/env python3
import gmpy2
from Crypto.Util import number

"""
Because m is small, m^3 is close to n, so we can compute the 3-th root of c + k*n where k=0,1,2...
"""

n = 17258212916191948536348548470938004244269544560039009244721959293554822498047075403658429865201816363311805874117705688359853941515579440852166618074161313773416434156467811969628473425365608002907061241714688204565170146117869742910273064909154666642642308154422770994836108669814632309362483307560217924183202838588431342622551598499747369771295105890359290073146330677383341121242366368309126850094371525078749496850520075015636716490087482193603562501577348571256210991732071282478547626856068209192987351212490642903450263288650415552403935705444809043563866466823492258216747445926536608548665086042098252335883
e = 3
ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

def low_e_attack(ct, e, n):
    i = 0
    while True:
        
        y, r = gmpy2.iroot(ct + i * n, e)  # Return the integer n-th root of x and boolean value that is True iff the root is exact. x >= 0. n > 0.
  
        if r == True:
            print(f"i = {i}")
            # Print output in hexadecimal format
            hex_output = hex(y)[2:]
            print(f"Decrypted message (hex): {hex_output}")

            # Print output in ASCII format
            flag = number.long_to_bytes(y).decode()
            print(f"Decrypted message (ASCII): {flag}")
            
            # Print output in long to bytes
            print(f"Decrypted message (long to bytes): {number.long_to_bytes(y)}")
            
            # Print output in decimal format
            print(f"Decrypted message (decimal): {y}")
            
            # Print output in bytes to long format
            print(f"Decrypted message (bytes to long): {number.bytes_to_long(number.long_to_bytes(y))}")
            
            exit()
        i = i + 1

if __name__ == "__main__":
    low_e_attack(ct, e, n)
