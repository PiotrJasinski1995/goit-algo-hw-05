# goit-algo-hw-05

## Task 1
Delete method to delete key-value pairs of the HashTable table, which was already implemented.

## Task 2
Binary search for a sorted array with fractional numbers. The written function for binary search return a tuple, where the first element is the number of iterations required to find the element. The second element gives the "upper bound" - the smallest element that is greater than or equal to the given value.

## Task 3
Comparation of the efficiency of the substring search algorithms: Boyer-Moore, Knuth-Morris-Pratt, and Rabin-Karp based on two text files:
- as expected, the Boyer-Moore was the fastest algorithm for each text separately and in general, in the best case it can even have linear time complexisty O(n),
- the slowest algorithm in every case was Rabin-Karp (with best case O(n + m) and worst case O(n * m),
- the Knuth-Morris-Pratt was always slower than Boyer-Moore, but faster than Rabin-Karp.
