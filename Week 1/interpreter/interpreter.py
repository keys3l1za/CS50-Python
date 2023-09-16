def interpret_expression(expression):
    x, operator, z = expression.split(" ")

    x = int(x)
    z = int(z)

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z

    return result

def main():
    u_input = input("Expression: ")
    result = interpret_expression(u_input)
    formatted_result = "{:.1f}".format(result)
    print(f"{formatted_result}")

if __name__ == "__main__":
    main()
