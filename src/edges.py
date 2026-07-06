import cv2

from utils import create_directory, load_image, save_image, to_gray

def sobel_x(image, kernel_size=3):
    sobel = cv2.Sobel(
        image,
        cv2.CV_64F,
        1,
        0,
        ksize=kernel_size
    )

    return cv2.convertScaleAbs(sobel)

def sobel_y(image, kernel_size=3):
    sobel = cv2.Sobel(
        image,
        cv2.CV_64F,
        0,
        1,
        ksize=kernel_size
    )

    return cv2.convertScaleAbs(sobel)

def sobel(image, kernel_size=3):
    x = sobel_x(image, kernel_size)
    y = sobel_y(image, kernel_size)

    return cv2.addWeighted(
        x,
        0.5,
        y,
        0.5,
        0
    )

def process_edges():
    create_directory("results")

    image = load_image("images/laboratorio.png")

    gray = to_gray(image)

    image_sobel_x = sobel_x(gray)

    save_image("results/image_sobel_x.png", image_sobel_x)

    image_sobel_y = sobel_x(gray)

    save_image("results/image_sobel_y.png", image_sobel_y)

    image_sobel = sobel(gray)

    save_image("results/image_sobel.png", image_sobel)

    print("Edges generated.")