"""Section 3, cell 10 — extracted from Functional_Introduction_To_Python_Section_3(Control_Structures).ipynb."""

## Generator Pipeline:  One expression chains into the next
# Make all attacks appear as Upper Case
upper_case_attacks = (attack.pop().upper() for attack in lazy_return_random_attacks())
# Remove the underscore
remove_underscore = (attack.split("_") for attack in upper_case_attacks)
# Create a new phrase
new_attack_phrase = (" ".join(phrase) for phrase in remove_underscore)
