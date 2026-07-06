from utils import (
    load_image,
    save_image,
    create_directory,
    resize_image
)

def apply_overlay(
        background,
        foreground
    ):
    background = background.copy()
    background_height, background_width = background.shape[:2]

    desired_width = int(background_width * 0.20)

    foreground = resize_image(
        foreground,
        width=desired_width
    )

    foreground_height, foreground_width = foreground.shape[:2]

    x = (background_width - foreground_width) // 2
    y = (background_height - foreground_height) // 2

    background[
        y:y+foreground_height,
        x:x+foreground_width
    ] = foreground

    return background

def process_overlay():
    create_directory("results")

    background = load_image("images/persona.jpg")
    foreground = load_image("images/unsa_logo.png")

    result = apply_overlay(background, foreground)

    save_image(
            f"results/overlay.png",
            result
        )

    print("Overlay generated.")