#!/usr/bin/env python3
"""
Program takes 2 command-line arguments, the name/path of an image file to
read, & another to save as output (JPEG/JPG & PNG). The program then overlays
an image (`shirts.png`) onto the input image (resizing & croping), saving
the result as output.
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    accepted_extensions = (".png", ".jpg", ".jpeg")

    if not input_file_path.lower().endswith(accepted_extensions) or not output_file_path.lower().endswith(accepted_extensions):
        sys.exit("Invalid input")

    elif Path(input_file_path).suffix.lower() != Path(output_file_path).suffix.lower():
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(input_file_path) as base_img:
            base_img_copy = base_img.copy()

            with Image.open("shirt.png") as shirt_img:
                shirt_img_size = shirt_img.size
                base_img_resized = ImageOps.fit(base_img_copy, shirt_img_size)

                composite_img = base_img_resized.paste(shirt_img, shirt_img)


    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
