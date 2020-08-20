---
title: "PACE 2017 – Track B: Minimum Fill-In"
---

The objective of this track is to solve the NP-hard **Minimum Fill-In Problem**:

- **Input:** An undirected simple graph G.
- **Output:** A minimum-size set of edges such that adding these edges to G results in a simple chordal graph, that is, a graph in which every induced cycle has length exactly three.

## Background

The minimum fill-in problem has applications in optimizing Gaussian elimination on sparse symmetric matrices. While sweeping the matrix, new non-zero elements may be introduced. To minimize the number of newly introduced nonzero elements, one can solve the minimum fill-in problem on an associated graph. Sweeping the matrix in the order dicated by a perfect elimination order of the chordal graph, yields a Gaussian elimination that introduces the fewest new nonzero elements. The problem is also of interest in Computational Phylogeny and the analysis of protein interaction networks. More background can be found in [Wikipedia](https://en.wikipedia.org/wiki/Chordal_completion#Applications).

Minimum fill-in is notorious for being one of the open problems in the first edition of Garey and Johnson’s monograph on NP-completeness. Yannakakis later proved that the problem is NP-complete. Several FPT-algorithms have been developed for chordal completion parameterized by the number k of edges that need to be added to make the graph chordal. The first was given by Kaplan et al ([dx.doi.org/10.1137/S0097539796303044](https://dx.doi.org/10.1137/S0097539796303044)), which runs in time O(16<sup>k</sup> k<sup>6</sup> + k<sup>2</sup> mn), and utilizes a kernel with O(k<sup>3</sup>) vertices. Natanzon et al. ([dx.doi.org/10.1137/S0097539798336073](https://dx.doi.org/10.1137/S0097539798336073)) improved the kernel size to O(k<sup>2</sup>) vertices and used it to develop a polynomial-time approximation algorithm. The algorithm by Fomin and Villanger, running in time 2<sup>O(k<sup>0.5</sup>\ log\ k)</sup> + O(k<sup>2</sup> mn), has the currently best worst-case running time  (<http://dx.doi.org/10.1137/11085390X>).

## Contest Rules

The following contest rules are there to make the contest interesting and fair. The submission can be made by an individual or by a team. If you would like to participate, but find that the rules are impeding you or are unclear, please contact us at komusiewicz@informatik.uni-marburg.de.

**Test Cases.** The test cases are 100 graphs which can be downloaded [here](https://github.com/PACE-challenge/Minimum-Fill-In-PACE-2017-instances).

**Evaluation.** This track focuses on fixed-parameter algorithms computing optimal solutions. Evaluation criterion is the number of instances that can be solved within the time limit (30 minutes per instance) on the evaluation machine (we will soon post details on this machine). To evaluate the algorithms we will use a set of 100 hidden instances which are similar in structure to the public test cases and revealed after the contest. Participants are strongly encouraged to submit preliminary versions (up to once per week) and will receive feedback on correctness and performance. We will publish a leader board with the three currently best submissions.

**Submission Requirements.** Implementations must not use SAT solvers, ILP solvers, or similar general solvers for NP-hard problems. We encourage submissions of algorithms that are fixed-parameter algorithms for any non-trivial parameterization; the standard parameter is the size of the edge set to add. The solution must be optimal, or if a randomized algorithm is used, have a provable error probability of at most 10<sup>-12</sup> (under the assumption that the random number generator produces true random bits).

Implementations must be provided in source code under a free software license (e.g. [GPLv2](http://www.gnu.org/licenses/license-list.html#GPLv2)) and must compile and run on the evaluation machine at [OPTIL.io](http://www.optil.io). The system supports most popular programming languages such as C, C++, Java, and Python;  implementations must use only a single CPU thread. The submission is done via the [OPTIL.io](http://www.optil.io). Implementations can be submitted once every 48 hours, and will be tested on the 100 public instances and the 100 hidden instances. The results on the hidden instances are visible only to the Track B committee. A current leaderboard for the results on the hidden instances will be published once per week on this website. To test compatibility with the [OPTIL.io](http://www.optil.io) system, there is also an unlimited ‘lite’ version of the problem which runs the program on fewer public instances with a time limit of 30 seconds.

- [Track B, public and hidden instances](https://www.optil.io/optilion/problem/3009)
- [Track B, lite version with some public instances](https://www.optil.io/optilion/problem/3010)

Implementations must be command-line programs which receive the graph on standard input and write the solution to standard output. Each implementation should be accompanied by a short description of the fixed-parameter algorithm either in plain text format or as a pdf.

**Input Format.** The graph format is a simple text format, where each line describes one edge, given by its two endpoints separated by whitespace, e.g.:

    ml mr
    l1 ml
    l2 ml
    l1 l2
    r1 mr
    r2 mr
    r1 r2

Vertex names can be any combination of letters, digits, and \_. Lines starting with ‘\#’ are comments. Note that this graph format cannot describe degree-0 vertices (which are irrelevant for Minimum Fill-In anyway).

**Output Format.** The output is a minimum-size fill-in set, with one edge per line, e.g.:

    l1 r1
    r2 ml

If the algorithm is randomized, the program must additionally accept a command line argument of the form “-s X”, where X is a 32-bit random seed as decimal number, and must yield reproducible results for the same seed.

**Notes and Hints.** The instances are selected to be challenging. It is expected that an initial implementation will only solve a few of them, and even the winning entry might solve only a minority.
