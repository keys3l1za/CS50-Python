def convert(time):
    hours_str, minutes_str = time.split(":")
    hours = int(hours_str)
    minutes = int(minutes_str)
    return hours + minutes / 60.0

def main():
    u_time = input("What time is it? ")
    time_in_hours = convert(u_time)

    if 7.0 <= time_in_hours < 10.0:
        print("It's breakfast time")
    elif 12.0 <= time_in_hours < 16.0:
        print("It's lunch time")
    elif 18.0 <= time_in_hours < 21.0:
        print("It's dinner time")

if __name__ == "__main__":
    main()
