"""Section 2, cell 27 — extracted from Functional_Introduction_To_Python_Section_2(Functions).ipynb."""


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
