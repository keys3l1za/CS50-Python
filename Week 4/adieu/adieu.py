import inflect

def main():
    p = inflect.engine()
    names = []

    print("Name:")

    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    if names:
        print_farewells(names, p)

def print_farewells(names, p):
    for i, name in enumerate(names):
        if i == len(names) - 1:
            print(f"Adieu, adieu, to {name}")
        elif i == len(names) - 2:
            print(f"Adieu, adieu, to {name} and {names[i + 1]}")
        else:
            print(f"Adieu, adieu, to {name},", end=" ")

    if len(names) > 2:
        print(f"and {names[-1]}")

if __name__ == "__main__":
    main()
