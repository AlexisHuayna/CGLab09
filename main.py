from src.threshold import process_thresholds
from src.watermark import process_watermark
from src.overlay import process_overlay
from src.morphology import process_morphology
from src.filters import process_filters

TASKS = [
    process_thresholds,
    process_watermark,
    process_overlay,
    process_morphology,
    process_filters
]

for task in TASKS:
    print(f"Ejecutando {task.__name__} ...")
    task()