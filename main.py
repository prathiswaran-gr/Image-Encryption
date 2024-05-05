from encryption import *
from decryption import *
from correlationAnalysis import *

input_image_path = './input/input_image.png'
encrypted_image_path = './output/encrypted_image.png'
decrypted_image_path = './output/decrypted_image.png'
arnold_iterations = 5

print("------------------------Please wait------------------------")
# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, arnold_iterations)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, arnold_iterations)

output_file = './output/correlation_results.png'
correlation_analysis(decrypted_image_path, encrypted_image_path, output_file)