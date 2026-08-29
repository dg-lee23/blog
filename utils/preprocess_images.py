# preprocess_images.py
from pathlib import Path
from PIL import Image

IMG_DIR = Path("static/images")
SIZE = 512

for path in IMG_DIR.iterdir():
    if not path.is_file():
        continue
    img = Image.open(path).convert("RGB")
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    img = img.crop((left, top, left + side, top + side))
    img = img.resize((SIZE, SIZE), Image.LANCZOS)
    img.save(path)  # overwrite, same name/format
    print(f"{path.name}: {w}x{h} -> {SIZE}x{SIZE}")