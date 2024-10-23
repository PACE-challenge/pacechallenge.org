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

![Example](/2025/img/example.png)

### Complexity

This problem is known to be $W[2]$-hard and hence believed to be not fixed-parameter tractable (fpt). However, it becomes fpt on several structurally restricted classes of graphs, e.g. planar graphs, degenerate graphs, or graphs with girth at least 5 (see [Literature](#literature)).

### Tracks

## Exact Track
todo

## Heuristic Track
todo

### Input and Output

## Input Format

We use the standard DIMACS-like .gr format for graphs. 

Lines are separated by `\n`. Lines starting with a `c` are considered to be a comment and hence ignored. The first (non-comment) line starts with a `p` followed by a problem descriptor, which is `ds` for the Dominating Set problem, followed by the number of vertices `n` and number of edges `m`.
The vertices are numbered from `1` to `n`.
Every other line contains two numbers representing an edge. Hence, the total file consists of $m+1$ non-empty non-comment lines.
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

## Output Format
The output format is similar, the main difference being that each line consists of a single number (representing a vertex of the solution instead of an edge).
We expect the first line to be a number representing the size of your solution. Every other (non-comment) line is expected to be a single number, representing a vertex of the solution.
Hence, the total file consists of $k+1$ non-empty non-comment lines, where $k$ is your solution size.
The solution in the example above can be specified by the following output.
```
    c The first non-comment line represents the solution size
    2
    3
    5
```

## Literature
