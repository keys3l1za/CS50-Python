def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))

            if y == 0 or x > y:
                print("ZeroDivisionError")
                continue

            percentage = (x / y) * 100
            rounded_percentage = round(percentage)

            if rounded_percentage <= 1:
                print("E")
            elif rounded_percentage >= 99:
                print("F")
            else:
                print(f"{rounded_percentage}%")

            break
        except ValueError:
            print("ValueError")
        except ZeroDivisionError:
            print("ZeroDivisionError")

if __name__ == "__main__":
    main()
