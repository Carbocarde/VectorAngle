#include <iostream>
#include "vector.h"
#include <chrono>
#include <stdlib.h>

#define STRINGYFY(x) #x

using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;

void static escape(void *p) // Mr. Carruth is asking you to use this function only for good ;D
{
	asm volatile("" : : "g"(p): "memory");
}

/*
Act as a compiler fence to ensure that the optimizer does not optimize instructions before or after this instruction.
This prevents instruction scrambling that could cause the end time to be recorded before the calculation function is
actually complete.
*/
void static clobber()
{
	asm volatile("" : : : "memory");
}

void testDimensionsFromTo(
		float (*angleCalculator)(f_vector, f_vector)
		, size_t end = 100
		, size_t step = 10
		, size_t iterations_per_dimensions = 200000
	)
{
	srand(time(NULL));
	size_t start = 2;
	for(size_t i = start; i < end; i += step){
		double average = 0;
		for(size_t j = 0; j < iterations_per_dimensions; j++){
			f_vector v1 = generateRandomVector(i);
			f_vector v2 = generateRandomVector(i);
			auto t1 = high_resolution_clock::now(); // I expect this to be a non factor
			float f = angleCalculator(v1,v2);
			escape(&f);
			auto t2 = high_resolution_clock::now();
			duration<double, std::milli> dur = t2 - t1;
			average += dur.count();
			delete v1.e;
			delete v2.e;
		}
		std::cout  << i << "," << average << "," << average/iterations_per_dimensions << std::endl;
	}
}

void testDimensionsFromToPreGeneratedVectors(
		float (*angleCalculator)(f_vector, f_vector)
		, size_t end = 100
		, size_t step = 10
		, size_t iterations_per_dimensions = 200000
	)
{
	srand(NULL);
	size_t start = 2;
	for(int i = start; i < end; i+= step)
	{
		//Generate vectors in a giant array
		f_vector * arrayOfVectors = (f_vector *)malloc(sizeof(f_vector) * iterations_per_dimensions * 2);
		for(int j = 0; j < iterations_per_dimensions; j += 2)
		{
			generateRandomVector(&arrayOfVectors[j], i);
			generateRandomVector(&arrayOfVectors[j+1], i);
		}
		// Calculate all vectors
		auto t1 = high_resolution_clock::now();
		for(int j = 0; j < iterations_per_dimensions; j += 2)
		{
			float f = 0;
			escape(&f);
			f = angleCalculator(arrayOfVectors[j], arrayOfVectors[j + 1]);
			clobber();

		}
		duration<double, std::milli> dur = high_resolution_clock::now() - t1;
		free(arrayOfVectors);
		std::cout << i << ","
		          << dur.count() << ","
			      << dur.count()/iterations_per_dimensions << std::endl;
	}
}

// This is a macro for easier benchmarking
#define RUN_TEST(function, parameters)					\
	std::cout << "Running " << STRINGYFY(function) << ",," << std::endl; 	\
	function parameters;

int main(void){
	RUN_TEST(testDimensionsFromTo, (angleBetweenNonNormalized,100,5,200000))
	RUN_TEST(testDimensionsFromToPreGeneratedVectors, (angleBetweenNonNormalized, 100, 5, 200000))

	return 0;
}
