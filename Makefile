setup:
	#You may want to create an alias to automatically source this:
	# alias functop="cd ~/src/functional_intro_to_python && source ~/.func/bin/activate"
	python3 -m venv ~/.func

install:
	pip install -r requirements.txt

test:
	#PYTHONPATH=. && pytest -vv --cov=paws --cov=spot-price-ml tests/*.py
	PYTHONPATH=. && py.test --nbval-lax notebooks/*.ipynb

lint:
	pylint --disable=R,C funclib

run-part-1:
	jupyter nbconvert notebooks/Functional_Introduction_To_Python_Section_1\(Introductory_Concepts\).ipynb --to slides --post serve

run-part-2:
	jupyter nbconvert notebooks/Functional_Introduction_To_Python_Section_2\(Functions\).ipynb --to slides --post serve

run-part-3:
	jupyter nbconvert notebooks/Functional_Introduction_To_Python_Section_3\(Control_Structures\).ipynb --to slides --post serve

run-part-4:
	jupyter nbconvert notebooks/Functional_Introduction_To_Python_Section_4\(Intermediate_Topics\).ipynb --to slides --post serve

run-part-5:
	jupyter nbconvert notebooks/IO\ Python.ipynb --to slides --post serve

all: install lint test
