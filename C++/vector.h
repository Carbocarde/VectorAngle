#ifndef Vector
#define Vector

#include <cstdlib>
#include <math.h>
#include <cassert>
#include <stdlib.h>
#include <time.h>

struct f_vector{
	float *e;
	size_t dimensions;
};


f_vector generateRandomVector(size_t dim){
	f_vector v = {new float[dim], dim};

	for(int i = 0; i < v.dimensions; i++){
		int j = rand();
		v.e[i] = *((float*)&j);

	}
	return v;
}

float dotProductSimple(f_vector v1, f_vector v2){
	assert(v1.dimensions = v2.dimensions);
	float sum = 0;
	for(int i = 0; i < v1.dimensions; i++){
		sum += v1.e[i] * v2.e[i];
	}
	return sum;
}

float norm(f_vector v){
	float sum = 0;
	for(int i = 0; i < v.dimensions; i++){
		sum += v.e[i] * v.e[i]; 
	}
	return sqrt(sum);
}
float angleBetween(f_vector v1, f_vector v2){
	float v1Norm = norm(v1);
	float v2Norm = norm(v2);
	float dotV1V2 = dotProductSimple(v1,v2);
	return acos(dotV1V2/(v1Norm * v2Norm));
}

#endif 
