The task of this year's challenge is to compute an *optimal* contraction sequence of a given undirected graph. 

## The Input Format
The graph is presented as input in essentially the same graph (`.gr`) format used in [previous iterations](https://pacechallenge.org/2017/treewidth/) of the challenge:

- The vertices of an n-vertex graph are the numbers 1 to n.
- The *line* separator is `\n`.
- A line starting with `c` is a *comment* and has no semantics.
- The first non-comment line is the *p-line*:
	- It is formatted as `p tww n m`, where
	- `n` is the number of vertices;
	- `m` the number of edges to follow;
	- `tww` the *problem descriptor*.
- The p-line is unique and no other line starts with `p`.
- After the p-line there will be exactly `m` non-comment lines that encode the edges:
	- These are formatted as `x y` and define an edge between x and y, where x and y are numbers between 1 and n.

Note that this format allows to encode isolated vertices, multi-edges, and self-loops. Here is an example:

```
c This file describes a graph with 6 vertices and 4 edges.
p tww 6 4
1 2
2 3
c This is a comment and will be ignored.
4 5
4 6
```

### Contracting two Vertices

The contraction of two vertices $x$ and $y$ is defined as follows:
- any edge (black or red) between $x$ and $y$ gets deleted;
- $x$ retains all black edges to its neighbors that are adjacent to $y$;
- all edges from $x$ to vertices that are not adjacent to $y$ become red;
- $x$ is connected with a red edge to all vertices that are connected
  to $y$ but not to $x$;
- $y$ gets deleted from the graph.

Note that in this definition, the contraction operation is *not* symmetric, that is, contracting $(x,y)$ results in a different (but isomorphic) graph than contracting $(y,x)$.

## Contraction Sequences

A *contraction sequence* for a graph $G=G_1$ is a sequence of vertex pairs $(x_1,y_1),(x_2,y_2),\dots$ such that:
- $x_1$ and $y_1$ are (not necessarily connected) vertices in $G_1$;
- contracting $x_1$ and $y_1$ yields a new graph $G_2$, in which the vertices $x_2$ and $y_2$ are present;
- the same argument holds inductively, that is, $x_i$ and $y_i$ are vertices in $G_i$;
- after all contractions have been performed, a single vertex remains.

### Validity of a Contraction Sequence

A contraction sequence is *valid* if:
- it contracts vertices at time $i$ that are present at time $i$;
- it produces a single vertex graph.

The *width* of a contraction sequence is the maximum red degree that appears during the contraction process. 

## Output Format

The output of this year's challenge is the twinwidth format `tww` that contains:
- Optional comment lines starting with `c` (as in the input);
- exactly $n-1$ contraction lines formatted as `x y`.

Here is an example:

```
1 2
1 3
4 5
4 6
1 6
```

## Verifier

This [Python script](../verifier.py) can be used to check whether a given
contraction sequence is valid for a given graph. The output will
either be the sequence width or an error message.

```
 python verifier.py <graph.gr> <result.tww>
```
