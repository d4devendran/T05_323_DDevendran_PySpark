Types of loops in python are
    1.While
    2.for
    3.nested

1.While:
 While loops are known as indefinite conditional loops.They keep on iterating until certain condition are met.
 There is no guarantee ahead of time regarding how many times the loop will iterate.

Syntax:
	while expression:
		statements

Ex:
	count=0
	while(count<9)
		print(“The count is:”,count)
	print(“Good bye!)

2.For:
for loop is python loop which repeats a group of statements a specified number of times.

Syntax:
	for <variable > in sequence:
			statement1
				statement2
					|
					|
				statement 3

3.Nested loop:
Python programming allows use of loop inside another loop
This is called Nested loop.

Syntax:							Syntax:

for iterating_var in sequence:				while expression:
	for iterating_var in sequence:				while expression:
		<statements>						<statements>
<statements>						<statements>
