# Hocam çalışması için PIL kütüphanesini indirmeyi unutmayınız.
# 39. satırdaki image_path'e örnek olarak bir resim indirip onun path'ini verebilirsiniz.
# PIL için -> pip install pillow

from PIL import Image
from collections import Counter

def find_most_common_pixel_color(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = list(img.getdata()) 
    color_counts = Counter(pixels)

    most_common_color, most_common_count = color_counts.most_common(1)[0]

    return most_common_color, most_common_count

def find_most_common_pattern(image_path, n):
    img = Image.open(image_path).convert("RGB")
    width, height = img.size
    patterns = []

    for row in range(height - n + 1):
        for col in range(width - n + 1):
            block = []
            for r in range(row, row + n):
                row_pixels = []
                for c in range(col, col + n):
                    row_pixels.append(img.getpixel((c, r)))
                block.append(tuple(row_pixels))
            patterns.append(tuple(block))

    pattern_counts = Counter(patterns)

    most_common_pattern, most_common_count = pattern_counts.most_common(1)[0]

    return most_common_pattern, most_common_count

if __name__ == "__main__":
    image_path = "fractal.png" # Hocam buraya örnek fraktal resminizin adresini veriniz.
    color, count = find_most_common_pixel_color(image_path)
    print(f"Most common color: {color}, Count: {count}")
    n = 3 
    pattern, pattern_count = find_most_common_pattern(image_path, n)
    print(f"Most common {n}x{n} pattern: {pattern}, Count: {pattern_count}")