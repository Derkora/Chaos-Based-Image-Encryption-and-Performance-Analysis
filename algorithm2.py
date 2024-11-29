from PIL import Image
import numpy as np

def rossler_prng(size, a=0.2, b=0.2, c=5.7, x0=0.1, y0=0.1, z0=0.1):
    x, y, z = x0, y0, z0
    prng = []
    dt = 0.01  # Time step
    for _ in range(size):
        x_next = x + (-y - z) * dt
        y_next = y + (x + a * y) * dt
        z_next = z + (b + z * (x - c)) * dt
        prng.append(int((x_next % 1) * 255))  # Normalize to 0-255
        x, y, z = x_next, y_next, z_next
    return np.array(prng, dtype=np.uint8)

def process(image):
    img_array = np.array(image)
    prng = rossler_prng(img_array.size)
    key = prng.reshape(img_array.shape)
    encrypted = np.bitwise_xor(img_array, key)
    perf_metrics = {
        "key_min": int(key.min()),
        "key_max": int(key.max()),
        "key_mean": float(key.mean())
    }
    return Image.fromarray(encrypted), perf_metrics
