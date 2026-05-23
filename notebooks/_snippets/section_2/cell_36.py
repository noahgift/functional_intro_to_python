"""Section 2, cell 36 — extracted from Functional_Introduction_To_Python_Section_2(Functions).ipynb."""


def multiply_by_100(x):
    """Multiplies by 100"""
    return x * 100


iris["100x_sepal_length"] = iris[["sepal_length"]].apply(multiply_by_100)
iris.head()
