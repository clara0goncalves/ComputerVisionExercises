#Color balance 
'''
Write a simple application to change the color balance of an image
by multiplying each color value by a different user-specified constant. If you want to get
fancy, you can make this application interactive, with sliders.
'''
import cv2
import numpy as np

def change_color_balance(image, red_ratio, green_ratio, blue_ratio):
    # Split the image into individual color channels
    blue, green, red = cv2.split(image)

    # Apply color balance ratios
    red = red * red_ratio
    green = green * green_ratio
    blue = blue * blue_ratio

    # Merge the color channels back into an image
    result_image = cv2.merge([blue, green, red])
    return result_image

def apply_gamma_transform(image, gamma):
    # Apply gamma transformation
    result_image = np.power(image/255.0, 1/gamma) * 255.0
    return result_image.astype(np.uint8)

# Load the input image
input_image_path = "test.jpg"
original_image = cv2.imread(input_image_path)

if original_image is None:
    print("Error: Unable to load the image.")
else:
    # Set color balance ratios
    red_ratio = 1.5  # You can adjust these values as needed
    green_ratio = 1.0
    blue_ratio = 1.0

    # Set gamma value
    gamma_value = 2.2  # You can adjust this value as needed

    # Apply color balance
    color_balanced_image = change_color_balance(original_image, red_ratio, green_ratio, blue_ratio)

    # Apply gamma transformation
    final_image = apply_gamma_transform(color_balanced_image, gamma_value)

    # Save the transformed image
    output_image_path = "output_image.jpg"
    cv2.imwrite(output_image_path, final_image)

    print("Image transformation complete. Output saved to:", output_image_path)

# 1. Do you get different results if you take out the gamma transformation before or after
# doing the multiplication? Why or why not?
    '''
    Yes, you get different results. The gamma transformation is a non-linear operation that changes the intensity distribution of pixel intensities in an image.
    The order of operations matters because each transformation interacts differently with the pixel values. 
    '''
    
# 2. Take the same picture with your digital camera using different color balance settings
# Can you recover what the color balance ratios are between the different settings? 

'''
Yes, you can recover the color balance ratios between different settings by comparing the pixel values of the same region in the image.
The color balance ratio values were obtained experimentally by taking the same picture with different color balance settings and comparing the pixel values of the same region in the image.
'''

# 3. If you have access to the RAW image for the camera, perform the demosaicing yourself
# or downsample the image resolution to get a “true” RGB image. 
# Does your camera perform a simple linear mapping between RAW values and the colorbalanced values in a JPEG? 
'''
The RAW image format contains unprocessed data from the camera's image sensor. To obtain an accurate representation of how the colors would look in a JPEG image, the RAW image must be demosaiced to obtain a true RGB image.  
The camera does not perform a simple linear mapping between RAW values and the color-balanced values in a JPEG. The RAW image data must be processed to obtain a color-balanced JPEG image.
'''

# 4. Can you think of any reason why you might want to perform a color twist on the images?

'''
Color twisting can be used to enhance or correct the color balance of an image. This process allows us to manipulate the intensity and hue of the colors in an image to achieve a desired effect.
For example, color twisting can be used to correct the color balance of an image that was captured under different lighting conditions, or to enhance the colors in an image to make it more visually appealing.
'''