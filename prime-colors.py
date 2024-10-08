# https://www.youtube.com/watch?v=8x374slJGuo
import math
import numpy as np
# from colorutils import Color
from PIL import Image
global N_PRIMES
N_PRIMES = 310248241 

def main():
    global N_PRIMES
    primes = get_primes(N_PRIMES)
    
    colors = np.array([
        [[0, 0 ,0], [1, 0, 0]],
        [[3, 0 ,0], [1, 0, 0]],
    ])
    color_image = Image.fromarray(colors, mode="RGB")
    color_image.save("primes.jpeg")
    
    # # loop through every number
    # for i in range(1, 100 + 1):
    #     # is i prime?
    #     if i in primes:
    #         mix_colors()
    #     # is i composite?
    #     else:
    #         factors = get_prime_factors(i)
            
# get primes
# courtesy of https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
def get_primes(end_prime):
    primes = [2]

    r, g, b = 0, 1, 1
    r_flag, g_flag, b_flag = True, False, False
    for num in range(3,end_prime,2):
        if all(num % i != 0 for i in range(2,int(math.sqrt(num))+1)):
            # add to an array
            if r_flag:
                primes.append({"n": num, "color": [r, 0, 0]})
                r += 1
                if r > 256:
                    g_flag = True
                    r_flag = False
            elif g_flag:
                primes.append({"n": num, "color": [0, g, 0]})
                g += 1
                if g > 256:
                    b_flag = True
                    g_flag = False
            elif b_flag and b < 256:
                primes.append({"n": num, "color": [0, 0, b]})
                b += 1
                
            else:
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
# https://stackoverflow.com/questions/69117672/how-to-make-a-color-grid-in-python-using-pil
# https://stackoverflow.com/questions/43971138/python-plotting-colored-grid-based-on-values
# https://www.codecademy.com/resources/docs/pillow/image/fromarray

if __name__ == "__main__":
    main()