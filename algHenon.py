# Henon Map
from PIL import Image
import numpy as np

def henon_map_prng(size, a=1.4, b=0.3, x0=0.1, y0=0.3):
    # Initialize variables
    x, y = x0, y0 
    prng = []
    
    # Generate pseudo-random numbers
    for _ in range(size):
        x_next = 1 - a * np.cos(x**6) + b * y
        y_next = -x
        prng.append(int((x_next % 1) * 255))  # Normalize to 0-255
        x, y = x_next, y_next
    return np.array(prng, dtype=np.uint8)

def process(image):
    # Convert image to numpy array
    img_array = np.array(image)
    prng = henon_map_prng(img_array.size)
    key = prng.reshape(img_array.shape)
    encrypted = np.bitwise_xor(img_array, key) # XOR

    return Image.fromarray(encrypted)