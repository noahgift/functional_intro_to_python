"""Section 2, cell 22 — extracted from Functional_Introduction_To_Python_Section_2(Functions).ipynb."""


def attack_counter():
    """Counts number of attacks on part of body"""
    lower_body_counter = 0
    upper_body_counter = 0

    def attack_filter(attack):
        nonlocal lower_body_counter
        nonlocal upper_body_counter
        attacks = {
            "kimura": "upper_body",
            "straight_ankle_lock": "lower_body",
            "arm_triangle": "upper_body",
            "keylock": "upper_body",
            "knee_bar": "lower_body",
        }
        if attack in attacks:
            if attacks[attack] == "upper_body":
                upper_body_counter += 1
            if attacks[attack] == "lower_body":
                lower_body_counter += 1
        print(f"Upper Body Attacks {upper_body_counter}, Lower Body Attacks {lower_body_counter}")

    return attack_filter
