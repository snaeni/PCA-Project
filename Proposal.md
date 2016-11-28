CSE 591 Project Proposal
Sharath Kumar Naeni
110950172


1.  The Coin Change Problem:


Formulation: How many different ways can you make change for an amount N, given a list of coin denominations.
This is a different to “change making problem” (Least number of coins to make amount N).
(1)            The problem, i.e., what's given and what's wanted from your project:
Project focus is to arrive at some efficient algorithm for “The Coin Change Problem”
 
(2)            The method that you use to solve the problem:
starting from recursive algorithm using the systematic method to arrive at an efficient iterative approach and calculate runtimes of new method.
(similar to chapter 4: III method applied on LCS algorithm)
 
(3)            The implementation of the method:
Will implement above method in C.
http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/
Memoized recursion method at https://quickgrid.wordpress.com/2015/05/23/0-1-knapsack-iterative-and-recursive-with-code/
 
(4)            The results, including the runs and tests:
Will compare the clarity, correctness and running times with both recursive and dynamic programming approaches at:
http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
 
2.  Convex Hull:


The reference at http://jeffe.cs.illinois.edu/teaching/373/notes/x05-convexhull.pdf talks about four
 Approaches to find convex hull solutions, namely:
a.     Jarvis Algorithm
b.     Divide and conquer
c.     Graham’s Algorithm
d.     Chan’s algorithm
Jarvis Algorithm is a straightforward naïve approach with running time O(n2) and Graham’s is an optimization with running time(nlogn).


(1)   The problem, i.e., what's given and what's wanted from your project:
Project focus would be to study above algorithms. Particularly Jarvis and Graham’s. Goal of the project is to arrive at an efficient algorithm (Close to Graham’s algorithm) using systematic method.


(2)   The method that you use to solve the problem:
Most of the problems taught in class deal with optimizations starting from clear recursive definitions to efficient iterative/incremental(book-keeping) approach. (LCS, 0-1 knapsack…)
Jarvis Algorithm itself is an iterative approach. We can still apply “Incrementalize” and “Implement” methods to optimize Jarvis algorithm:
example: we can store the clockwise orientation of triplet (p,q,r) and use it for subsequent iterations in Jarvis method.


(3)   The implementation of the method:
Jarvis method: http://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/
Graham’s method: http://www.geeksforgeeks.org/convex-hull-set-2-graham-scan/


(4)   The results, including the runs and tests:
Will compare the clarity, correctness and running times of Jarvis method, Graham’s method at above links with our derived method.
