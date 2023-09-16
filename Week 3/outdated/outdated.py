def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date_input = input("Date: ")
            parts = date_input.split("/")

            if len(parts) == 3:
                month, day, year = map(int, parts)
            else:
                month, day, year = parse_date_input(date_input, months)

            if not (1 <= month <= 12) or not (1 <= day <= 31) or not (0 <= year <= 9999):
                raise ValueError("Invalid date.")

            formatted_date = f"{year:04d}-{month:02d}-{day:02d}"
            print(formatted_date)
            break
        except (ValueError, IndexError):
            continue

def parse_date_input(date_input, months):
    parts = date_input.split(" ")
    month = months.index(parts[0]) + 1
    day = int(parts[1].rstrip(","))
    year = int(parts[2])
    return month, day, year

if __name__ == "__main__":
    main()
