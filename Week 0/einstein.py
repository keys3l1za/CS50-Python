def main():
    mass = int(input("m: "))
    speed_of_light = 300000000
    energy = calculate_energy(mass, speed_of_light)
    print(f"E: {energy}")

def calculate_energy(mass, speed_of_light):
    energy = mass * speed_of_light ** 2
    return energy

if __name__ == "__main__":
    main()
