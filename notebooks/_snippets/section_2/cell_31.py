"""Section 2, cell 31 — extracted from Functional_Introduction_To_Python_Section_2(Functions).ipynb."""


def randomized_speed_attack_decorator(function):
    """Randomizes the speed of attacks"""

    import time
    import random

    def wrapper_func(*args, **kwargs):
        sleep_time = random.randint(0, 3)
        print(f"Attacking after {sleep_time} seconds")
        time.sleep(sleep_time)
        return function(*args, **kwargs)

    return wrapper_func
