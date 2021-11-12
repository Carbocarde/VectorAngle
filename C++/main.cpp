#include <iostream>
#include "vector.h"
#include <chrono>

using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::milliseconds;

int main(){
	constexpr size_t iterations = 200000;
	auto t0 = high_resolution_clock::now();
	std::cout <<  "Dimensions, Total Time, Average Time" << std::endl;
	for(size_t i = 2; i <200; i += 2){
		double average = 0;
		for(size_t j = 0; j < iterations; j++){ 
			f_vector v1 = generateRandomVector(i); // 1/4 kB
			f_vector v2 = generateRandomVector(i); // 1/4 kB
			auto t1 = high_resolution_clock::now(); // I expect this to be a non factor
			float angle = angleBetween(v1,v2);
			__asm__ __volatile__ ("" : : : "memory"); // Evil Vodoo magic
			auto t2 = high_resolution_clock::now();
			duration<double, std::milli> dur = t2 - t1;
			average += dur.count();
			delete v1.e;
			delete v2.e;
		}
		////average /= iterations;
		std::cout << i << "," << average << "," << average/iterations << std::endl;
	}

	duration<double, std::milli> total = high_resolution_clock::now() - t0;
	std::cout << "Total time: " << total.count() << std::endl;


}
