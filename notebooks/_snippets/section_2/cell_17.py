"""Section 2, cell 17 — extracted from Functional_Introduction_To_Python_Section_2(Functions).ipynb."""


def attack_location(technique):
    """Return the location of an attack"""

    attacks = {
        "kimura": "arm_attack",
        "straight_ankle_lock": "leg_attack",
        "arm_triangle": "neck_attach",
    }
    if technique in attacks:
        return attacks[technique]
    return "Unknown"
