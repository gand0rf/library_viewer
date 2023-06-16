# library_viewer

An interesting little idea I had based on a poster that came with my visual stuido .net bundle from 2002.
It was a really neat breakdown of teh standar libraries in .Net and there modules.
I thought I would try and make soemthing like that for python.

---Usage---
run: python main.py

It will then print out a list of the standard library along with installed libraies.
Enter the number of the package you want to look at.
It will then print the name of the package and run the dir() on it.
This will print a list of moduels that you would normally be able to call and use.

-----------

If you try this and see packages not listed, or it comes back and gives an error when trying to list the modules,
please in an issue and I will try and help. Sometimes it can be like the library beautifulsoup4 that gets imported in as bs4.
Hence the need for the Package_Checker.py class. In the cass of this example, it would return 'bs4' so that the right text
is added to package.py
