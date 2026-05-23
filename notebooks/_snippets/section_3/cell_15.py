"""Section 3, cell 15 — extracted from Functional_Introduction_To_Python_Section_3(Control_Structures).ipynb."""

tournaments = ["NAGA", "IBJJF", "EBI"]
while True:
    try:
        tournament = tournaments.pop()
        print(f"I would like to compete in the {tournament} tournament.")
    except IndexError:
        print("There are no more tournaments")
        break
