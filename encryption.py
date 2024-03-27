from PIL import Image
from arnoldMapping import arnold_mapping
from fibonacciTransformation import fibonacci_transformation
def encrypt_image(image_path, output_path, arnold_iterations):
    original_image = Image.open(image_path)

    # Arnold Mapping
    arnold_scrambled = arnold_mapping(original_image, arnold_iterations)

    # Fibonacci Transformation
    encrypted_image = fibonacci_transformation(arnold_scrambled)

    # Save the encrypted image
    encrypted_image.save(output_path)
    print("Image encrypted and saved successfully.")


