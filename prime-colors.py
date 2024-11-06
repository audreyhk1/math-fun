# https://www.youtube.com/watch?v=8x374slJGuo
import math
import numpy as np
# from colorutils import Color
from PIL import Image
import matplotlib.pyplot as plt
import mixbox
import random
global N_PRIMES
N_PRIMES = 310248241 

def main():
    global N_PRIMES
    primes_numbers, primes_colors = get_primes(N_PRIMES)
    random.shuffle(primes_colors)
    
    # colors = np.array([0, 0, 0])
    # for i in range(1, 200):
    #     colors = np.concatenate((colors, [i, i, i]), axis=0)
    # color_image = Image.fromarray(colors, mode="RGB")
    
    # color_image.save("primes.jpeg")
    
    pixel_arr = []
    print(primes_colors)
    
    prime_index = 0
    # # loop through every number
    for i in range(2, N_PRIMES):
        # is i prime?
        if i in primes_numbers:
            pixel_arr.append(primes_colors[prime_index])
            prime_index += 1
        # is i composite?
        else:
            pixel = []
            factors = get_prime_factors(i)
            # loop through factors
            for factor in factors[1:]:
                # get factor color from index in primes_number
                try:
                    color = primes_colors[primes_numbers.index(factor)]
                    if factor != factors[1]:
                        pixel = mix_colors(pixel, color)
                    else:
                        pixel = color
                except ValueError:
                    pass
            pixel_arr.append(pixel)
    
    np_pixel_arr = np.array(pixel_arr)   
      
                
            
# get primes
# courtesy of https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
def get_primes(end_prime):
    primes_colors = []
    primes_numbers = [2]

    r, g, b = 0, 1, 1
    r_flag, g_flag, b_flag = True, False, False
    for num in range(3,end_prime,2):
        if all(num % i != 0 for i in range(2,int(math.sqrt(num))+1)):
            # add to an array
            if r_flag:
                primes_colors.append([r, 0, 0])
                primes_numbers.append(num)
                r += 1
                if r > 256:
                    g_flag = True
                    r_flag = False
            elif g_flag:
                primes_colors.append([0, g, 0])
                primes_numbers.append(num)
                g += 1
                if g > 256:
                    b_flag = True
                    g_flag = False
            elif b_flag and b < 256:
                primes_colors.append([0, 0, b])
                primes_numbers.append(num)
                b += 1
                
            else:
                return primes_numbers, primes_colors

# mix colors - https://github.com/scrtwpns/mixbox/tree/master/python
# make primes brighter, composites lighter
def mix_colors(color1, color2):
    centroid_color = []
    for i in range(len(color1)):
        centroid_color.append(int((color1[i] + color2[i]) / 2))
    return centroid_color


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