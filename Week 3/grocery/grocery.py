def main():
    grocery_list = {}
    while True:
        try:
            item = input("")
            if item.lower() == "q" or item.lower() == "quit":
                break

            item = item.lower()
            grocery_list[item] = grocery_list.get(item, 0) + 1
        except EOFError:
            break

    sorted_items = sorted(grocery_list.items())

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
