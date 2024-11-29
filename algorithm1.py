from PIL import Image
import numpy as np

def henon_map_prng(size, a=1.4, b=0.3, x0=0.1, y0=0.3):
    x, y = x0, y0
    prng = []
    for _ in range(size):
        x_next = 1 - a * np.cos(x**6) + b * y
        y_next = -x
        prng.append(int((x_next % 1) * 255))  # Normalize to 0-255
        x, y = x_next, y_next
    return np.array(prng, dtype=np.uint8)

def process(image):
    img_array = np.array(image)
    prng = henon_map_prng(img_array.size)
    key = prng.reshape(img_array.shape)
    encrypted = np.bitwise_xor(img_array, key)
    perf_metrics = {
        "key_min": int(key.min()),
        "key_max": int(key.max()),
        "key_mean": float(key.mean())
    }
    return Image.fromarray(encrypted), perf_metrics
