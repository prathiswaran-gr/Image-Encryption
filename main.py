from encryption import encrypt_image
from decryption import decrypt_image

input_image_path = 'lena.png'
encrypted_image_path = 'encrypted_image.png'
decrypted_image_path = 'decrypted_image.png'
arnold_iterations = 5

# Encrypt the image
encrypt_image(input_image_path, encrypted_image_path, arnold_iterations)

# Decrypt the image
decrypt_image(encrypted_image_path, decrypted_image_path, arnold_iterations)
