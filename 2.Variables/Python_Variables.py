1.Variables

--> Variables are stored values i.e we are using for storing the reference of data
    Ex: x=10, x=10+20
   ‘x’ is variable name and 10, 10+20 is its value
--> Here value 10 will converts into binary form and then  stored in memory heap space.
    ‘x’ will not store the data but its will store reference of the memory location
--> While we are calling print(x) ,
   ‘x’ 🡪 will call reference the memory address of value
	The value presented in the memory address will converted into
	binary to numerical then it show as result.

2.LEGB Rule:

--> The LEGB rule names the possible scopes of a variable in Python: Local, Enclosing, Global, Built-in.
    Python searches namespaces in this order to determine the value of an object given its name.
--> Scopes are created with functions, classes, and modules.
    Local    : The variables assigned inside a function in python program.
    Enclosed : The variables assigned inside inside a fuction(inner class).
    Global   : The variables assigned outside a function in python program.
    Builtin  : If there is no local,enclosed,global varbales then python will search for Builtin variables.

3.Tokens

Token is the smallest unit inside the program

There are following tokens in python:
A. Identifiers
B. Operators
C. Literals
D. Keywords
E. Constants

A.Identifiers :
	Name of the variables Ex: x=10
    Here ‘ x’ is an identifier

B. Operators:
	These are mathematical expressions like +, -,*,/,%, etc
    Ex: x=10
    Here ‘=‘ is an operator for assigning value
C. Literals:
	Literals are nothing but values that are assigned to variables.
    Ex: x=10
    Here value 10  is a literal

D. Keywords:
	Keywords are predefined words in python like Alpha, Beta & Gamma in maths.
    Ex: for , if , class , while etc

E. Constants:
	These are the values that we can’t change.
    Ex: x=10
	Here 10 is constant , the value of 10 we can’t change.

