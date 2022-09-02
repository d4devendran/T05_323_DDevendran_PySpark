Control Statements:
1.Break
2.Continue
3.Pass

1.Break
With the break statement we can stop the loop before it has looped through all the items.

Ex:
Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

2.Continue
With the continue statement we can stop the current iteration of the loop, and continue with the next:

Ex:
it do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

3.Pass
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

Example
for x in [0, 1, 2]:
  pass
