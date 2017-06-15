Notes for Python Class


Operations
Sum: i+j
Difference: i-j
Product: i*j
Division: i/j
Division w/o Remainder: i//j
Divsion only remainer: i%j
Raise to a power: i to the power j

Equality Tests
	i == j
	i != j


Variables (AKA Bindings)
	* Assign a variable: x='value'

KeyWords
	* These cannot be used as an assignment
	* Specific to programming language

Types
	*int
	*float
	*bool
	*string


Operations on Strings
	1) 3*'eric'
	2) len('eric')
		- counts spaces
	3) 'eric'[1]
		- gives element at position 1
	4) 'eric'[1:]


Input / Output: print()
	- Used to output to the console

input() 
- expects everything to be a string
- User types something and hits enter


Integrated Development Environment (IDE)
	- 
	-  


while() Loops
	- Control flow
	- Format: while <condition>:
	- Condition evaluates to a boolean
	- IF Condition is true, do all the steps inside the code block
	- Unbounded number of iterations
	- Can end early via a break
	- Can use a counter, but must initialize

for <variable> in range(<some_num>)
	- first time, <variable> starts at the smalled value
	- next time, <variable> gets the prev value +1
	- range(<initial>, <final>, <increment>)
	- For Loops can be rewriten as a while loop
	- Uses a counter
	- Know number of iterations

break statement
	- Immediately exists whatever loop it is in
	- skyps remaining expressions in code block
	- exits only innermost loop


Reviewing Strings
	- Think of strings as a sequence of characters
	- Can compare strings using:
		- ==, <,>
	- len() is a function 
	- Can use square brackets to find a value at position x in a string
	- "string"[1:3]

Slicing strings
	- Can slice strings using [start:stop:step]
	- if step is -x, it's accessed in reverse order'
	- Strings are "immutable"
		- They cannot be modified


For Loops
	- loop variable that iterates over a set of values
	- epressions inside loop exectuted with value 


Approximate Solutions
	- Start with exhaustive enumeration
	- Find a solutiont that is "close enough"
	- Start with a guess and increment by some small value
	- The Tradeoff
		- Decreasing epsilon size: slower program
		- Increasing epsilon size: less accurate answer


Bisection Search
	- SQRT of a positive integer, x, lies between 1 and x
 	- Choose a middle value, if it is too big then go for the smaller half
	- 


Floats & Fractions
	- Internally, computers represent numbers in binary
	- If there is no integer p such that x*(2**p) is a whole number, then the internal representation is an approximation
	- Testing equality of floats is not exact 
		- Use abs(x-y) < small number rather than x == y
	- 

Netwon - Raphson:
	- General approximation algorithm to find roots of a polynomial in one variable
	- p(x) = AxX^n + a(n-1)x^(n-1_) + ... + a1x + a0
	- find r such that p(r) = 0


Functions
	- Write re-usable chunks of code: Functions
	- Function charcteristics:
		- Has a name
		- Has parameters
		- Has a docstring: documentation that explains what the function does
		- Had a body: commands or instructions that define the function

How to Write a function:
	def is_even (i)
		""" docstring text"""
		print("is even")
		return i%2 == 0

Calling Functions
	- Formal parameter gets bound to the value of an actual parameter when a function is called
	- New scope/frame/environment ceated when enter a function
	- Scope is mapping of name to objects
	- if there is no return statement --> a "none" is returned

return
	- only has meaning inside a function
	- only one return executed inside a function 	
	- code inside a function but after return statement not executed
	- has a value associated with it

print
	- print can be used outside Functions
	- can execute manyb print statements inside a function
	- code inside function can be executed after a print statement
	- has a value associated with it, outputted to the console


Functions & Scope
	- inside a function, can access a variable defined outside
	- inside a function, cannot modify a variable defined outside


Default Values in Functions
	- You can give default values to Functions
	- Example:
		def printName(firstName, lastName, reverse=False)
 
 Specifications
 	- A contract between implementor of a function and the clients who use it
 		- Assumptions: conditions that must be met by clients
 		- Guarantees: conditions that must be met by a function
  		


























