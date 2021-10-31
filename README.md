## About This Project
This project aims to discover/document the different ways to calculate the angle between two vectors.

## Current Methods
1. Dot Product (norm)
2. Dot Product (mag)
3. Projection

## Current Numbers
Runtime for each method to calculate the angle between 1,000,000 randomly generated vectors on an Intel® Core™ i7-8550U CPU
(in seconds).

Vector Dimension|Dot Product - Norm|Dot Product - Mag|Projection
---------------:|-----------------:|----------------:|---------:
2|4.844|0.631|0.952
3|4.866|0.846|1.038
4|4.777|0.591|0.939
5|4.572|0.762|1.028
10|7.645|0.651|1.012
20|8.083|0.901|1.144
30|7.082|0.816|1.336
40|12.186|0.867|1.434
50|14.435|0.767|1.177
100|15.922|1.015|1.498
1,000|

## Future Methods
1. Change of Basis
2. Dot Product Binary Search

## TODO
- [X] Dot Product Norm Implementation
- [X] Projection Implementation
- [X] Dot Product Magnitude Implementation
- [X] Testing Suite
- [X] Numba Integration
  - [X] Methods
  - [X] Util
- [X] Projection Method Writeup
- [ ] Publish Repo
- [ ] Change of Basis Implementation
- [ ] Dot Product Binary Search Implementation

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
    - I use Pycharm, as this allows me to collect and export the runtime for each of the pytest testcases.
 - Util.py
    - Contains utility functions like generating vectors or normalizing a vector.

## Running this project:
`pip install -r requirements.txt`

`pytest TestAngle.py`

`pytest TestAngleBenchmark.py`
