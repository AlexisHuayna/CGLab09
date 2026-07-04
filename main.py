from src.threshold import process_thresholds
from src.watermark import process_watermark

TASKS = [
    process_thresholds,
    process_watermark
]

for task in TASKS:
    print(f"Ejecutando {task.__name__} ...")
    task()