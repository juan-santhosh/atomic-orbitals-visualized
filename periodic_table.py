class Atom:
    def __init__(
        self,
        name,
        chemical_symbol,
        atomic_number,
        mass_number,
        electron_configuration,
    ):
        self.name = name
        self.chemical_symbol = chemical_symbol
        self.atomic_number = atomic_number
        self.mass_number = mass_number
        self.electron_configuration = electron_configuration

#region periodic_table

hydrogen    = Atom("Hydrogen",   "H",     1,  1.0078,                        "1s¹")
helium      = Atom("Helium",     "He",    2,  4.0026,                        "1s²")
lithium     = Atom("Lithium",    "Li",    3,  6.9410,                     "1s²2s¹")
beryllium   = Atom("Beryllium",  "Be",    4,  9.0122,                     "1s²2s²")
boron       = Atom("Boron",      "B",     5,  10.811,                  "1s²2s²2p¹")
carbon      = Atom("Carbon",     "C",     6,  12.011,                  "1s²2s²2p²")
nitrogen    = Atom("Nitrogen",   "N",     7,  14.007,                  "1s²2s²2p³")
oxygen      = Atom("Oxygen",     "O",     8,  15.999,                  "1s²2s²2p⁴")
fluorine    = Atom("Fluorine",   "F",     9,  18.998,                  "1s²2s²2p⁵")
neon        = Atom("Neon",       "N",    10,  20.180,                  "1s²2s²2p⁶")
sodium      = Atom("Sodium",     "Na",   11,  22.990,               "1s²2s²2p⁶3s¹")
magnesium   = Atom("Magnesium",  "Mg",   12,  24.305,               "1s²2s²2p⁶3s²")
aluminium   = Atom("Aluminium",  "Al",   13,  26.982,            "1s²2s²2p⁶3s²3p¹")
silicon     = Atom("Silicon",    "Si",   14,  28.086,            "1s²2s²2p⁶3s²3p²")
phosphurus  = Atom("Phosphurus", "P",    15,  30.974,            "1s²2s²2p⁶3s²3p³")
sulphur     = Atom("Sulphur",    "S",    16,  32.065,            "1s²2s²2p⁶3s²3p⁴")
chlorine    = Atom("Chlorine",   "Cl",   17,  35.453,            "1s²2s²2p⁶3s²3p⁵")
argon       = Atom("Argon",      "Ar",   18,  39.948,            "1s²2s²2p⁶3s²3p⁶")
potassium   = Atom("Potassium",  "K",    19,  39.098,         "1s²2s²2p⁶3s²3p⁶4s¹")
calcium     = Atom("Calcium",    "Ca",   20,  40.078,         "1s²2s²2p⁶3s²3p⁶4s²")
scandium    = Atom("Scandium",   "Sc",   21,  44.956,      "1s²2s²2p⁶3s²3p⁶3d¹4s²")
titanium    = Atom("Titanium",   "Ti",   22,  47.867,      "1s²2s²2p⁶3s²3p⁶3d²4s²")
vanadium    = Atom("Vanadium",   "V",    23,  50.942,      "1s²2s²2p⁶3s²3p⁶3d³4s²")
chromium    = Atom("Chromium",   "Cr",   24,  51.996,      "1s²2s²2p⁶3s²3p⁶3d⁵4s¹")
manganese   = Atom("Manganese",  "Mn",   25,  54.938,      "1s²2s²2p⁶3s²3p⁶3d⁵4s²")
iron        = Atom("Iron",       "Fe",   26,  55.845,      "1s²2s²2p⁶3s²3p⁶3d⁶4s²")
cobalt      = Atom("Cobalt",     "Co",   27,  58.933,      "1s²2s²2p⁶3s²3p⁶3d⁷4s²")
nickel      = Atom("Nickel",     "Ni",   28,  58.693,      "1s²2s²2p⁶3s²3p⁶3d⁸4s²")
copper      = Atom("Copper",     "Cu",   29,  63.546,     "1s²2s²2p⁶3s²3p⁶3d¹⁰4s¹")
zinc        = Atom("Zinc",       "Zn",   30,  65.380,     "1s²2s²2p⁶3s²3p⁶3d¹⁰4s²")

#endregion

periodic_table_list = [
    hydrogen,                                                                                                                                                        helium, 
    lithium,   beryllium,                                                                                         boron,     carbon,  nitrogen,   oxygen,  fluorine, neon,
    sodium,    magnesium,                                                                                         aluminium, silicon, phosphurus, sulphur, chlorine, argon,
    potassium, calcium,   scandium, titanium, vanadium, chromium, manganese, iron, cobalt, nickel, copper, zinc,
]