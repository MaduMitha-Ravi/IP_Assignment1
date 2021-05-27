"""
---------------------------------------------------------------------------------------------------------------
Author: Madu Mitha Ravi
Purpose: Assignment 1 - Question 1
Algorithm: Single Point Resampling & Resizing
Description: Performs resizing of a raw image to the specified resolution and saves them as resized raw image
Time Taken: Takes less than 1 minute 
---------------------------------------------------------------------------------------------------------------
"""

import math
import numpy as np
import os
from pylab import *
from PIL import Image
from io import BytesIO


def singlepoint_resample(image, N, M, x, y):
    """
    singlepoint_resample function performs the resampling of the pixel data, from the original image this function gets the pixel value that needs to be updated for the new image resolution
    """
    i = int(x)
    j = int(y)
    
    s = x - i
    t = y - j
   
    result = image[j][i] * (1 - s) * (1 - t) + image[j][i+1] * s * (1 - t) + image[j+1][i] * t * (1 - s) + image[j+1][i+1] * s * t
    
    return result

    
def singlepoint_resize(image,N, M,resized, N1, M1):
    """
    singlepoint_resize function calculates the distance for the resized image - Dx and Dy, then it iterates through the pixels and calls the resample function to get the pixel value for that coordinate
    """
    Dx = float((N-1)/(N1-1))
    Dy = float((M-1)/(M1-1))
    y = 0.0 
    for j in range(M1-1):
        x = 0.0
        for i in range(N1-1):
            resized[j][i] = singlepoint_resample(image, N, M, x, y)
            x += Dx
        y += Dy
    
    return resized

def save_newresizeImage(newImg, fname):
    """
    save_newresizeImage function saves the resized image in raw format 
    """
    filename = '%s' % fname
    np.array(newImg).tofile(filename)


def read_grayscaleimage(filename, size):
    """
    read_grayscaleimage function reads the image rose.raw or museum.raw in grayscale format, then saves it as a jpeg to get the array data for further processing
    """
    img = open(filename, 'rb').read()
    img = Image.frombytes('L', size , img)
    img.save("tmp.jpeg")  

    image_array = np.array((img))

    return image_array

    
if __name__ == "__main__":

    """
    Main function from where the necessary functions are called for resizing the image for the requested resolution
    """

    """
    a) Input image filename: “rose.raw”
    Original resolution: 256x256
    New resolution: 500x500
    b) Input image filename: “rose.raw”
    Original resolution: 256x256
    New resolution: 1000x1000
    """

    filename = "rose.raw"
    size = (256, 256)  
    
    image_array0 = read_grayscaleimage(filename, size)
    resized0 = np.empty([500, 500])
    singlepoint_image0 = singlepoint_resize(image_array0,256, 256,resized0,500,500)
    save_newresizeImage(singlepoint_image0, 'q1_resizedimage1_500x500.raw')

    image_array1 = read_grayscaleimage(filename, size)
    resized1 = np.empty([1000, 1000])
    singlepoint_image1 = singlepoint_resize(image_array1,256, 256,resized1,1000,1000)
    save_newresizeImage(singlepoint_image1, 'q1_resizedimage2_1000x1000.raw')

    """
    c) Input image filename: “museum.raw”
    Original resolution: 1280x960
    New resolution: 640x480
    d) Input image filename: “museum.raw”
    Original resolution: 1280x960
    New resolution: 320x240
    e) Input image filename: “museum.raw”
    Original resolution: 1280x960
    New resolution: 160x120
    """

    filename1 = "museum.raw"
    size1 = (1280, 960)  
    image_array2 = read_grayscaleimage(filename1, size1)
    resized2 = np.empty([480, 640])
    singlepoint_image2 = singlepoint_resize(image_array2,1280, 960, resized2,640,480)
    save_newresizeImage(singlepoint_image2, 'q1_resizedimage3_640x480.raw')

    image_array3 = read_grayscaleimage(filename1, size1)
    resized3 = np.empty([240, 320])
    singlepoint_image3 = singlepoint_resize(image_array3,1280, 960, resized3,320,240)
    save_newresizeImage(singlepoint_image3, 'q1_resizedimage4_320x240.raw')

    image_array4 = read_grayscaleimage(filename1, size1)
    resized4 = np.empty([120, 160])
    singlepoint_image4 = singlepoint_resize(image_array4,1280, 960, resized4,160,120)
    save_newresizeImage(singlepoint_image4, 'q1_resizedimage5_160x120.raw')