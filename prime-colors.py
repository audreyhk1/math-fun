# https://www.youtube.com/watch?v=8x374slJGuo
import math
from colorutils import Color
global N_PRIMES
N_PRIMES = 256

def main():
    primes = get_primes()
    
    # # loop through every number
    # for i in range(2, 50):
    #     # is i prime?
    #     if i in primes:
    #         mix_colors()
    #     # is i composite?
    #     else:
    #         factors = get_prime_factors(i)
            
# get primes
# courtesy of https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
def get_primes(end_prime = N_PRIMES):
    primes = [2]

    r, g, b = 0
    for num in range(3,end_prime,2):
        if all(num % i != 0 for i in range(2,int(math.sqrt(num))+1)):
            # add to an array
            primes.append({"n": num, "color": []})
    
    return primes

# mix colors - https://github.com/edaniszewski/colorutils?tab=readme-ov-file#33-color-arithmetic
# make primes brighter, composites lighter
def mix_colors(factors, primes_list):
    pass


# get primes of composite number 
def get_prime_factors(n):
    factors = []
    for x in range (1, n + 1):
        if n % x == 0:
            factors.append(x)
    
    return factors
# add to map - https://matplotlib.org/stable/users/explain/colors/colormaps.html

if __name__ == "__main__":
    main()