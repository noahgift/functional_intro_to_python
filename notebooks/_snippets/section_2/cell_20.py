"""Section 2, cell 20 — extracted from Functional_Introduction_To_Python_Section_2(Functions).ipynb."""


def multiple_attacks(attack_location_function):
    """Takes a function that categorizes attacks and returns location"""

    new_attacks_list = ["rear_naked_choke", "americana", "kimura"]
    for attack in new_attacks_list:
        attack_location = attack_location_function(attack)
        print(f"The location of attack {attack} is {attack_location}")
