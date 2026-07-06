import cv2

from utils import (
    load_image,
    save_image,
    to_gray,
    create_directory
)

def binary_threshold(image, threshold):
    _, result = cv2.threshold(
        image,
        threshold,
        255,
        cv2.THRESH_BINARY
    )

    return result

def process_thresholds():

    create_directory("results")

    image = load_image("images/laboratorio.png")

    gray = to_gray(image)

    thresholds = [60, 120, 180]

    for value in thresholds:
        result = binary_threshold(
            gray,
            value
        )

        save_image(
            f"results/threshold_{value}.png",
            result
        )

        print(
            f"Umbral {value} generado."
        )