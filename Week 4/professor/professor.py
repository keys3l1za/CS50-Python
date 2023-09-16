import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y = generate_integer(level)
        correct_answer = x + y
        tries = 0

        while tries < 3:
            user_answer = get_user_answer(x, y)

            if user_answer == correct_answer:
                score += 1
                break
            else:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"Correct answer: {correct_answer}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass

def generate_integer(level):
    max_value = 10 ** level - 1
    x = random.randint(0, max_value)
    y = random.randint(0, max_value)
    return x, y

def get_user_answer(x, y):
    while True:
        try:
            user_answer = int(input(f"{x} + {y} =  "))
            return user_answer
        except ValueError:
            pass

if __name__ == "__main__":
    main()
