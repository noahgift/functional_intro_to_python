"""Section 2, cell 13 — extracted from Functional_Introduction_To_Python_Section_2(Functions).ipynb."""


def attack_techniques(**kwargs):
    """This accepts any number of keyword arguments"""

    for name, attack in kwargs.items():
        print(f"This is attack I would like to practice: {attack}")
