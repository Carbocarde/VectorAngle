# This is not meant to demonstrate "C++ better than Python"


# How to build and run
`clang` or `gcc`
## Build
`clang++ main.cpp -Wall -Wextra`
## Run
`./a > result.csv`


# Plotting the output
The program outputs all the results from the tests in a CSV File, where the first column is always only the name of the function that was called.


# What does the program do?

The function `generateRandomVector` takes in a dimension and gives back a vector (structure) of a pointer to a float array and the size of that array(aka the dimension of the vector)

both attributes are public so no getters or setters, just access them with the "." operator

The function `testDimensionsFromTo` takes in
- function 	(What function should be tested)
- end 		(Whats the maximal dimension + 1)
- step		(How many dimensions should it increase by from test to test)
- iterations_per_dimensions (How many iterations should it do per dimension-step)

## How do I add a new function to test to the program

In the main function:
type the macro `RUN_TEST(X,Y)`, where:
	X is the methodology to test with
		- `testDimensionsFromTo`
		- `testDimensionsFromToPreGeneratedVectors`
	Y is the arguments for the function X in the format `(functionToTest, maximumDimensions, step Size between dimensions, iterations per dimension)`
		The braces are `()` are important as the argument Y gets concatonated as is onto the functioncall X


