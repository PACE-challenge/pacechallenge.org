---
layout: page
title: "PACE 2023"
sidebar_link: true
sidebar_sort_order: 10
---

This year's challenge is about
[twinwidth](https://en.wikipedia.org/wiki/Twin-width), a graph
parameter that (intuitively) measures the distance of a graph to a
co-graph. The parameter was introduced in
[2020](https://ieeexplore.ieee.org/document/9317878) and has lead to
a multitude of theoretical
[results](https://dblp.uni-trier.de/search?q=twin-width) since then.

### Challenge Description

The goal of this year's challenge is to compute a contraction sequence
for a given graph of small width. More precisely: 

**Input:** An *undirected* graph $G=(V,E)$. <br/>
**Output:** A contraction sequence that contracts $G$ to a single
vertex. <br/>
**Measure:** The width of the contraction sequence. 

Details about the input and output format can be found [here](./io.md). 

### Tracks

As in previous incarnations of the challenge, we will have *two*
tracks: One focusing on **Exact** algorithms and one for **Heuristic**
solutions. 

Details about the scoring methods can be found [here](./scoring).

#### The Exact Track
The task is to compute an optimal solution for each given graph, that
is, a contraction sequence of *minimum* width. For each instance, the
solver has to output a solution within a time limit of <em
style="color:#db8a00">30 minutes</em>.

Submissions should be based on provably optimal algorithms, however,
this is *not* a formal requirement. Submissions that output an
*incorrect* solution or a solution that is known to be *non-optimal*
will be **disqualified**. Besides dedicated algorithms, we also
encourage submissions based on other paradigms such as SAT, MaxSAT,
or ILPs.

#### The Heuristic Track

In this track the solver shall compute a *good* solution
*quickly*. The solver will be run on each instance for <em
style="color:#db8a00">5 minutes</em> and receives the Unix signal
SIGTERM afterwards. When receiving this signal, the process has to
output a correct contraction sequence immediately to the standard
output and terminate. If the program does not halt in a reasonable
time after reserving the signal, it will be stopped via SIGKILL. In
this case the instance is counted as *time limited
exceeded*. Information on how to handle Unix signals in various
programming languages can be found on the [optil.io webpage](https://www.optil.io/optilion/help/signals).

For this track solutions do *not* have to be optimal. However, solvers
that produce *incorrect* solution will be **disqualified**.

### Theory Awareness 

Very little is known about computational aspects of twinwidth. There
is a reasonable effective
[SAT-encoding](https://arxiv.org/abs/2110.06146) and a proof that it
is already hard to test whether a graph has twinwidth [at most
four](https://arxiv.org/abs/2112.08953). Since one of the goals of the
challenge is to bridge the gap between theory and practice, we
encourage submissions that are baked with new theoretical
insights. This year's incarnation of the PACE supports this idea in two ways:

1. The instance sets will contain some instances from predefined graph
   classes (such as planar graphs, twinwidth 2 graphs, etc.). Solvers
   can thus specialize, to a certain degree, to specific inputs.
2. We will give an extra **Theory Award** to the submission with the most
   interesting theoretical guarantee that has to be documented in the solver description. 

### Benchmark Sets

There will be three benchmark set:

1. A *tiny set* for debugging that contains graphs together with their
   twinwidth.
   - [instances](./tiny-set.zip)
   - [solutions](./tiny-set-sol.zip)
   - [images](./tiny-set.pdf)
2. The *exact set* containing 200 instances divided into 100
   public instances for development and 100 private instances used for
   evaluation.
   - [public
     instances](https://cloudtcs.tcs.uni-luebeck.de/index.php/s/Dm5pZfzxkoP8cL6)
     <em style="color:#ff0000">(Update from 15.02.2023: The set contained duplicates, which have now been replaced.)</em>
3. The *heuristic set* containing 200 instances divided into 100
   public instances for development and 100 private instances used for evaluation.
   - [public instances](https://cloudtcs.tcs.uni-luebeck.de/index.php/s/QMxJFWgDZF4bEo2)

### Submission

Details about the submission requirements ca be found [here](submissions).

### Timeline

- September 2022: Announcement of the Challenge
- October 2022: Definition of the input and output format. 
  - A tiny test set will be provided.
  - A verifier will be provided.
- November 2022: Announcement of the ranking methods and additional
  information about the submission process.
- ~~December 2022~~ January 2023: Public instances and details about the benchmark set
  get published.
- March 2023: Submission on [optil.io](www.optil.io) opens with public
  leaderboard.
- May 2023: The public leaderboard gets frozen.
- June 2023: Submission Deadline.
	- June 1st, 2023 (AoE): Submission deadline for solver.
	- June 15th, 2023 (AoE): Submission deadline for solver description.
- July 2023: Announcement of the Results.
- IPEC 2023: Award ceremony.

## Program Committee

- [Max Bannach](http://www.tcs.uni-luebeck.de/mitarbeiter/bannach/) (Universität zu Lübeck)
- [Sebastian Berndt](http://www.tcs.uni-luebeck.de/de/mitarbeiter/berndt/) (Universität zu Lübeck)
