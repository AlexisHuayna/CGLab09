import numpy as np
import cv2

from utils import create_directory, load_image, save_image, to_gray

def harris(
        color_image,
        gray_image,
        block_size=2,
        kernel_size=3,
        k=0.04
    ):
    gray = np.float32(gray_image)

    response = cv2.cornerHarris(
        gray,
        block_size,
        kernel_size,
        k
    )

    response = cv2.dilate(
        response,
        None
    )

    result = color_image.copy()

    result[
        response > 0.01 * response.max()
    ] = [0, 0, 255]

    return result

def process_corners():
    create_directory("results")

    image = load_image("images/laboratorio.png")

    gray = to_gray(image)

    result = harris(image, gray)

    save_image("results/harris.png", result)

    print("Harris generated.")