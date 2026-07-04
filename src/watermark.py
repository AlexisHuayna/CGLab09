import cv2

from utils import (
    load_image,
    save_image,
    resize_image,
    create_directory
)

def apply_watermark(
        image,
        watermark,
        alpha=0.85,
        beta=0.15
    ):
    image_height, image_width = image.shape[:2]

    desired_width = int(image_width * 0.15)

    watermark = resize_image(watermark, width=desired_width)

    logo_height, logo_width = watermark.shape[:2]

    margin = 20

    x = image_width - logo_width - margin
    y = image_height - logo_height - margin

    roi = image[
        y:y+logo_height,
        x:x+logo_width
    ]

    blended = cv2.addWeighted(
        roi,
        alpha,
        watermark,
        beta,
        0
    )

    image[
        y:y+logo_height,
        x:x+logo_width
    ] = blended

    return image

def process_watermark():
    create_directory("results")

    image = load_image("images/persona.jpg")
    watermark = load_image("images/unsa_logo.png")

    result = apply_watermark(image,watermark)

    save_image(
            f"results/watermark.png",
            result
        )
    

    print(
        f"Watermark generated."
    )
