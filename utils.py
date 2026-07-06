import cv2
import matplotlib.pyplot as plt
import os

def load_image(path):
    image = cv2.imread(path)

    if image is None:
        raise FileNotFoundError(
            f"No se encontro la image: {path}"
        )
    
    return image

def show_image(title, image):
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(8,6))

    plt.imshow(rgb)
    
    plt.title(title)

    plt.axis("off")

    plt.show()

def save_image(path, image):
    cv2.imwrite(path, image)

def create_directory(path):
    os.makedirs(path, exist_ok=True)

def resize_image(image, width=None, height=None):
    h, w = image.shape[:2]

    if width is None and height is None:
        return image
    
    if width is None:
        ratio = height / h
        width = int(w * ratio)
    else:
        ratio = width / w
        height = int(h * ratio)
    
    resized = cv2.resize(
        image,
        (width, height),
        interpolation=cv2.INTER_AREA
    )

    return resized

def to_gray(image):
    return cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

def create_kernel(size=3):
    return cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (size, size)
    )

def opening(image, kernel):
    return cv2.morphologyEx(
        image,
        cv2.MORPH_OPEN,
        kernel
    )

def closing(image, kernel):
    return cv2.morphologyEx(
        image,
        cv2.MORPH_CLOSE,
        kernel
    )

def adjust_brightness_contrast(
        image,
        alpha=0.1,
        beta=0
    ):
    return cv2.convertScaleAbs(
        image,
        alpha=alpha,
        beta=beta
    )

def gaussian_blur(
        image,
        kernel_size=5
    ):
    return cv2.GaussianBlur(
        image,
        (kernel_size, kernel_size),
        0
    )

def median_blur(
        image,
        kernel_size=5
    ):
    return cv2.medianBlur(
        image,
        kernel_size
    )