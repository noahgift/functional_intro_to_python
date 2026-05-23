"""Section 4, cell 11 — extracted from Functional_Introduction_To_Python_Section_4(Intermediate_Topics).ipynb."""


class UFC:
    def weight_class(self, weight):
        """Weight Class Finder"""

        classes = {155: "Lightweight", 170: "Welterweight"}
        return classes[weight]
