import numpy as np
from PIL import Image
def arnold_mapping(image, iterations, encrypt=True):
    width, height = image.size
    pixels = np.array(image)

    for _ in range(iterations):
        new_pixels = np.zeros_like(pixels)
        for i in range(width):
            for j in range(height):
                if encrypt:
                    new_i = (2 * i + j) % width
                    new_j = (i + j) % height
                else:
                    new_i = (i - j) % width
                    new_j = (-i + 2 * j) % height
                new_pixels[new_i, new_j] = pixels[i, j]

        pixels = new_pixels

    return Image.fromarray(pixels) 