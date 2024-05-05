import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate2d
from PIL import Image

def correlation_analysis(image_path_plaintext, image_path_ciphertext, output_file):
    # Load the image
    plain_image = Image.open(image_path_plaintext).convert('L')  # Convert to grayscale
    cipher_image = Image.open(image_path_ciphertext).convert('L')
    plain_pixels = np.array(plain_image)
    cipher_pixels = np.array(cipher_image)

    # Define correlation kernels for different orientations
    horizontal_kernel = np.array([[1, 1, 1],
                                  [0, 0, 0],
                                  [-1, -1, -1]])
    vertical_kernel = np.array([[1, 0, -1],
                                [1, 0, -1],
                                [1, 0, -1]])
    diagonal_kernel = np.array([[1, 0, -1],
                                [0, 0, 0],
                                [-1, 0, 1]])

    # Compute correlation for plaintext
    plaintext_horizontal_corr = correlate2d(plain_pixels, horizontal_kernel, mode='same')
    plaintext_vertical_corr = correlate2d(plain_pixels, vertical_kernel, mode='same')
    plaintext_diagonal_corr = correlate2d(plain_pixels, diagonal_kernel, mode='same')

    # Compute correlation for ciphertext
    ciphertext_horizontal_corr = correlate2d(cipher_pixels, horizontal_kernel, mode='same')
    ciphertext_vertical_corr = correlate2d(cipher_pixels, vertical_kernel, mode='same')
    ciphertext_diagonal_corr = correlate2d(cipher_pixels, diagonal_kernel, mode='same')

    # Concatenate the correlation analysis results
    concatenated_results = np.concatenate((plaintext_horizontal_corr, 
                                           plaintext_vertical_corr, 
                                           plaintext_diagonal_corr,
                                           ciphertext_horizontal_corr, 
                                           ciphertext_vertical_corr, 
                                           ciphertext_diagonal_corr), axis=1)

    # Plot the correlation analysis results with space between images
    fig, axs = plt.subplots(2, 3, figsize=(15, 10), gridspec_kw={'height_ratios': [1, 1.5]})

    im0 = axs[0, 0].imshow(plaintext_horizontal_corr, cmap='hot', interpolation='nearest')
    axs[0, 0].set_title('Plain image\nHorizontal Correlation')
    axs[0, 0].set_xlabel('Pixel Index')
    axs[0, 0].set_ylabel('Pixel Index')
    
    cbar = fig.colorbar(im0, ax=axs, orientation='vertical', label='Correlation Coefficient')
    cbar.ax.yaxis.set_ticks_position('left')  # Set ticks on the left side

    # Plot vertical correlation
    axs[0, 1].imshow(plaintext_vertical_corr, cmap='hot', interpolation='nearest')
    axs[0, 1].set_title('Vertical Correlation')


    # Plot diagonal correlation
    axs[0, 2].imshow(plaintext_diagonal_corr, cmap='hot', interpolation='nearest')
    axs[0, 2].set_title('Diagonal Correlation')
  
    
    axs[1, 0].imshow(ciphertext_horizontal_corr, cmap='hot', interpolation='nearest')
    axs[1, 0].set_title('Cipher image\nHorizontal Correlation')
    axs[1, 0].set_xlabel('Pixel Index')
    axs[1, 0].set_ylabel('Pixel Index')


    # Plot vertical correlation
    axs[1, 1].imshow(ciphertext_vertical_corr, cmap='hot', interpolation='nearest')
    axs[1, 1].set_title('Vertical Correlation')
   

    # Plot diagonal correlation
    axs[1, 2].imshow(ciphertext_diagonal_corr, cmap='hot', interpolation='nearest')
    axs[1, 2].set_title('Diagonal Correlation')
    
  

    # Adjust layout and save the plot
    plt.savefig(output_file)
    plt.close()
    print("Correlation analysis image generated and saved successfully.")

