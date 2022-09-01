PYTHON INTRODUCTION 

1.What is python?
--> Python is interpreted, High level , Object oriented programming language.
--> Python is a programming language that combines the features of  C and Java

2.Features of python?
--> Simple
--> Easy to learn
--> Open source
--> High level language
--> Dynamically typed
--> Platform independent
--> Portable
--> Procedure and Object oriented language

3.PVM
--> Compiler converts the program source code into bytecode
--> The role of Python Virtual Machine is to convert the byte code instructions into machine code
--> The interpreter converts the byte code into machine code and sends machine code to the computer processor for execution.
--> since interpreter is playing the main role, often Python Virtual Machine is also called an interpreter

4.Memory Management in python
--> Memory manager inside the PVM allocates memory required for objects created in a Python program.
--> All these objects are stored on separate memory called heap.
--> Heap is the memory which allocated during runtime.
--> The size of the heap memory depends on the Random Access Memory of our computer and it can increase or decrease its size depending on the requirement of the program.

5.Garbage collection in python
--> Garbage collector is a module in Python that is useful to delete objects from memory which are not used in the program
--> Garbage collector can detect reference cycles. When an object is found with a reference count 0 , garbage collector understands that the object is not used by the program.
--> Garbage collector tries to delete the objects which are not referenced in the program
--> get_threshold()---To know how many times garbage collector removed
--> collect()---To run Garbage collector manually

6.Comparisons between Java and Python

			JAVA 									PYTHON

1.Java is object oriented programming	      	 1.Python is interpreted, High level,object oriented programming language.
2.it is compulsory to declare the datatypes	 2.Type declaration is not required in Python
  of variables,arrays etc in Java				   
3.Memory allocation done by JVM			 3.Memory allocation done by PVM
4.Java has for , do…while , while loops 	 4.Python has while and for loops
  and switch statement				   it does not have switch statement.
5.Java supports both single and multi-		 5.python supports only single dimensional array for multi we need to import numpy
  dimensional arrays						    										    
6. Java collection objects like			 6.python collection objects like lists and
   Stack, LinkedList or Vector store only          dictionaries can store any type of objects
   objects

7.IDE & IDLE
--> IDLE Integrated Development Environment

8.Comments in python
--> Single line comments:
--> These comments starts with a hash symbol(#)
Ex:
	a=10
--> Multi line comments:
--> These comments starts with tripe quotes(“””)
Ex:
	“””------”””
