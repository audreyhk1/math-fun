import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import itertools


def main():
    # create an array with all colors
    color_array = create_color_array()
    n_colors = 100000
    print("Retived color_array")
    
    # get all primes
    primes_array = get_primes(n_colors - 1)
    print("Retrieved primes_array")
    
    prime_colors = []
    for prime in primes_array:
        prime_colors.append((color_array[prime], prime))
    print("Retrieved get_prime_colors")
    
    # create mosaic
    rows = math.ceil(math.sqrt(len(prime_colors)))  # Ensure rows are an integer
    cols = math.ceil(len(prime_colors) / rows)
    create_mosaic(prime_colors, [rows, cols])
        
        

    

# create an array with all colors RGB as tuples
def create_color_array():
    # https://chatgpt.com/share/6768e9a7-6a1c-8010-931e-ed3f9e54f9d0
    hi = list(itertools.product(range(256), repeat=3))
    print(len(hi))
    return hi

# retrieve all primes from 2 to N using the Sieve of Erathoneses
# courtesy of https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/#
def get_primes(n):
    prime_sieve = [True for i in range(n+1)]
    # start prime
    p = 2
    
    while (p * p <= n):
        if (prime_sieve[p] == True):
            for i in range(p * p, n+1, p):
                prime_sieve[i] = False
        p += 1
    
    # create an array
    primes_array = []
    for p in range(2, n+1):
        if prime_sieve[p]:
            primes_array.append(p)
            
    return primes_array

# https://chatgpt.com/share/6768eff2-bba0-8010-95ae-d103eaaff915
def create_mosaic(prime_colors_tuples, grid_length):
    rows, cols = grid_length
    fig, ax = plt.subplots(figsize=(cols, rows))
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.axis('off')
    
    for idx, ((r, g, b), label) in enumerate(prime_colors_tuples):
        row = idx // cols
        col = idx % cols
        
        color = (r / 255, g / 255, b / 255)
        
        rect = patches.Rectangle((col, rows - row - 1), 1, 1, linewidth=0, edgecolor=None, facecolor=color)
        ax.add_patch(rect)
        
        ax.text(col + 0.5, rows - row - 0.5, str(label), color='white', 
                ha='center', va='center', fontsize=10, fontweight='bold')

    plt.savefig("primes.jpeg")

if __name__ == "__main__":
    main()