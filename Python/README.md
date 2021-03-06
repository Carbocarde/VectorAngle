## Python Implementation

## Current Methods
1. Dot Product (norm)
2. Dot Product (mag)
3. Projection
4. Dot Product Bin Search (mag)
5. Projection Bin Search

## Current Numbers - Python Benchmark
Runtime for each method to calculate the angle between 1,000,000 randomly generated vectors on an Intel® Core™ i7-8550U CPU
(in seconds).

Vector Dimension|Dot Product - Norm|Dot Product - Mag|Projection|Dot Product - Bin Search|Projection - Bin Search|
---------------:|-----------------:|----------------:|---------:|-----------------------:|----------------------:|
2|2.135|0.634|1.112|1:23|1:30
3|4.157|0.592|0.877|1:24|1:30
4|3.169|0.877|1.112|1:21|1:30
5|3.170|0.745|1.420|1:28|1:33
10|4.960|0.828|0.955|1:21|1:31
20|6.657|0.764|5.416|1:22|1:29
30|9.061|0.714|1.088|1:22|1:33
40|7.343|0.871|1.335|1:21|1:32
50|5.553|1.026|1.360|1:22|1:31
100|1.992|0.757|1.420|1:27|1:43
1,000|1.283|0.560|0.826|5:02|8:45

## Future Methods
1. Change of Basis

## TODO
- [X] Dot Product Norm Implementation
- [X] Projection Implementation
- [X] Dot Product Magnitude Implementation
- [X] Testing Suite
- [X] Numba Integration
  - [X] Methods
  - [X] Util
- [X] Dot Product Binary Search Implementation
- [X] Projection Binary Search Implementation
- [ ] Change of Basis Implementation

## File Structure
 - Angle.py
    - Contains the implementation for the general-solvers
 - SpecialCases.py
    - Contains the implementation for the normalized vector solvers
 - TestAngle.py
    - Contains testcases to ensure that the angle calculations are accurate when compared to the traditional dot product method.
    - This uses both hand-written testcases along with repeatable (seeded) randomly-generated testcases.
 - TestAngleBenchmark
    - Contains testcases that execute the methods a specified number of times on randomly generated vectors.
    - The testcases will take a while to start executing, as all the vectors are generated prior to any testcase being executed.
 - Util.py
    - Contains utility functions like generating vectors or normalizing a vector.

## Running this project:
`pip install -r requirements.txt`

`pytest TestAngle.py`

`pytest --durations=0 TestAngleBenchmark.py`
