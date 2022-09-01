PYTHON INTRODUCTION

1. PYTHON FEATURES:

     1.High level programming language
        Programming languages are of two types: low level and high level
        A low level language uses machine code instructions, these instructions directly interact with the CPU.
        High  level languages use English words to develop programs,These are easy to learn and use like COBOl,PHP or JAVA
        Python also uses English words in its programs and hence it is called high level programming language.

     2.Dynamically typed
        We don't have to declare the type of variable while assigning a value to a variable in Python.
        Other languages like C, C++, Java, etc.., there is a strict declaration of variables before assigning values to them.
        It states the kind of variable in the runtime of the program. So, Python is a dynamically typed language

     3.Platform independent
        When a python program is compiled using a python compiler, it generates a byte code. Python's byte code represents a
        fixed set of instructions that run on all operating systems and hardware. Using a PVM anybody can run these byte code
        instructions on any operating systems like UNIX, Linux,Windows etc.

     4.Portable
        When program yields the same result on any compueter in the world, the it is called a portable program.

     5.Procedure oriented and Object Oriented
       Python is a procedure oriented as well as object oriented programming language,
       In procedure oriented programming languages, the programs are built using fuctions and procedures e.g C,PASCAL
       In object oriented programming languages, the programs uses classes and objects e.g C++,JAVA

     6.Interpreted
       A program code is called source code, Python compiler translates the python program into intermediate code called byte
       code. This byte code is then executed by PVM. Inside the PVM, an interpreter converts the byte code intsructions into
       machine code so that the processor will understand and run that machine code to produce results.

2. ADVANTAGES AND DISADVANTAGES of python

   Advantages of python:
		 1.It is easy to learn and use,Open source and it has an extensive library.
		 2.Python increases productivity.
		 3.It is very flexible.
		 4.It has a very supportive community.

   Disadvantages of python
		 1.Because of its elementary programming, users face difficulty while working with other programming languages.
		 2.Python is a time-consuming language. It has a low execution speed.
		 3.There are many issues with the design of  the language, which only gets displayed during runtime.
		 4.It is not suited for memory-intensive programs and mobile applications


3. COMPILE TIME VS RUN TIME:

Compile time:
--> The source code for a program written in a programming language is typically compiled into executable code

Run time:
--> The executable code typically requires a “runtime” component to support the execution of the code.
--> There are some programming languages that do not need to be compiled into executable code; they are interpreted at runtime or execution time.

4. WHY PYTHON IS CALLED INTERPRETED PROGRAMMING LANGUAGE:

--> Python language is an interpreted language. Python programs are executed directly from the source code.
--> Compiler converts the program source code into bytecode
--> The role of Python Virtual Machine is to convert the byte code instructions into machine code
--> The interpreter converts the byte code into machine code and sends machine code to the computer processor for execution.
--> since interpreter is playing the main role, often Python Virtual Machine is also called an interpreter

5. TOKENS IN PYTHON:

The smallest unit part in a python program we call it Token.
Tokens are like
1.Identifiers
2.Operators
3.Literals
4.Keywords
5.Constants

6.MEMORY MANAGEMENT IN PYTHON:

--> Memory manager inside the PVM allocates memory required for objects created in a Python program.
--> All these objects are stored on separate memory called heap.
--> Heap is the memory which allocated during runtime.
--> The size of the heap memory depends on the Random Access Memory of our computer and it can increase or decrease its size depending on the requirement of the program.

7.GARBAGE COLLECTION HOW IT WORKS
--> Garbage collector is a module in Python that is useful to delete objects from memory which are not used in the program
--> Garbage collector can detect reference cycles. When an object is found with a reference count 0 , garbage collector understands that the object is not used by the program.
--> Garbage collector tries to delete the objects which are not referenced in the program
--> get_threshold()---To know how many times garbage collector removed
--> collect()---To run Garbage collector manually

8. .PY VS .PYC FILE

--> .py files contain the source code of a program. Whereas, .pyc file contains the bytecode of your program.
--> We get bytecode after the compilation of the .py file (source code). .pyc files are not created for all the files that you run. It is only created for the files that you import.
--> Before executing a python program python interpreter checks for the compiled files. If the file is present, the virtual machine executes it. If not found, it checks for the .py file. If found, compile it to a .pyc file and then the python virtual machine executes it.
    Having a .pyc file saves you the compilation time.

9.HOW PYTHON PROGRAM EXECUTES INTERNALLY

   Step 1:  The python compiler reads a python source code or instruction. Then it verifies that the instruction is well-formatted,
             i.e. it checks the syntax of each line. If it encounters an error, it immediately halts the translation and
             shows an error message.

   Step 2: If there is no error, i.e. if the python instruction or source code is well-formatted then the
           compiler translates it into its equivalent form in an intermediate language called “Byte code”.

   Step 3: Byte code is then sent to the Python Virtual Machine(PVM) which is the python interpreter.
            PVM converts the python byte code into machine-executable code.
            If an error occurs during this interpretation then the conversion is halted with an error message

10.PYTHON IS DYNAMICALLY PROGRAMMING LANGUAGE.WHY?

Programming languages are divided into 2 types.
--> They are Static and Dynamic programming languages.
--> The memory or the storage space that will be created during compile-time of a program is called Static programming and the memory created during runtime is called Dynamic programming.

--> We don't have to declare the type of variable while assigning a value to a variable in Python.
    Other languages like C, C++, Java, etc.., there is a strict declaration of variables before assigning values to them.
    It states the kind of variable in the runtime of the program. So, Python is a dynamically typed language

