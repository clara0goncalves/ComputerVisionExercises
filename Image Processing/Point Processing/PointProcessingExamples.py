from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def display_image_with_label(ax, image, title):
    ax.imshow(image)
    ax.set_title(title)
    ax.axis('off')

def point_processing_transformations(image):
    fig, axes = plt.subplots(2, 4, figsize=(12, 6))
    fig.suptitle("Point Processing Transformations", fontsize=16)

    # Original
    display_image_with_label(axes[0, 0], image, "Original Image")

    # Darken
    darken_image = image - 50
    display_image_with_label(axes[0, 1], darken_image, "Darken: f(x) = x - 50")

    # Lower Contrast
    lower_contrast_image = image * 0.5
    display_image_with_label(axes[0, 2], lower_contrast_image, "Lower Contrast: f(x) = 0.5 * x")

    # Non-linear
    non_linear_image = np.power(image, 0.5)
    display_image_with_label(axes[0, 3], non_linear_image, "Non-linear: f(x) = x^(0.5)")

    # Invert
    invert_image = 255 - image
    display_image_with_label(axes[1, 0], invert_image, "Invert: f(x) = 255 - x")

    # Lighten
    lighten_image = image + 50
    display_image_with_label(axes[1, 1], lighten_image, "Lighten: f(x) = x + 50")

    # Raise Contrast
    raise_contrast_image = image * 2
    display_image_with_label(axes[1, 2], raise_contrast_image, "Raise Contrast: f(x) = 2 * x")

    # Non-linear Raise Contrast
    non_linear_raise_contrast_image = np.power(image, 2)
    display_image_with_label(axes[1, 3], non_linear_raise_contrast_image, "Non-linear Raise Contrast: f(x) = x^2")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    # Load an example image (replace 'your_image_path.jpg' with the actual path to your image)
    image_path = 'cat.jpg'
    original_image = np.array(Image.open(image_path))

    # Check if the image is loaded successfully
    if original_image is not None:
        point_processing_transformations(original_image)
    else:
        print("Error loading the image. Please check the image path.")
