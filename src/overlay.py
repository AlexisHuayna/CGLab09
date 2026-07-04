def applY_overlay(
        background,
        foreground
    ):
    background_height, background_width = background.shape[:2]
    foreground_height, foreground_width = foreground.shape[:2]

    area = background_height * background_width * 0.2