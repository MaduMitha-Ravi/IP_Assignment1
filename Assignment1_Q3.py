"""
---------------------------------------------------------------------------------------------------------------
Author: Madu Mitha Ravi
Purpose: Assignment 1 - Question 3
Algorithm: Bit Masking
Description: Performs update to intensity level of an image
Time Taken: Takes less than 1 minute
---------------------------------------------------------------------------------------------------------------
"""

import numpy as np
import os
from PIL import Image
from io import BytesIO


def compute_square(n):
    """
    Return the square root value
    """
    sqrt = np.sqrt(n)
    return int(sqrt)


def open_image():
    """
    open_image function reads the image rose.raw in grayscale format, converts to array data for further processing
    """
    rawData = open("rose.raw", 'rb').read()
    imgSize = (256, 256)  
    img = Image.frombytes('L', imgSize, rawData)
    original_image = np.asarray(img)

    return original_image


def copy_image(original_image):
    """
    Image is copied so that the copied image cna be processed
    """
    original_image1 = original_image.copy()
    return original_image1


def update_intensity(original_image1, intensity_level):
    """
    Image is updated with the intensity levels by masking
    """
    sqrt = compute_square(intensity_level)
    n_bits = int(np.log2(sqrt))

    if n_bits < 8:
        bitmask = int(f"{'1' * n_bits}{'0' * (8 - n_bits)}", 2)
        original_image1 = original_image1 & bitmask

    Image.fromarray(original_image1,mode='L')

    save_image(original_image1, intensity_level)


def save_image(original_image1, intensity_level):
    """
    save_newresizeImage function saves the resized image in raw format 
    """
    filename = 'q3_updatedintensitylevel_%s.raw' % intensity_level
    np.array(original_image1).tofile(filename)


if __name__ == "__main__":
    """
    Main function from where the necessary functions are called for Changing the intensity levels of the image rose.raw
    """
    original_image = open_image()
    original_image1 = copy_image(original_image)
    update_intensity(original_image1, 128)

    original_image1 = copy_image(original_image)
    update_intensity(original_image1, 64)

    original_image1 = copy_image(original_image)
    update_intensity(original_image1, 32)

    original_image1 = copy_image(original_image)
    update_intensity(original_image1, 16)