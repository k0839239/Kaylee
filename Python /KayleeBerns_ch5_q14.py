def kinetic_energy(mass, velocity):
    return .5 * mass * velocity ** 2


if __name__ == "__main__":
    input_mass = input("Enter value for mass")
    input_velocity = input("Enter value for velocity")
    print(kinetic_energy(int(input_mass), int(input_velocity)))


