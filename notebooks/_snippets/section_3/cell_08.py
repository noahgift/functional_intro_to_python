"""Section 3, cell 8 — extracted from Functional_Introduction_To_Python_Section_3(Control_Structures).ipynb."""


def lazy_return_random_attacks():
    """Yield attacks each time"""
    import random

    attacks = {
        "kimura": "upper_body",
        "straight_ankle_lock": "lower_body",
        "arm_triangle": "upper_body",
        "keylock": "upper_body",
        "knee_bar": "lower_body",
    }
    while True:
        random_attack = random.choices(list(attacks.keys()))
        yield random_attack


# Make all attacks appear as Upper Case
upper_case_attacks = (attack.pop().upper() for attack in lazy_return_random_attacks())
