import numpy as np
from PIL import Image
def fibonacci_transformation(image, encrypt=True):
    pixels = np.array(image)
    max_val = np.max(pixels)

    a, b = 0, 1
    fib_sequence = [a]
    while b < max_val:
        fib_sequence.append(b)
        a, b = b, a + b

    for i in range(len(fib_sequence)):
        if encrypt:
            pixels = np.bitwise_xor(pixels, fib_sequence[i])
        else:
            pixels = np.bitwise_xor(pixels, fib_sequence[len(fib_sequence) - i - 1])

    return Image.fromarray(pixels)
