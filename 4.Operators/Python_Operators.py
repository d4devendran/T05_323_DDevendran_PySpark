Operators:
	
--> Python Operators in general are used to perform operations on values and variables.
--> OPERATORS: Are the special symbols. Eg- + , * , /, etc.
--> OPERAND: It is the value on which the operator is applied.

Types of operators:
1. Arithmatic operators
Operator			Name				Example				Result
											      if x=5 , y=10
+					Addition		x+y				10
-					Subtraction		x-y				-5
*					Multiplication		x*y				50
/					Division		x/y				0.5
%					Modulus			x%y				5
**					Exponentiation		x**y				9765625
//					Floor division		x//y				0

2. Assignment operatiors
Operator			   Example				     Same As

=				    x=5						x=5
+=				    x+=3					x=x+3
-=				    x-=3					x=x-3
*=				    x*=3					x=x*3
/=				    x/=3					x=x/3
%=				    x%=3					x=x%3
//=				    x//=3					x=x//3
**=				    x**=3					x=x**3
&=				    x&=3					x=x&3
|=				    x|=3					x=x|3
^=				    x^=3					x=x^3
>>==				    x>>=3					x=x>>3
<<==				    x<<=3					x=x<<3

3. Comparison operators
Operator			        Name				Example

==					Equal				x==y
!=					Not Equal			x!=y
>					Greater than			x>y
<					Less than			x<y
>=					Greater than			x>=y
					or equal to
<=					Less than or 			x<=y
					equal to

4. Logical operators
Operator			        Description					    Example

and					Returns True if both			  	x<5 and x<10
					Statements are True

or					Returns True if any				x<5 or x<10
					of statements is True

not					Reverse the result				not(x<5 and x<10)
					returns False if the
					result is true

5. Membership operators
Operator				Description							Example

in					Returns True if a sequence					x in y
					with specified value is present
					in the object

not in					Returns True if a sequence					x not in y
					with the specified value is not
					present in the object

6. Identity operators
Operator				Name								Example

is					Returns True if both						x is y
					variables are same object

is not					Returns True if both						x is not y
					variables are not the same object

7. Bitwise operators
Bitwise operators used to compare binary numbers

Operator				Name			Description

&					AND			Sets each bit into 1 if both bits are 1
|					OR			Sets each bit to 1 if one of two bits is 1
^					XOR			Sets each bit 1 if only one of two bits is 1
~					NOT			Inverts all the bits
