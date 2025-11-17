#!/usr/bin/env python3
"""
Program takes 2 command-line arguments, the name/path of an image file to
read, & another to save as output (JPEG/JPG & PNG). The program then overlays
an image (`shirts.png`) onto the input image (resizing & croping), saving
the result as output.
"""
import sys
from pathlib import Path


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
        ...

    except FileNotFoundError:
        sys.exit("Specified input does not exist")


if __name__ == "__main__":
    main()
