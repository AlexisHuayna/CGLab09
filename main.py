from src.threshold import process_thresholds
from src.watermark import process_watermark
from src.overlay import process_overlay
from src.morphology import process_morphology
from src.filters import process_filters
from src.edges import process_edges
from src.corners import process_corners

TASKS = [
    process_thresholds,
    process_watermark,
    process_overlay,
    process_morphology,
    process_filters,
    process_edges,
    process_corners
]

for task in TASKS:
    print(f"Ejecutando {task.__name__} ...")
    task()