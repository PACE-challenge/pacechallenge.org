---
title: "PACE 2016 – Track B: Feedback Vertex Set"
---

The objective of this track is to solve the NP-hard **Feedback Vertex Set Problem**:

- **Input:** An undirected graph.
- **Output:** A minimum-size set of vertices such that deleting these vertices destroys all cycles (i.e., produces a forest).

The following contest rules are there to make the contest interesting and fair. The submission can be made by an individual or by a team. If you would like to participate, but find that the rules are impeding you or are unclear, please contact us at christian.komusiewicz@uni-jena.de.


## Test Cases
The test cases are 230 graphs from various real-world sources, ranging from 30 to 20,000 vertices and from 60 to 90,000 edges, with a median of 300 vertices and 1000 edges. Of these, a random subset of 100 is being published and 130 will be reserved for the evaluation. The published instances can be downloaded [here](https://github.com/ckomus/PACE-fvs) (the repository now features the public and hidden instances).


## Evaluation
This track focuses on fixed-parameter algorithms computing optimal solutions. Evaluation criterion is the number of instances that can be solved within the time limit (30 minutes per instance) on the evaluation machine (Xeon E5-1620 3.6GHz, 64GB RAM). Participants are strongly encouraged to submit preliminary versions (up to once per week) and will receive feedback on correctness and performance.


## Submission Requirements
Implementations must use fixed-parameter algorithms. The standard parameter is the size of the feedback vertex set, but other non-trivial parameterizations (such as treewidth) are encouraged. The solution must be optimal, or if a randomized algorithm is used, have a provable error probability of at most 10<sup>-12</sup> (under the assumption that the random number generator produces true random bits).

Implementations must be provided in source code under a free software license (e.g. [GPLv2](http://www.gnu.org/licenses/license-list.html#GPLv2)) and must compile and run on the evaluation machine (Debian GNU/Linux 7.7). This system supports most popular programming languages such as C, C++, Java, C\#, Scala, Go, and Haskell; contact christian.komusiewicz@uni-jena.de if you are unsure whether your environment is supported. To improve comparability, implementations must not use SAT solvers, ILP solvers, or similar general solvers for NP-hard problems, and use only a single CPU thread. The preferred method of submission is a link to a publicly available source code repository such as [GitHub](https://github.com/), sent to christian.komusiewicz@uni-jena.de, or alternatively a source code archive.

Implementations must be command-line programs which receive the graph on standard input and write the solution to standard output. Each implementation should be accompanied by a short description of the fixed-parameter algorithm either in plain text format or as a pdf.


## Input Format
The graph format is a simple text format, where each line describes one edge, given by its two endpoints separated by whitespace, e.g.:

    ml mr
    l1 ml
    l2 ml
    l1 l2
    r1 mr
    r2 mr
    r1 r2

Vertex names can be any combination of letters, digits, and \_. Lines starting with ‘\#’ are comments. Note that this graph format cannot describe degree-0 vertices (which are irrelevant for Feedback Vertex Set anyway).


## Output format
The output is a minimum-size feedback vertex set, with one vertex per line, e.g.:

    l1
    r2

If the algorithm is randomized, the program must additionally accept a command line argument of the form “-s X”, where X is a 32-bit random seed as decimal number, and must yield reproducible results for the same seed.


## Notes and Hints

The instances are selected to be challenging. It is expected that an initial implementation will only solve a few of them, and even the winning entry might solve only a minority.
Since the parameter is probably not going to be very small in all instances, a key for success is probably good data reduction. [Becker et al](http://arxiv.org/pdf/1106.0225.pdf). give a few simple rules.
Good starting points might be the simple randomized algorithm by [Becker et al](http://arxiv.org/pdf/1106.0225.pdf). running in *O*(4<sup>*k*</sup>) time, where *k* is the size of the feedback vertex set, or the moderately involved deterministic algorithm by [Kociumaka and Pilipczuk](http://arxiv.org/pdf/1306.3566.pdf), running in *O*(3.618<sup>*k*</sup>) time.
Some instances contain self-loops (edges of the form “v1 v1”). The corresponding vertex needs to be deleted in any solution.
The benchmark instances do not contain multiple edges. It is not necessary that your implementation handles multiple edges in the input. However, multiple edges may result from data reduction (see [Becker et al](http://arxiv.org/pdf/1106.0225.pdf).) and one might want to consider this when designing the graph data structures.
