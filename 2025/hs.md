---
layout: page 
title: "PACE 2025 - Hitting Set"
---


## Hitting Set

The second challenge for this year is **Hitting Set**:

**Input**: A set system (hypergraph) $\mathcal{S}$ <br/>
**Output**: A hitting set for $\mathcal{S}$

### What is a hitting set?

A _hitting set_ for a set system $\mathcal{S}$ is a set $H \subseteq V(G)$ such that every set $S \in E(\mathcal{S})$ contains at least one vertex from $H$, that is, for all $S \in E(\mathcal{S})$ we have $S \cap H \neq \varnothing$.

![Example](/2025/img/example_hs.png)

The Hitting Set problem is a natural generalization of many well-known graph problems, including

 - **Vertex Cover**, by considering the set of all edges
 - **Dominating Set**, by considering the set of all closed neighborhoods
 - **(Directed) Feedback Vertex Set**, by considering the set of all (directed) cycles

### Complexity
As Dominating Set is NP-hard and W$[2]$-hard, it is immediate that also Hitting Set is NP-hard and W$[2]$-hard. 
In fact, Hitting Set is also NP-complete and W$[2]$-complete.
However, it is fpt on several structurally restricted classes of set systems, e.g. set systems where the size of each set is bounded by a constant and set systems of bounded VC-dimension (see [Literature](#literature)).

## Tracks

### Exact Track

The task is to compute an optimal solution for each given graph, that is, a minimum hitting set. For each instance, the solver has to output a solution within a time limit of 30 minutes and a memory limit of 8 GB.

Instances in this track will satisfy structural properties that theoretically allow the efficient solution of the problem, e.g. encode graph instances (of dominating set, vertex cover, feedback vertex set, etc.) that admit efficient solutions, however, it will not be given with the input what type of problem is encoded. 

Submissions should be based on provably optimal algorithms, however, this is not a formal requirement. Submissions that output an incorrect solution or a solution that is known to be non-optimal will be disqualified. Besides dedicated algorithms, we also encourage submissions based on other paradigms such as SAT, MaxSAT, or ILPs. We allow the use of open source SAT solvers and ILP solvers.

### Heuristic Track

In this track, the solver shall compute a good solution quickly. The solver will be run on each instance for 5 minutes and a memory limit of 8GB. After 5 minutes the solver receives the Unix signal SIGTERM. When receiving this signal, the process has to output a dominating set to the standard output and terminate. 
If the program does not halt in a reasonable time after reserving the signal, it will be stopped via SIGKILL. In this case the instance is counted as time limit exceeded. 

For this track solutions do not have to be optimal. However, solvers that produce incorrect solution will be disqualified.

## Input and Output

### Input Format

We use a natural extension for standard DIMACS-like .gr for hypergraphs, namely .hgr files, where every line represents a set.

Lines are separated by `\n`. Lines starting with a `c` are considered to be a comment and hence ignored. The first (non-comment) line starts with a `p` followed by a problem descriptor, which is `hs` for the Hitting Set problem, followed by the number of vertices `n` and number of sets `m`.
The vertices are numbered from `1` to `n`.
Every other line contains a list of numbers representing a set. The total file consists of $m+1$ non-empty non-comment lines.
The example set system above can be described by the following file.
```
    c I am a comment
    p hs 6 5
    1 2
    2 3 4
    2 4 5
    1 3 6
    5 6
```

### Output Format
The output format is as for the dominating set problem.
We expect the first line to be a number representing the size of your solution. Every other (non-comment) line is expected to be a single number, representing a vertex of the solution.
Hence, the total file consists of $k+1$ non-comment lines, where $k$ is your solution size.
The solution in the example above can be specified by the following output.
```
    c The first non-comment line represents the solution size
    2
    2
    6
```


## Literature

 - M. Cygan, F. V. Fomin, Ł. Kowalik, D. Lokshtanov, D. Marx, M. Pilipczuk, M. Pilipczuk, S. Saurabh: Parameterized Algorithms.
 - H. Brönnimann, M. T. Goodrich: Almost optimal set covers in finite VC-dimension.
 - F. N. Abu-Khzam. A kernelization algorithm for d-hitting set.
