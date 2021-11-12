#include <iostream>
#include "vector.h"
#include <chrono>
#include <stdlib.h>

#define STRINGYFY(x) #x

using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;

float testDimensionsFromTo(float (*angleCalculator)(f_vector, f_vector), size_t end = 100, size_t step = 10, size_t iterations_per_dimensions = 200000){
	srand(time(NULL));
	size_t start = 2;
	float sum = 0;
	for(size_t i = start; i < end; i += step){
		double average = 0;
		for(size_t j = 0; j < iterations_per_dimensions; j++){
			f_vector v1 = generateRandomVector(i);
			f_vector v2 = generateRandomVector(i);
			auto t1 = high_resolution_clock::now(); // I expect this to be a non factor
			sum += angleCalculator(v1,v2);
			__asm__ __volatile__ ("" : : : "memory"); // This should prevent the optimizer from optimizing
			auto t2 = high_resolution_clock::now();
			duration<double, std::milli> dur = t2 - t1;
			average += dur.count();
			delete v1.e;
			delete v2.e;
		}
		std::cout  << "," << i << "," << average << "," << average/iterations_per_dimensions << std::endl;
	}
	return sum;
}

int main(void){
	//Run the program with only default arguments
	std::cout << "Running " << STRINGYFY(angleBetweenNonNomalized) << std::endl;
	testDimensionsFromTo(angleBetweenNonNormalized, 100, 5);
	std::cout << "Running " << STRINGYFY(angleBetweenNormalized) << std::endl;
	testDimensionsFromTo(angleBetweenNormalized, 100, 5);
	std::cout << "Running " << STRINGYFY(projection) << std::endl;
	testDimensionsFromTo(projection, 100, 5);
	//Add more Test here



	//
	return 0;
}
