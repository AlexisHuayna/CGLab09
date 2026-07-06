from utils import adjust_brightness_contrast, create_directory, gaussian_blur, load_image, median_blur, save_image


def process_filters():

    create_directory("results")

    image = load_image("images/persona.jpg")

    brighter = adjust_brightness_contrast(image, beta=50)

    save_image("results/brighter.png", brighter)

    darker = adjust_brightness_contrast(image, beta=-50)

    save_image("results/darker.png", darker)

    high_contrast = adjust_brightness_contrast(image, alpha=1.5)

    save_image("results/high_contrast.png", high_contrast)

    low_contrast = adjust_brightness_contrast(image, alpha=0.7)

    save_image("results/low_contrast.png", low_contrast)

    gaussian = gaussian_blur(brighter)

    save_image("results/gaussian.png", gaussian)

    median = median_blur(low_contrast)

    save_image("results/median.png", median)
    
    print("Filters generated.")
