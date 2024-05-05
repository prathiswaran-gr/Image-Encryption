from PIL import Image
from arnoldMapping import arnold_mapping
from fibonacciTransformation import fibonacci_transformation
def decrypt_image(image_path, output_path, arnold_iterations):
    encrypted_image = Image.open(image_path)

    # Inverse Fibonacci Transformation
    decrypted_fibonacci = fibonacci_transformation(encrypted_image, encrypt=False)

    # Inverse Arnold Mapping
    decrypted_image = arnold_mapping(decrypted_fibonacci, arnold_iterations, encrypt=False)

    # Save the decrypted image
    decrypted_image.save(output_path)
    print("Image decrypted and saved successfully.")