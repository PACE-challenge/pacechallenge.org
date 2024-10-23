---
layout: page 
title: "PACE 2025 - Hitting Set"
---


## Hitting Set

The second challenge for this year is **Hitting Set**

**Input**: A set system (hypergraph) $\mathcal{S}$ <br/>
**Output**: A hitting set for $\mathcal{S}$

### What is a hitting set?

A _hitting set_ for a set system $\mathcal{S}$ is a set $H \subseteq V(G)$ such that every set $S \in E(\mathcal{S})$ contains at least one vertex from $H$, that is, for all $S \in E(\mathcal{S})$ we have $S \cap H \neq \varnothing$.

The Hitting Set problem is a natural generalization of many well-known graph problems, including

 - **Vertex Cover**, by considering the set of all edges
 - **Dominating Set**, by considering the set of all closed neighborhoods
 - **(Directed) Feedback Vertex Set**, by considering the set of all (directed) cycles

### Complexity
As Dominating Set is already $W[2]$-complete, it is immediate that Hitting Set is $W[2]$-hard and hence believed to be not fixed-parameter tractable (fpt).
In fact, Hitting Set is also $W[2]$-complete.
However, it becomes fpt on several structurally restricted classes of set systems, e.g. set systems where the size of each set is bounded by a constant (see [Literature](#literature)).

### Tracks

## Exact Track
todo

## Heuristic Track
todo

### Input and Output

## Input Format

We use a natural extension for standard DIMACS-like .gr for hypergraphs, namely .hgr files, where every line represents a set.

Lines are separated by `\n`. Lines starting with a `c` are considered to be a comment and hence ignored. The first (non-comment) line starts with a `p` followed by a problem descriptor, which is `hs` for the Hitting Set problem, followed by the number of vertices `n` and number of sets `m`.
The vertices are numbered from `1` to `n`.
Every other line contains a list of numbers representing a set. The total file consists of $m+1$ non-empty non-comment lines.
The example set system above can be described by the following file.
```
    c I am a comment
    p hs x x
    TODO
```

## Output Format
The output format is as for the dominating set problem.
We expect the first line to be a number representing the size of your solution. Every other (non-comment) line is expected to be a single number, representing a vertex of the solution.
Hence, the total file consists of $k+1$ non-empty non-comment lines, where $k$ is your solution size.
The solution in the example above can be specified by the following output.
```
    c The first non-comment line represents the solution size
    TODO
```


### Literature