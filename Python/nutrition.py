#!/usr/bin/env python3
"""
Program prompts consumers user for a fruit and outputs the number of calories in one portion of that fruit
"""


def main():
    fruit = input("Item: ").strip().lower()

    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    if fruit in fruits:
        print(f"Calories: {fruits[fruit]}")
    else:
        pass


if __name__ == "__main__":
    main()
