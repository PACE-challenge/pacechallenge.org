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

<em style="color:#db8a00">Details about the input and output format will be made available in October.</em>

### Tracks

As in previous incarnations of the challenge, we will have *two*
tracks: One focusing on **Exact** algorithms and one for **Heuristic**
solutions.

#### The Exact Track
The task is to compute an optimal solution for each given graph, that
is, a contraction sequence of *minimum* width. For each instance, the
solver has to output a solution within a time limit of <em
style="color:#db8a00">$x$</em> minutes.

Submissions should be based on provably optimal algorithms, however,
this is *not* a formal requirement. Submissions that output an
*incorrect* solution or a solution that is known to be *non-optimal*
will be **disqualified**. Besides dedicated algorithms, we also
encourage submissions based on other paradigms such as SAT, MaxSAT,
or ILPs.

<em style="color:#db8a00">The scoring-scheme and the precise value of $x$ will be announced in November.</em>

#### The Heuristic Track

In this track the solver shall compute a *good* solution
*quickly*. The solver will be run on each instance for <em
style="color:#db8a00">$y$</em> minutes and receives the Unix signal
SIGTERM afterwards. When receiving this signal, the process has to
output a correct contraction sequence immediately to the standard
output and terminate. If the program does not halt in a reasonable
time after reserving the signal, it will be stopped via SIGKILL. In
this case the instance is counted as *time limited
exceeded*. Information on how to handle Unix signals in various
programming languages can be found on the [optil.io webpage](https://www.optil.io/optilion/help/signals).

For this track solutions do *not* have to be optimal. However, solvers
that produce *incorrect* solution will be **disqualified**.

<em style="color:#db8a00">The scoring-scheme and the precise value of $y$ will be announced in November.</em>

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
   - <em style="color:#db8a00">This set will be made available in October.</em>
2. The *exact set* containing 200 instances divided into 100
   public instances for development and 100 private instances used for
   evaluation.
   - <em style="color:#db8a00">The public instances will be made
     available in December; the private instances after the challenge.</em>
3. The *heuristic set* containing 200 instances divided into 100
   public instances for development and 100 private instances used for evaluation.
   - <em style="color:#db8a00">The public instances will be made
     available in December; the private instances after the challenge.</em>

### Submission

<em style="color:#db8a00">Details about the submission requirements
will be provided in November.</em>

### Timeline

- September 2022: Announcement of the Challenge
- October 2022: Definition of the input and output format. 
  - A tiny test set will be provided.
  - A verifier will be provided.
- November 2022: Announcement of the ranking methods and additional
  information about the submission process.
- December 2022: Public instances and details about the benchmark set
  get published.
- March 2023: Submission on [optil.io](www.optil.io) opens with public
  leaderboard.
- May 2023: The public leaderboard gets frozen.
- June 2023: Submission Deadline.
  - <em style="color:#db8a00">The precise deadline will be announced in
    November.</em>
  - Solver descriptions have to be submitted within two weeks after the deadline.
- July 2023: Announcement of the Results.
- IPEC 2023: Award ceremony.

## Program Committee

- [Max Bannach](http://www.tcs.uni-luebeck.de/mitarbeiter/bannach/) (Universität zu Lübeck)
- [Sebastian Berndt](http://www.tcs.uni-luebeck.de/de/mitarbeiter/berndt/) (Universität zu Lübeck)
