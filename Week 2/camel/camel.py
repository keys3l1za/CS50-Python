def camel_to_snake(variable_name):
    snake_name = ""
    for char in variable_name:
        if char.isupper():
            snake_name += "_" + char.lower()
        else:
            snake_name += char
    return snake_name

def main():
    camel_case_name = input("camelCase: ")
    snake_case_name = camel_to_snake(camel_case_name)
    print(f"snake_case: {snake_case_name}")

if __name__ == "__main__":
    main()
