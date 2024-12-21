# Hocam çalışması için PIL kütüphanesini indirmeyi unutmayınız.
# 40. satırdaki image_path'e örnek olarak bir resim indirip onun path'ini verebilirsiniz.
# PIL için -> pip install pillow

import sys
from PIL import Image

def calculate_bw_percentage(image_path):
    image = Image.open(image_path).convert("RGBA")

    pixels = image.getdata()

    black_count = 0
    white_count = 0
    total_count = 0

    for pixel in pixels:
        r, g, b, a = pixel

        if a == 0:
            continue

        if (r, g, b) == (0, 0, 0):
            black_count += 1
        elif (r, g, b) == (255, 255, 255):
            white_count += 1
        
        total_count += 1

    if total_count == 0:
        return 0.0, 0.0

    black_percentage = (black_count / total_count) * 100.0
    white_percentage = (white_count / total_count) * 100.0

    return black_percentage, white_percentage


def main():
    image_path = "yin_yang.png" # Hocam buraya örnek yin yang resminizin adresini veriniz. (dosya png olmazsa sonuç hatalı olacaktır.)
    black_perc, white_perc = calculate_bw_percentage(image_path)
    print(f"Black: {black_perc:.2f}%")
    print(f"White: {white_perc:.2f}%")


if __name__ == "__main__":
    main()