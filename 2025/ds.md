---
layout: page 
title: "PACE 2025 - Dominating Set"
---

## Dominating Set

The first challenge for this year is **Dominating Set**:

**Input:** An undirected graph $G$ <br/>
**Output:** A dominating set for $G$

### What is a dominating set?

A _dominating set_ for a graph $G$ is a set $D \subseteq V(G)$ such that every vertex or one of its neighbors is contained in $D$, that is, for all $v \in V(G)$ we have $v \in D$ or there is $u \in S$ with $uv \in E(G)$.

![Example](/2025/img/example_ds.png)

### Complexity

Dominating set is known to be NP-complete, even on planar graphs of maximum degree $3$. 
The problem is also W$[2]$-hard (parameterized by solution size), and hence believed to be not fixed-parameter tractable (fpt) in general. 
However, it is fpt on many structurally restricted classes of graphs, e.g. planar graphs, degenerate graphs, biclique-free graphs, and more. 
The problem is linear time solvable on all graphs with a fixed bounded treewidth or cliquewidth. 

A simple greedy algorithm on $n$-vertex graphs yields an $\ln n$ approximation, and it is NP-complete to compute better approximations in general. 
On several restricted graph classes we can compute much better approximations. 
For instance, the problem admits a polynomial-time approximation scheme
(PTAS) on planar graphs and, more generally, on graph classes with subexponential expansion. 
It admits a constant factor approximation on classes of bounded degeneracy and an $O(d\cdot \ln k)$ approximation (where $k$ denotes
the size of a minimum dominating set) on classes of VC dimension $d$. 


## Tracks

### Exact Track

The task is to compute an optimal solution for each given graph, that is, a minimum dominating set. For each instance, the solver has to output a solution within a time limit of 30 minutes and a memory limit of 8 GB.

Instances in this track will satisfy structural properties that theoretically allow the efficient solution of the problem, e.g. be planar and have a moderately small domination number, have moderately small treewidth or cliquewidth, etc. 

Submissions should be based on provably optimal algorithms, however, this is not a formal requirement. Submissions that output an incorrect solution or a solution that is known to be non-optimal will be disqualified. Besides dedicated algorithms, we also encourage submissions based on other paradigms such as SAT, MaxSAT, or ILPs. We allow the use of open source SAT solvers and ILP solvers.

### Heuristic Track

In this track, the solver shall compute a good solution quickly. The solver will be run on each instance for 5 minutes and a memory limit of 8GB. After 5 minutes the solver receives the Unix signal SIGTERM. When receiving this signal, the process has to output a dominating set to the standard output and terminate. 
If the program does not halt in a reasonable time after reserving the signal, it will be stopped via SIGKILL. In this case the instance is counted as time limit exceeded. 

For this track solutions do not have to be optimal. However, solvers that produce incorrect solution will be disqualified.

## Input and Output

### Input Format

We use the standard DIMACS-like .gr format for graphs. 

Lines are separated by `\n`. Lines starting with a `c` are considered to be a comment and hence ignored. The first (non-comment) line starts with a `p` followed by a problem descriptor, which is `ds` for the Dominating Set problem, followed by the number of vertices `n` and number of edges `m`.
The vertices are numbered from `1` to `n`.
Every other line contains two numbers representing an edge. Hence, the total file consists of $m+1$ non-comment lines.
The example graph above can be described by the following file.
```
    c I am a comment
    p ds 7 9
    1 2
    1 3
    2 3
    2 4
    3 4
    4 5
    5 6
    5 7
    6 7
```

### Output Format
The output format is similar, the main difference being that each line consists of a single number (representing a vertex of the solution instead of an edge).
We expect the first non-comment line to be a number representing the size of your solution. Every other (non-comment) line is expected to be a single number, representing a vertex of the solution.
Hence, the total file consists of $k+1$ non-comment lines, where $k$ is your solution size.
The solution in the example above can be specified by the following output.
```
    c The first non-comment line represents the solution size
    2
    3
    5
```

## Final Evaluation
The final score will be computed over all public and private instances (for the parameterized track, we use a selection of 100 public instances, which are the ones provided on optil.io).

## Literature

- T. W. Haynes, S. Hedetniemi, P. Slater. Fundamentals of Domination in Graphs (book).
- F. V. Fomin, D. Kratsch, and G. J. Woeginger. Exact (exponential) algorithms for the dominating set problem.
- B. Randerath and I. Schiermeyer. Exact algorithms for minimum dominating set. 
- F. V. Fomin, F. Grandoni, D. Kratsch. Measure and conquer: Domination – a case study.
- D. S. Johnson. Approximation algorithms for combinatorial problems.
- L. Lovász. On the ratio of optimal integral and fractional covers.
- B. S. Baker. Approximation algorithms for NP-complete problems on planar graphs.
- N. Bansal and S. W. Umboh. Tight approximation bounds for dominating set on graphs of bounded arboricity.
- J. Alber, M. R. Fellows, and R. Niedermeier. Polynomial-time data reduction for Dominating Set. 
- G. Philip, V. Raman, and S. Sikdar. Polynomial kernels for Dominating Set in graphs of bounded
degeneracy and beyond.



