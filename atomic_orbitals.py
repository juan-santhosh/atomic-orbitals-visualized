from periodic_table import periodic_table_list


def calc_orbitals(atomic_number):
    electron_config = periodic_table_list[atomic_number - 1].electron_configuration
    orbitals = []

    def orbital_remove(energy_level, subshell, orientation):
        orbitals.remove(f"{energy_level}{subshell}{orientation}")
    
    def append_orientations(subshell, starting_energy_level):
        for energy_level in range(electron_config.count(subshell)):
            for i in range(len(orientations)):
                orbitals.append(f"{energy_level + starting_energy_level}{subshell}{orientations[i]}")

    for i in range(electron_config.count("s")):
        orbitals.append(f"{i + 1}s")

    orientations = ["x", "y", "z"]
    append_orientations("p", 2)

    orientations = ["yz", "xz", "xy", "x^2-y^2", "z^2"]
    append_orientations("d", 3)

    orientations = ["x(x^2-3y^2)", "z(x^2-y^2)", "x(5z^2-r^2)", "z(5z^2-3r^2)", "y(5z^2-r^2)", "xyz", "y(3x^2-y^2)"]
    append_orientations("f", 4)

    removal_orientations = []
    for i in range(len(electron_config)):
        if electron_config[i] == "p":
            count = electron_config[i + 1]
            if count == "¹" or count == "²":
                removal_orientations.append("z")

            if count == "¹":
                removal_orientations.append("y")

            energy_level = electron_config[i - 1]
            for orientation in range(len(removal_orientations)):
                orbital_remove(energy_level, "p", removal_orientations[orientation])

        elif electron_config[i] == "d":
            count = electron_config[i + 1]

            if count == "¹" and electron_config[i + 2] == "⁰":
                continue
            else:
                if count == "¹" or count == "²" or count == "³" or count == "⁴":
                    removal_orientations.append("z^2")

                if count == "¹" or count == "²" or count == "³":
                    removal_orientations.append("x^2-y^2")
            
                if count == "¹" or count == "²":
                    removal_orientations.append("xy")
                
                if count == "¹":    
                    removal_orientations.append("xz")
                

            energy_level = electron_config[i - 1]
            for orientation in range(len(removal_orientations)):
                orbital_remove(energy_level, "d", removal_orientations[orientation])

    return orbitals
