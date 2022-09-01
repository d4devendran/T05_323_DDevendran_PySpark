1.VARIABLE SCOPES OF LEGB RULE

  --> The LEGB rule names the possible scopes of a variable in Python: Local, Enclosing, Global, Built-in.
      Python searches namespaces in this order to determine the value of an object given its name.
      Scopes are created with functions, classes, and modules.
      Local    : The variables assigned inside a function in python program.
      Enclosed : The variables assigned inside inside a fuction(inner class).
      Global   : The variables assigned outside a function in python program.
      Builtin  : If there is no local,enclosed,global varbales then python will search for Builtin variables.

2.MEMORY ALLOCATION OF VARIABLES

   --> Memory allocation can be defined as allocating a block of space in the computermemory to a program.
       in python memory allocation and deallocation method is automatic as the python developers created a garbage
       collection for python so that the user does not have to do manual garbage collection

3.SWAP 2 VARIABLES WITHOUT USING THIRD VARIABLE
    x = 5
    y = 7
    print ("Before swapping: ")
    print("Value of x : ", x, " and y : ", y)
    x, y = y, x
    print ("After swapping: ")
    print("Value of x : ", x, " and y : ", y)

   Output:
    ===============
   Before swapping:
   Value of x :  5  and y :  7
   After swapping:
   Value of x :  7  and y :  5

4.LOCAL VS GLOBAL VARIABLES .EXPLAIN IN DETAIL?

  --> Variables are classified into Global variables and Local variables based on their scope.
      The main difference between Global and local variables is that global variables can be accessed globally in the entire program,
      whereas local variables can be accessed only within the function or block in which they are defined.