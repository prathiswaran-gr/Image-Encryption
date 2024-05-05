import os
from PIL import Image
from arnoldMapping import arnold_mapping
from fibonacciTransformation import fibonacci_transformation

def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating directory. '+ directory)
            
            
def encrypt_image(image_path, output_path, arnold_iterations):
    original_image = Image.open(image_path)

    # Arnold Mapping
    arnold_scrambled = arnold_mapping(original_image, arnold_iterations)

    # Fibonacci Transformation
    encrypted_image = fibonacci_transformation(arnold_scrambled)


    createFolder("C:/Users/prath/OneDrive/Desktop/Project/output")
    
    # Save the encrypted image
    encrypted_image.save(output_path)
    print("Image encrypted and saved successfully.")

