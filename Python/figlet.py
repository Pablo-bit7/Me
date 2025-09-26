#!/usr/bin/env python3
"""
Program takes 2 or no command-line arguments
(1st being `-f` or `--font`, and the 2nd being the name of a font),
prompts the user for input, then returns the input in the font specified
or a random font if unspecified
"""
import sys
import random
from pyfiglet import Figlet


def main():
    prompt = input("Input: ").strip()

    try:
        figlet = Figlet()

        if len(sys.argv) == 1:
            figlet.setFont(font=random.choice(figlet.getFonts()))
        
        elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
            if sys.argv[2] in figlet.getFonts():
                figlet.setFont(font=sys.argv[2])
            else:
                sys.exit("Invalid font")

        else:
            sys.exit("Invalid usage")
    
    except (ValueError, KeyboardInterrupt, EOFError):
        return

    print(figlet.renderText(prompt))


if __name__ == "__main__":
    main()
