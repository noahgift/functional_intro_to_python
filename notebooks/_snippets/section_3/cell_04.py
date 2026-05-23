"""Section 3, cell 4 — extracted from Functional_Introduction_To_Python_Section_3(Control_Structures).ipynb."""


def attacks():
    list_of_attacks = ["lower_body", "lower_body", "upper_body"]
    print(f"There are a total of {len(list_of_attacks)} attacks coming!")
    for attack in list_of_attacks:
        yield attack


attack = attacks()
count = 0
while next(attack) == "lower_body":
    count += 1
    print(f"crossing legs to prevent attack #{count}")
else:
    count += 1
    print(f"This is not a lower body attack, I will cross my arms for #{count}")
