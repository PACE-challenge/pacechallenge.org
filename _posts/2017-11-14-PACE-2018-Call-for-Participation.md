---
layout: post
title: "PACE 2018 Call for Participation"
---
The objective of this challenge is to solve the NP-hard graph problem Steiner Tree on undirected edge-weighted graphs:

- **Input:** An undirected edge-weighted graph G, and a set of terminals T subset of V(G).
- **Output:** A tree, subgraph of G, spanning T, which minimizes the sum of its edge-weights.

This problem has been dubbed after the Swiss mathematician Jakob Steiner and has applications in VLSI and network routing, as well as phylogenetic tree reconstruction. Steiner Tree has fixed-parameter algorithms in the number of terminals, and in the treewidth. The first two tracks will explore those two avenues. In a third track, we encourage algorithms without optimum guarantee and preferably (but it is not mandatory) loosely inspired by the FPT literature on Steiner tree problems.

## Tracks

You can participate in any subset of the following tracks:

1.  [**Exact with few terminals**](#track-1-exact-with-few-terminals):
    You have 30 minutes per instance.
    Win by solving more instances than the other participants.
    You want to maximize the number of solved instances. The time to solve them (within the limit of 30 minutes) will only be a factor to break potential ties.
    In all the instances, the number of terminals is relatively small.
2.  [**Exact with low treewidth**](#track-2-exact-on-low-treewidth):
    You have 30 minutes per instance.
    Win by solving more instances than the other participants.
    The same rules as  for the previous track applies, but for this track only, we provide a tree decomposition, and the treewidth is relatively low.
3.  [**Heuristic**](#track-3-heuristic):
    You have 30 minutes per instance.
    Win by printing Steiner trees of smaller weight than the other participants.
    The teams will be ranked by increasing average ratio sol/opt, where sol is the value of your solution and opt is the optimum value (when known) or the best available upper bound (otherwise).

## Prices

PACE 2018 is generously sponsored by [NETWORKS](http://thenetworkcenter.nl/), an NWO Gravitation project of the University of Amsterdam, Eindhoven University of Technology, Leiden University, and the Center for Mathematics and Computer Science (CWI). Through their support, we can hereby announce a total of 4000 euros of sponsoring that will be divided into prizes and travel awards for participants.

## Dates

-   November 14th, 2017: Announcement of the challenge
-   December 11th, 2017: You may start testing your code on optil.io (see [this page](https://pacechallenge.wordpress.com/2017/12/12/optil-io/))
-   **May 1st, 2018, anywhere on earth: Submission** of the final version
-   May 10th, 2018: Announcement of the results
-   August 20-24, 2018: Award ceremony at the International Symposium on Parameterized and Exact Computation ([IPEC 2018](http://algo2018.hiit.fi/ipec/)) in Helsinki

Participants of PACE are highly encouraged to submit manuscripts describing their contributions to publication venues such as IPEC, ESA Track B, and arXiv.org. We also encourage the use of the provided benchmark instances.

## Programme committee

-   [Édouard Bonnet](http://www.lamsade.dauphine.fr/~bonnet/) (Middlesex University, London)
-   [Florian Sikora](http://www.lamsade.dauphine.fr/~sikora/) (LAMSADE, Université Paris Dauphine)
    You can contact us by clicking [here](mailto:edouard.bonnet@lamsade.dauphine.fr,florian.sikora@lamsade.dauphine.fr).

## Steering committee

-   [Holger Dell](https://www.holgerdell.com/) (Saarland University and Cluster of Excellence, MMCI)
-   [Bart M. P. Jansen](https://www.win.tue.nl/~bjansen/) (chair) ( Eindhoven University of Technology)
-   <span style="font-weight:400;">[Thore Husfeldt](http://thorehusfeldt.net/) (ITU Copenhagen and Lund University)</span>
-   <span style="font-weight:400;">[Petteri Kaski](https://users.ics.aalto.fi/pkaski/) (Aalto University)</span>
-   [Christian Komusiewicz](http://users.minet.uni-jena.de/~komusiewicz/) (Philipps-Universität Marburg)
-   [Frances A. Rosamond](http://www.cdu.edu.au/engit/staff-profiles/frances-rosamond) (University of Bergen)

## Submission

For a good dissemination of the implementations, a *submission* is a *source code* hosted in a public repository like [GitHub](https://github.com/), released under an open source license (e.g. [GPL](http://choosealicense.com/licenses/gpl-3.0/), [MIT](http://choosealicense.com/licenses/mit/), or [public domain](https://creativecommons.org/publicdomain/zero/1.0/)); the repository must contain a LICENSE.md or LICENSE.txt file at the root.

Then, to participate, you will just upload your code to the platform [optil.io ](https://www.optil.io/optilion/)as stated on [this page](https://pacechallenge.wordpress.com/2017/12/12/optil-io/). Current leader board on public instances will be live on optil.io. The final ranking will be done on the private instances, using the last valid submission on public instances on optil.io. We kindly ask the participants to send by email to the PC the name of the participants in the team, the name used on optil.io for each track, a link to the public repository as well as a short description of the program and algorithm.

If you want to participate, register now at <https://goo.gl/forms/4mkuCcSjVVkMUZIy1>.

## Track 1: Exact with few terminals

The implementation you submit should compute an optimal Steiner tree of the given graph. We anticipate submissions to be based on a provably optimal algorithm, although we do not make this a formal requirement. Instead, if your submission halts on some instance within the allotted time and produces a solution that is known to be non-optimal, the submission will be disqualified.

There are 200 benchmark instances, labeled instance001.gr to instance200.gr. Larger numbers in the filename should, as a rule of thumb, correspond to harder instances since the instances are ordered lexicographically by increasing (t,m) where t is the number of terminals and m is the number of edges. The odd instances are public and the even instances are secret. You can download the public instances [here](http://www.lamsade.dauphine.fr/~sikora/pace18/exactLowTerm.zip).

Submitted implementations will essentially be executed as follows (reading from standard input, writing to standard output):

    ./st-exact -s 4321 < instanceXYZ.gr > instanceXYZ.ost

If your program is deterministic, it should ignore the option -s 4321; otherwise, this integer between 0 and (2^32)-1 should be used as the initial random seed for your program (and the program should be deterministic if the random seed is given). While your algorithm can use randomness to speed up its computation in expectation, the randomness should be zero-error since we will disqualify any final submission that prints a solution that is non-optimal. The input format is specified in Appendix A and the output format in Appendix B. In Appendix C, we will provide a validity checker.

## Track 2: Exact on low treewidth

It is the same as track 1 except that all instances have low treewidth and a tree decomposition is given in the input file. On almost half of the instances, the provided tree decomposition has guaranteed minimum width. The details on how the decompositions are given can be found in Appendix A. They have been computed thanks to the winning implementations of the previous PACE challenge. Nothing prevents you from re-computing your own tree decomposition.

There are 200 benchmark instances, labeled instance001 to instance200.gr. The instances are ordered lexicographically by increasing (b,m) where b is the maximum bag size of the given tree decomposition and m is the number of edges. The odd instances are public and the even instances are secret. You can download the public instances [here](http://www.lamsade.dauphine.fr/~sikora/pace18/exactLowTw.zip).

### Evaluation and Ranking for the exact tracks

-   We run your submission on the secret instances, for 30 minutes each.
-   If any output produced is invalid or suboptimal, the submission gets disqualified.
-   If your submission solves more instances than the submissions of other participants, you win. As a tie-breaker, we use the running time to rank submissions.

## Track 3: Heuristic

The implementation you submit must compute a Steiner tree of the graph within the allotted time. You don’t need to implement a timer: We will send the Unix signal SIGTERM when the timeout is reached.

There are 200 benchmark instances, labeled instance001 to instance200.gr. The odd instances are public and the even instances are secret. You can download the public instances [here](http://www.lamsade.dauphine.fr/~sikora/pace18/heuristic.zip).

**SIGTERM**: When your process receives this signal, it must immediately print the current best Steiner tree to standard output and then halt. We will send the signal by issuing the following command:

    kill -SIGTERM $pid

To avoid race conditions with other printing operations, your SIGTERM handler should probably only set an atomic flag (see also <http://en.cppreference.com/w/c/program/sig_atomic_t>), which indicates to the rest of your program that it should print a solution as soon as it is safe to do so, and then halt. If the process blocks for too long, say 30 seconds, we will forcefully kill it with SIGKILL. For convenience, we recommend your program handles SIGINT the same way as SIGTERM.

Your program will be executed as follows (reading from standard input, writing to standard output):

    ./st-heuristic -s 4321  < instanceXYZ.gr > instanceXYZ.ost

### Evaluation and Ranking

-   We run your submission on the secret instances, for 30 minutes each.
-   If any output produced is invalid (including a lack of output) the submission gets disqualified.
-   We will rank the teams by increasing mean *approximation ratio*. The approximation ratio will be computed with respect to the optimum (if we know it) or to the best upper bound (otherwise).

## Detailed Submission Requirements for Implementations

**Final implementations must be entirely in source code** and must include automatic build instructions such as a *Makefile* that builds the operating-system executable binary on the target platform. As the sole exception to the entire source code requirement, the use of standard libraries installed on the target platform is permitted. The use of third-party SAT/CSP/ILP solvers is prohibited. For the testing phase on optil.io, please refer to the [optil.io help page](https://www.optil.io/optilion/help) for the requirements (Submitting solution paragraph).

**Input and output formats.** An implementation must conform to the detailed problem-specific format for giving input to and output from an executable binary. Input to an executable binary is given via (a) the command-line parameters, and (b) the standard input. Output from an executable binary is given via the standard output.

**Implementations must be deterministic.** Randomized algorithms are encouraged, but the entropy to the executable binary must be supplied via the command-line parameter “-s 4321”. The only exception to this rule is nondeterministic behavior caused by UNIX signals or querying the time spent/remaining.

All submission must be **single-threaded** (however, wrapper threads forced by limitations of your programming language are fine).

## Appendix A: Graph format

We describe the file format .gr, which is a simplification of  the [STP file format](http://steinlib.zib.de/format.php).

The file starts with a line ‘SECTION Graph’. The next two lines are of the form ‘Nodes \#nodes’ and ‘Edges \#edges’, always in that order, where \#nodes is the number of vertices and \#edges is the number of edges of the graph. The \#edges next lines are of the form ‘E u v w’ where u and v are integers between 1 and \#nodes representing an edge between u and v of weight the positive integer w. The following line reads ‘END’ and finishes the list of edges.

There is then a section Terminals announced by two lines ‘SECTION Terminals’ and ‘Terminals \#terminals’ where \#terminals is the number of terminals. The next \#terminals lines are of the form ‘T u’ where u is an integer from 1 to \#nodes, which means that u is a terminal. Again, the section ends with the line ‘END’.

In Track 1 and 3, the file ends with a subsequent line ‘EOF’. Here is an example of a small graph.

    SECTION Graph
    Nodes 5
    Edges 6
    E 1 2 1
    E 1 4 3
    E 3 2 3
    E 2 4 4
    E 3 5 10
    E 4 5 1
    END

    SECTION Terminals
    Terminals 2
    T 2
    T 4
    END

    [SECTION Tree Decomposition  \\only in instances of Track 2 
    ...
    END]

    EOF

In Track 2, we append a section tree decomposition starting with a line ‘SECTION Tree decomposition’ and ending with a line ‘END’. The lines in the scope of this section follows the format of the output of the treewidth tracks of PACE 2016 and PACE 2017.

For completeness, we reproduce the relevant paragraphs below.

Recall the definition of a tree decomposition of a graph G: It is a tree T such that every vertex x in V(T) has an associated bag B(x) that is a subset of V(G). Moreover, every edge e in E(G) must be a subset of at least one bag B(x), and for every vertex v in V(G), the set of nodes whose bags contain v induces a connected subtree of T. The width of T is the maximum size of its bags minus one.

We define the file format .td. The first line starts with s, then td, followed by the number N of bags of the tree decomposition, the width of the tree decomposition plus one (i.e., the largest bag size), as well as the number of vertices of the original input graph. The next lines we expect start with b and specify the contents of each bag; for example, b 4 3 4 6 7 specifies that bag number 4 contains the vertices 3, 4, 6, and 7 of the original graph. For every bag i, there must be exactly one line starting with b i. All remaining lines indicate an edge in the tree decomposition, so it must consist of two decimal integers from 1 and N and the graph described this way must be a tree. For example, the following is a suboptimal tree decomposition of the path with four edges.

    c decomposition with 4 bags, width 2, for a graph with 5 vertices
    s td 4 3 5
    b 1 1 2 3
    b 2 2 3 4
    b 3 3 4 5
    b 4
    1 2
    2 3
    2 4

In the instances of the test set, there will be at most one commentary line. When there is a line “c We do not guarantee that this tree decomposition has minimum width.”, the tree decomposition was computed with a top heuristic of PACE 2017 for one hour, and when there is no commentary line, the provided decomposition has minimum width.

## Appendix B: Output Format

The output file (.ost) starts with the line ‘VALUE x’ where x is the weight of the found Steiner tree. The next lines are of the form ‘u v’ where u and v are two vertices of the graph linked by an edge and lists all the edges of the found Steiner tree. Here is a small example.

    VALUE 20
    1 3
    3 5
    7 3
    10 7
    7 22

## Appendix C: Validity checker

A validity checker will test if a given Steiner tree (specified in the .ost file format) is indeed a valid Steiner tree of the input graph (specified in the .gr format) and that its weight corresponds to the value specified on the first line. The validity checker will be used to evaluate whether your submitted implementation computed a correct Steiner tree.
