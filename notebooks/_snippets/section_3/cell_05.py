"""Section 3, cell 5 — extracted from Functional_Introduction_To_Python_Section_3(Control_Structures).ipynb."""


def recommended_attack(position):
    """Recommends an attack based on the position"""
    if position == "full_guard":
        print(f"Try an armbar attack")
    elif position == "half_guard":
        print(f"Try a kimura attack")
    elif position == "full_mount":
        print(f"Try an arm triangle")
    else:
        print(f"You're on your own, there is no suggestion for an attack")
