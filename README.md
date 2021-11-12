## About This Project
Dot products encode a lot of information - one of which is the angle between two vectors. 
This project aims to discover/document the different ways to calculate the angle between two vectors.

## Current Methods
1. Dot Product (norm)
2. Dot Product (mag)
3. Projection
4. Dot Product Bin Search (mag)
5. Projection Bin Search

## Current Numbers
Runtime for each method to calculate the angle between 1,000,000 randomly generated vectors on an Intel® Core™ i7-8550U CPU
(in seconds).

Vector Dimension|Dot Product - Norm|Dot Product - Mag|Projection|Dot Product - Bin Search|Projection - Bin Search|
---------------:|-----------------:|----------------:|---------:|-----------------------:|----------------------:|
2|4.844|0.631|0.952|1:23|1:30
3|4.866|0.846|1.038|1:24|1:30
4|4.777|0.591|0.939|1:21|1:30
5|4.572|0.762|1.028|1:28|1:33
10|7.645|0.651|1.012|1:21|1:31
20|8.083|0.901|1.144|1:22|1:29
30|7.082|0.816|1.336|1:22|1:33
40|12.186|0.867|1.434|1:21|1:32
50|14.435|0.767|1.177|1:22|1:31
100|15.922|1.015|1.498|1:27|1:43
1,000|2:16|5:22|5:04|5:02|8:45

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
- [X] Projection Method Writeup
- [X] Dot Product Binary Search Implementation
- [X] Projection Binary Search Implementation
- [X] Publish Repo
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
    - I use Pycharm, as this allows me to collect and export the runtime for each of the pytest testcases.
 - Util.py
    - Contains utility functions like generating vectors or normalizing a vector.

## Running this project:
`pip install -r requirements.txt`

`pytest TestAngle.py`

`pytest TestAngleBenchmark.py`
