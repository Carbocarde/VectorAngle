## About This Project
Dot products encode a lot of information - one of which is the angle between two vectors.
This project aims to discover/document the different ways to calculate the angle between two vectors.

## Blog Series

1. [Intro - Dot Product](https://www.nulliq.dev/posts/vector-angle-1/)
2. [Method 2 - Change of Basis](https://www.nulliq.dev/posts/vector-angle-2/)
3. [Method 3 - Projection](https://www.nulliq.dev/posts/vector-angle-3/)
4. [Benchmarking](https://www.nulliq.dev/posts/vector-angle-4/)

## Current Methods
1. Dot Product (norm)
2. Dot Product (mag)
3. Projection [(Writeup about this method)](Writeups/Projection%20Approach.pdf)
4. Dot Product Bin Search (mag)
5. Projection Bin Search

## Future Methods
1. Change of Basis

## TODO
- [X] Projection Method Writeup
- [X] Publish Repo
- [X] Rewrite in C++

## Languages
- Python
  - Has testing for method accuracy and a pytest benchmark.
    - Benchmark is not as accurate as the C++ implementation.
- C++
  - Is much better for benchmarking.
  - Does not have method accuracy checks (Methods are created/checked in Python and then ported to C++).
