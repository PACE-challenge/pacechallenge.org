---
layout: page
title: "PACE 2022 - Track Details"
---

For PACE 2022, we offer the following two tracks:

- [**Exact Track**](#exact-track)
- [**Heuristic Track**](#heuristic-track)

You can participate in any subset of the two tracks.

## Exact Track

Your submission should find an optimal (minimum) feedback vertex set (see also the [problem description](/2022/directed-fvs/)) within 30 minutes.
We expect your submission to be an exact algorithm, although we do not ask you to provide a proof of it. If we find through code checks or experiments that your algorithm is not an exact algorithm, then it will be excluded from the track.
If for some instance your program returns a solution that is not optimal within the time limit, either because it is not minimum or not a feedback vertex set, then your submission will be disqualified. 
See also the [input format](#input-format) and [output format](#output-format).

**Ranking method:**
You will be ranked by the number of solved instances.
In case of a tie, the winner is determined by the time required to solve all instances.


## Heuristic Track

Your submission should find a feedback vertex set (see also the [problem description](/2022/directed-fvs/)) within 10 minutes.
See also the [input format](#input-format) and [output format](#output-format).

**Termination:**
Your program will receive the Unix signal SIGTERM on timeout.
When your process receives this signal, it must immediately print the current best solution to the standard output and then halt.
You can find examples how to handle SIGTERM in [several popular programming languages](https://www.optil.io/optilion/help/signals).
If the process blocks for too long, say 30 seconds after the initial SIGTERM signal, we will forcefully stop it with SIGKILL.
If we forcefully stopped the program, then the instance counts as time limit exceeded and you get 0 points for this instance.
Note that the optil.io system may not work 100% correctly all the time, i.e. the default of your program should be that your program returns a solution after 10 minutes.

**Ranking method:**
You will be ranked by the geometric mean over all instances of 100 × (best solution size) / (solution size).
Here, (solution size) is the size of the solution returned by your submission and (best solution size) is the size of the smallest solution known to the PC (which may not be optimal).
If the output of your program turns out to be not a feedback vertex set (or there is no output on SIGKILL) for some instance, (solution size) for the instance will be regarded as infinity (so you will receive no point for that instance).


## Input Format

The input graph is given via the standard input, which follows the Metis file format described below.

Lines are separated by the character `\n`. Each line that starts with the character `%` is considered to be a comment line.
The first non-comment line contains the number of vertices `n` and edges `m` and an identifier `t` (separated by a single space each time). The identifier `t` indicates whether the graph
contains node or edge weights. Since we only consider unweighted graphs, `t` will always equal `0`.
The next `n` non-comment lines contain the adjacency lists of the nodes. Let $L = \{l_1, \ldots, l_n\}$ denote these lines.
Then, each line $l_u$ is of the form `v1 v2 ... vl` (separated by a single space each time) representing the adjacency list of node `u`. That means `u` is connected to `v1` by an edge `(u,v1)`, and to `v2` by an edge `(u,v2)` and so forth.  Note that the nodes are numbered `1` to `n`.

Moreover, graphs are considered to be directed and simple, i.e. parallel edges and self-loops are forbidden.
For example, a graph with four vertices and five directed edges can be defined as follows:

```
% This file describes a directed graph with four vertices and five directed edges.
4 5 0
2 3
3
% we are half-way done with the instance definition.
4
1
```

## Output Format 
Every line must be in the form `u` followed by the new line character `\n`, where `u` represents a node contained in your feedback vertex set. Here is an example:

```
1
2
```

Use [this](/2022/verifier.tar.gz) to verify whether the output is a feedback vertex set.
To compile this verifier for feedback vertex set execute `make all` in the command line.
Afterwards, there is an executable `verifier`.
The verifier takes two arguments: paths to an input graph file and a solution file containing the solution (see [output format](#output-format)).
Note that it does not check for optimality.


The instances for both tracks will be available to download in December. <!--Download the instances [here](https://).-->

<!--## Benchmark for Heuristic Track-->
<!--[>TODO update<]-->
<!--There are 200 instances, labeled heur001.gr to heur200.gr.-->
<!--The instances are ordered lexicographically by non-decreasing $(n,m)$ where $n$ is the number of vertices and $m$ is the number of edges.-->
<!--The odd instances are public and the even instances are private.-->
<!--Instances heur001.gr to heur170.gr have graph size ($n + m$) at most one million.-->
<!--The largest instance does not exceed size five million.-->
<!--For every instance, the number of vertices is at most two million and there are at least 100 instances in which the number of vertices is at most 1,000.-->
<!--See below for the distribution of instance sizes.-->


<!--TODO Download the instances [here](https://).-->


