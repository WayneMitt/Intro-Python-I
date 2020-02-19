"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
from pathlib import Path

file_to_open = Path(r'c:/Users/wayne/Documents/LambdaProjects/Sprint 11 - Intro to Python and OOP/Intro-Python-I/src/foo.txt')

foo = open(file_to_open)

print(foo.read())
foo.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

bar = open("bar.txt", "w")
bar.write(" Here's a line \n And another \n and a third")
bar.close()

file_to_open = Path(r'c:/Users/wayne/Documents/LambdaProjects/Sprint 11 - Intro to Python and OOP/Intro-Python-I/bar.txt')

bar2 = open(file_to_open)
print(bar2.read())