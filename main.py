import os

TEXT = (
    "The kettle takes its time. Steam rises the way weather does, "
    "without hurry. Outside, a field is taking the light, taking it, "
    "and no one asks the field to hurry. You are somewhere warm. "
    "The day is long, and it is not waiting on you."
)

if not 1 <= len(TEXT) <= 280:
    raise SystemExit("entry text out of range")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
