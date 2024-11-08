

'''
  Function to find the number of coprimes less than n based on Euler totient function
  Time complexity = O(sqrt(n) + k); 
    n is the input number
    k is the number of prime factors of n

  Parameters:
  -----------
    n: integer
       The input positive number  

  Returns:
  --------
    phi: integer
         Phi value of n (the number of coprimes < n)

  Examples:
  ---------
    >>> n_cp = Euler_Totient_SingleNum(11)
    >>> print(n_cp) 
    10

  See also:
    https://github.com/leduckhai/Awesome-Competitive-Programming/blob/main/Mathematics/Euler_Totient_NumList.ipynb    

  Reference: 
    https://en.wikipedia.org/wiki/Euler%27s_totient_function#Euler's_product_formula
    https://cp-algorithms.com/algebra/phi-function.html
'''

def Euler_Totient_SingleNum(n):
  '''
    Function to find all prime factors of a positive integer
    Time complexity = O(sqrt(n))

    See also:
      https://github.com/leduckhai/Awesome-Competitive-Programming/blob/main/Mathematics/PrimeFactorization.ipynb
  '''

  def PrimeFactorization(n):
    factors = []
    d = 2

    while n > 1:
      
      while n % d == 0:
        if d not in factors:
          factors.append(d)
        n /= d

      d += 1

      if d*d > n:
        if n > 1: 
          factors.append(int(n))
          break

    return factors

  # Core function
  PFs = PrimeFactorization(n) # All prime factors of n
  phi = n 

  for p in PFs:
    phi *= (1-1/p)

  return int(phi)



N = 155

a = Euler_Totient_SingleNum(N)
     
print(a)