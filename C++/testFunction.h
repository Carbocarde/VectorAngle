#ifndef tF
#define tF

void testDimensionsFromTo(size_t start = 2, size_t end = 100, size_t step = 2, size_t iterations_per_dimensions = 200000, float (*angleCalculator)(f_vector, f_vector) = angleBetweenNonNormalized){
	srand(time(NULL));		
	auto t0 = high_resolution_clock::now();
	float sum = 0;
	for(size_t i = start; i < end; i += step){
		double time_per_dim = 0;
		for(size_t j = 0; j < iterations_per_dimensions; j++){ 
			f_vector v1 = generateRandomVector(i); 
			f_vector v2 = generateRandomVector(i); 
			auto t1 = high_resolution_clock::now(); // I expect this to be a non factor
			sum += angleCalculator(v1,v2);
			__asm__ __volatile__ ("" : : : "memory"); // This should prevent the optimizer from optimizing
			auto t2 = high_resolution_clock::now();
			duration<double, std::milli> dur = t2 - t1;
			average += dur.count();
		}
		std::cout << i << "," << time_per_dim << "," << time_per_dim/iterations_per_dimensions << std::endl;
	}

	duration<double, std::milli> total = high_resolution_clock::now() - t0;
	std::cout << "Total time: " << total.count() << std::endl;
	std::cout << sum << std::endl;
}
#endif
