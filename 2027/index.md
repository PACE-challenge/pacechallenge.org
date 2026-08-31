---
layout: page
title: "PACE 2027"
sidebar_link: true
sidebar_sort_order: 10
---

<style media="screen and (max-width:1020px)"> img {display:none;} </style>

## Problem

This year features the $k$-Path problem of finding a path of length $k$ in a graph. See also the [IPEC'26 Announcement Slides](./announcement_slides.pdf).

### What is a $k$-path

In an undirected graph $G = (V, E)$, a $k$-path is a sequence of $k + 1$ distinct vertices $v_1, v_2, \dots, v_{k+1}$ such that $\lbrace v_i, v_{i+1} \rbrace \in E$ for all $i \in \lbrace 1, 2, \dots, k \rbrace$.

In a weighted directed graph $G = (V, A, w)$ with a weight function $w$ mapping directed edges into positive real numbers, a $k$-path is a sequence of $k + 1$ distinct vertices $v_1, v_2, \dots, v_{k+1}$ such that $(v_i, v_{i+1}) \in A$ for all $i \in \lbrace 1, 2, \dots, k \rbrace$, and its weight is $\sum_{i=1}^{k} w(v_i, v_{i+1})$.

![Example](/2027/img/example.png)

For example, the above figure contains an undirected $4$-path on the left and a directed $3$-path of weight $12$ on the right.

### Complexity

Finding the longest path is NP-hard due to the NP-completeness of the Hamiltonian Path problem. It is, however, fixed-parameter tractable in the length of the path. Numerous FPT-time approaches have been designed for the problem such as *color coding* and *algebraic algorithms*. The $k$-Path problem is also FPT with respect to many other parameters such as treedepth. On the negative results, $k$-Path does not admit a polynomial kernel unless $\text{NP} \subseteq \text{coNP} / \text{poly}$.

### Literature

- Monien, B. (1985). How to find long paths efficiently.
- Alon, N., Yuster, R., and Zwick, U. (1995). Color-coding.
- Bodlaender, H. L., Downey, R. G., Fellows, M. R., and Hermelin, D. (2009). On problems without polynomial kernels.
- Williams, R. (2009). Finding paths of length $k$ in $O^*(2^k)$ time.
- Björklund, A., Husfeldt, T., Kaski, P., and Koivisto, M. (2017). Narrow sieves for parameterized paths and packings.
- Tsur, D. (2019). Faster deterministic parameterized algorithm for $k$-path.
- Nederlof, J., Pilipczuk, M., Swennenhuis, C. M., and Węgrzycki, K. (2023). Hamiltonian cycle parameterized by treedepth in single exponential time and polynomial space.

## Timeline

 - September 2026: Announcement of the challenge and tracks &#x2705;
 - October 2026: Definition of input and output formats, tiny test set, and verifier
 - January 2027: Release of public instances and details about the benchmark
 - April 2027: Submission via [optil.io](https://optil.io/) opens
 - Early July 2027: Final submission deadline
 - Mid-July 2027: Solver review phase
 - End of July 2027: Announcement of results

## Tracks
The challenge features three distinct tracks:
1. an "exact unweighted" track -- output the largest integer $k$ in an undirected unweighted graph $G$ such that $G$ contains a $k$-path together with the path as a certificate.
2. an "exact weighted" track -- output a $k$-path of maximum weight in a weighted directed graph. 
3. a "heuristic" track -- output a valid lower bound for the maximum path length in an undirected unweighted graph, computed within a reasonable time limit, and a path witnessing the lower bound.

## Zulip

Join us on [Zulip](https://pacechallenge.zulipchat.com/join/l3eavdfbytkcjiypecpzetuw/) for discussions and updates.


## Program Committee

- [Juha Harviainen](https://juhaharviainen.com/) (University of Helsinki, Finland)
- [André Schidler](https://cca.informatik.uni-freiburg.de/schidler/) (University of Freiburg, Germany)
- [Frank Sommer](https://www.fmi.uni-jena.de/en/6006/dr-frank-sommer) (University of Jena, Germany)
