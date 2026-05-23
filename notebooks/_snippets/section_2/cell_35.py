"""Section 2, cell 35 — extracted from Functional_Introduction_To_Python_Section_2(Functions).ipynb."""

iris["rounded_sepal_length"] = iris[["sepal_length"]].apply(pd.Series.round)
iris.head()
