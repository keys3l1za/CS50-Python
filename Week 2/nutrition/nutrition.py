def main():
    fruit_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew": 50,
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
        "tangerine":50,
        "watermelon": 80
    }

    fruit_input = input("Item: ").lower()

    if fruit_input in fruit_calories:
        calories = fruit_calories[fruit_input]
        print(f"Calories: {calories}")

if __name__ == "__main__":
    main()
