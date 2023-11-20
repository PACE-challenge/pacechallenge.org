---
layout: page 
title: "PACE 2024 - Input and Output"
---

The task of this year's challenge is to compute a crossing-minimal two-layer layout of a given bipartite graph $G=((A\dot\cup B),E)$ with a fixed linear order on the vertices of $A$. 

## The Input Format
The graph is presented as input in essentially the same graph (`.gr`) format used in [previous iterations](https://pacechallenge.org/2023/io/) of the challenge:

- The *line separator* is `\n`.
- A line starting with `c` is a *comment* and has no semantics.
- The first non-comment line is the *p-line*:
	- It is formatted as `p ocr n0 n1 m`, where
	- `ocr` the *problem descriptor*;
	- `n0` is the number of vertices in bipartition $A$ (the fixed partition);
	- `n1` is the number of vertices in bipartition $B$ (the free partition);
	- `m` the number of edges to follow.
- The p-line is unique and no other line starts with `p`.
- The vertices in $A$ are numbered from $1$ to $n_0$, the vertices in $B$ are numbered from $n_0+1$ to $n_0+n_1$.
- After the p-line there will be exactly `m` non-comment lines that encode the edges:
	- These are formatted as `x y` and define an edge between $x$ and $y$, where $x$ is a number between $1$ and $n_0$, and $y$ is a number between $n_0+1$ and $n_0+n_1$.

Here is an example:


```
c this is a comment
p ocr 3 3 3
1 5
2 4
3 6
```

![Input](../img/input.svg)

For the parameterized track, the p-line contains an additional parameter `cw` that gives the cutwidth of the graph. 
The first line is then formatted as 'p ocr n0 n1 m cw'
The first $n_0+n_1$ lines then list a total order of the vertices attaining this cutwidth.
```
c this is a comment
p ocr 3 3 3 1
1
5
2
4
6
3
1 5
2 4
3 6
```



## Output Format

In the output, we only expect the second bipartition for the $n_1$ vertices of $B$ to be encoded. 
The $n_0$ vertices of $A$ are assumed to be placed along a line in ascending order. 
Hence, the output file contains just $n_1$ numbers separated by newlines.

```
5
4
6
```

![Output](../img/output.svg)

## Verifier

We provide a [verifier](verifier) to check whether a given
linear order is valid for a given graph. The output will
either be the number of crossings or an error message.

## Autotester

We will provide a repository that contains a script to automatically test your
implementation on a set of instances and solutions, together with a public
test set (TBA December 2024).