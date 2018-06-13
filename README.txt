directory structure is:

python-trials
	foo
	bar
		barchild

* For a script running in python-trials the children directories are visible, if they are made into python packages with the __init__.py files

* For run scripts in foo to be able to SEE packages in bar, add the following lines to the top of the run scripts:

#! /anaconda2/bin/python
import sys
sys.path.insert(0, '/home/akshaya/technical/tinkerbox/python-trials/')

* The "shebang line" is used to indicate interpreter for UNIX systems to consider the right interpreter if the python file is made into an executable and executed directly.

chmod +x RunFile.py
./RunFile.py

* For some odd reason importing a RunScript from any package also runs that RunScript. So only import class files or package files.

TODO

* What Lars wrote in his code with exception catching
* Check if RunScript in barchild can use package files in foo, bar, python-trials
* The use of main() function in python