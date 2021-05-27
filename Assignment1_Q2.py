"""
---------------------------------------------------------------------------------------------------------------
Author: Madu Mitha Ravi
Purpose: Assignment 1 - Question 2
Algorithm: Weighted Single Point Resampling & Resizing
Description: Performs weighted resizing of a raw image to the specified resolution and saves them as resized raw image
Time Taken: Takes around 35 minutes (by reducing k, execution time can be reduced)
---------------------------------------------------------------------------------------------------------------
"""

import math
import numpy as np
import os
from pylab import *
from PIL import Image
from io import BytesIO


def weighted_resample(image, N, M, x, y):
    """
    weighted_resample function performs the resampling of the pixel data, from the original image this function gets the pixel value that needs to be updated for the new image resolution
    """
    i = int(x)
    j = int(y)
    
    s = x - i
    t = y - j
   
    result = image[j][i] * (1 - s) * (1 - t) + image[j][i+1] * s * (1 - t) + image[j+1][i] * t * (1 - s) + image[j+1][i+1] * s * t
    
    return result

    
def weighted_resize(image,N, M,resized, N1, M1):
    """
    weighted_resize function calculates the distance for the resized image - Dx and Dy, then it iterates through the pixels and calls the resample function iterating for k/2 times to get the weighted sum of pixel value for that coordinate
    """
    Dx = float((N-1)/(N1-1))
    Dy = float((M-1)/(M1-1))
    y = 0.0 

    # Value of k is selected based on d value that d is less than 1 (pixel) for all the cases in this assignment
    k = 11
    d = Dx/(k-1)
    print(d, k)
    for j in range(M1-1):
        x = 0.0
        for i in range(N1-1):
            #resized[j][i] = singlepoint_resample(image, N, M, x, y)
            
            new_k = int(k/2) 
            totalsum = 0.0
            for s in range(-new_k, new_k):
                for t in range(-new_k, new_k):
                    totalsum += weighted_resample(image, N, M, x+new_k*d, y+new_k*d)
                    resized[j][i] = int(totalsum/(k*k))
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
    Main function from where the necessary functions are called for resizing the image for the requested resolution using the weighted approach
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
    weighted_resized0 = np.empty([500, 500])
    weighted_image0 = weighted_resize(image_array0,256, 256,weighted_resized0,500,500)
    save_newresizeImage(weighted_image0, 'q2_resizedimage1_500x500.raw')

    image_array1 = read_grayscaleimage(filename, size)
    weighted_resized1 = np.empty([1000, 1000])
    weighted_image1 = weighted_resize(image_array1,256, 256,weighted_resized1,1000,1000)
    save_newresizeImage(weighted_image1, 'q2_resizedimage2_1000x1000.raw')

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
    weighted_resized2 = np.empty([480, 640])
    weighted_image2 = weighted_resize(image_array2,1280, 960, weighted_resized2,640,480)
    save_newresizeImage(weighted_image2, 'q2_resizedimage3_640x480.raw')

    image_array3 = read_grayscaleimage(filename1, size1)
    weighted_resized3 = np.empty([240, 320])
    weighted_image3 = weighted_resize(image_array3,1280, 960, weighted_resized3,320,240)
    save_newresizeImage(weighted_image3, 'q2_resizedimage4_320x240.raw')

    image_array4 = read_grayscaleimage(filename1, size1)
    weighted_resized4 = np.empty([120, 160])
    weighted_image4 = weighted_resize(image_array4,1280, 960, weighted_resized4,160,120)
    save_newresizeImage(weighted_image4, 'q2_resizedimage5_160x120.raw')
    