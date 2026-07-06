import numpy as np
import cv2

from src.threshold import binary_threshold
from utils import (
    load_image,
    save_image,
    create_directory,
    to_gray,
    create_kernel
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

def add_salt_pepper_noise(
        image,
        amount=0.02,
        salt_ratio=0.5
    ):
    noisy = image.copy()

    height, width = image.shape[:2]

    total_pixels = height * width

    num_noisy = int(total_pixels * amount)
    num_salt = int(num_noisy*salt_ratio)
    num_pepper = num_noisy - num_salt

    rows = np.random.randint(0, height, num_salt)
    cols = np.random.randint(0, width, num_salt)
    noisy[
        rows,
        cols
    ] = 255

    rows = np.random.randint(0, height, num_pepper)
    cols = np.random.randint(0, width, num_pepper)

    noisy[
        rows,
        cols
    ] = 0

    return noisy

def process_morphology(size=3):
    create_directory("results")

    image = load_image("images/persona.jpg")

    gray = to_gray(image)

    binary = binary_threshold(
            gray,
            120
        )
    
    save_image(
        f"results/binary.png",
        binary
    )
    
    noisy = add_salt_pepper_noise(binary,0.10)

    save_image(
        f"results/noisy.png",
        noisy
    )
    
    kernel = create_kernel()

    opened = opening(noisy, kernel)

    save_image(
        f"results/opening.png",
        opened
    )

    closed = closing(noisy, kernel)

    save_image(
        f"results/closing.png",
        closed
    )

    print("Morphology generated.")