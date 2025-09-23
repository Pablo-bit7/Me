#!/usr/bin/env python3
"""
Prompts user for a str in English and outputs the “emojized” version
"""
import emoji


def main():
    try:
        usr_npt = input("Input: ").strip()
        print(f"Output: {emoji.emojize(usr_npt, language='alias')}")
    
    except (ValueError, EOFError):
        return


if __name__ == "__main__":
    main()
