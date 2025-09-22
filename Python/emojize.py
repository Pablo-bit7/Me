#!/usr/bin/env python3
"""
Prompts user for a str in English and outputs the “emojized” version
"""
import emoji


def main():
    try:
        usr_npt = input("Input: ").strip()

        if "_" in usr_npt:
            print(f"Output: {emoji.emojize(usr_npt)}")
        
        else:
            ...
    
    except ValueError:
        return
    except EOFError:
        return
    
    else:
        ...


if __name__ == "__main__":
    main()
