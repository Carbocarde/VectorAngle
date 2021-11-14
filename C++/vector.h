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

// Creates a vector with random values in it
// There are no guarantees about the distribution, all possible values a float can take can be reached
f_vector generateRandomVector(size_t dim){
	f_vector v = {new float[dim], dim};

	for(size_t i = 0; i < v.dimensions; i++){
		int j = rand();
		v.e[i] = *((float*)&j);

	}
	return v;
}

void generateRandomVector(f_vector * v, size_t dim){
	v->e = new float[dim];
	v->dimensions = dim;
	for(size_t i = 0; i < dim; i++){
		int j = rand();
		v->e[i] = *(float *)&j;

	}

};

// takes in two vectors and gives back their dot product
float dotProductSimple(f_vector v1, f_vector v2){
	float sum = 0;
	for(size_t i = 0; i < v1.dimensions; i++){
		sum += v1.e[i] * v2.e[i];
	}
	return sum;
}

float norm(f_vector v){
	float sum = 0;
	for(size_t i = 0; i < v.dimensions; i++){
		sum += v.e[i] * v.e[i];
	}
	return sqrt(sum);
}

void normalize(f_vector v){
	float n = norm(v);
	for(size_t i = 0; i < v.dimensions; i++){
		v.e[i] /= n;
	}
}

void scale(f_vector v, float scalar){
	for(size_t i = 0; i < v.dimensions; i++){
		v.e[i] *= scalar;
	}
}

float angleBetweenNonNormalized(f_vector v1, f_vector v2){
	float v1Norm = norm(v1);
	float v2Norm = norm(v2);
	float dotV1V2 = dotProductSimple(v1,v2);
	return acos(dotV1V2/(v1Norm * v2Norm));
}

float angleBetweenNormalized(f_vector v1, f_vector v2){
	normalize(v1);
	normalize(v2);
	return acos(dotProductSimple(v1,v2));
}

float angleBetweenProjection(f_vector v1, f_vector v2){
	float dot = dotProductSimple(v1, v2);
	float div = dotProductSimple(v1, v1);
	float scalar = dot / div;
	scale(v1, scalar);

	// v1 now stores the projected vector of v2
	float hor_mag_sq = dotProductSimple(v1,v1);
	float hyp_mag_sq = dotProductSimple(v2,v2);

	return acos(sqrt(hor_mag_sq/hyp_mag_sq));
}

#endif
