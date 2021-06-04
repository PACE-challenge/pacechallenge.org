---
title: "PACE 2017 – Track A: Tree Width"
---

The objective of this track is to compute the NP-hard graph parameter *tree width*:

- **Input:** An undirected graph.
- **Output:** A minimum-width [tree-decomposition](https://en.wikipedia.org/wiki/Tree_decomposition) of the graph.

In last year’s PACE, we had some great submissions, but we and many participants also felt that there was plenty of room for improvement, both in terms of the submitted implementations and in terms of the setup of the challenge, which is why we offer it again this year. For example, the instances are much harder than last year.


## Challenges

You can participate in one or both of these challenges:

1.  **Compute a tree-decomposition of minimum width.**
    You have 30 minutes per instance.
    Win by solving more instances than the other participants.
2.  **Compute some tree-decomposition.**
    You have 30 minutes per instance.
    Win by printing solutions of smaller width than the other participants.

All submission must be **single-threaded** (however, wrapper threads forced by limitations of your programming language are fine).


## Submission

A *submission* consists of the *source code* of the implementation hosted in a public repository on [GitHub](https://github.com/), released under an open source license (e.g. [GPL](http://choosealicense.com/licenses/gpl-3.0/), [MIT](http://choosealicense.com/licenses/mit/), or [public domain](https://creativecommons.org/publicdomain/zero/1.0/)); the repository must contain a LICENSE.md or LICENSE.txt file at the root.

If you are thinking about participating, register now at <https://goo.gl/forms/zo0Slq1X6j3fNdxd2>. You will receive an edit link there so that you can submit a preliminary version by **March 1st, 2017** and the final version by **May 1st, 2017**.

Every submission must pass all *automatic tests*. Use this convenient autotester early and often: <https://github.com/holgerdell/td-validate/blob/master/autotest-tw-solver.py>

In March 2017, we will publish a *leaderboard*, that is, a ranking of all preliminary versions that were submitted.


## Challenge 1: Compute an optimal tree decomposition

The implementation you submit should compute an optimal tree decomposition of the given graph. We anticipate submissions to be based on a provably optimal algorithm, although we do not make this a formal requirement. Instead, if your submission halts on some instance within the allotted time and produces a solution that is known to be non-optimal, the submission will be disqualified. We also do not prescribe the algorithmic paradigm that is to be used; if a SAT-solver based submission consistently outperforms more direct approaches, this will be valuable information.

There are 200 benchmark instances, labeled ex001.gr to ex200.gr. Larger numbers in the filename should (as a rule of thumb) correspond to harder instances. The odd instances are public and the even instances are secret. You can download the instances at <https://github.com/PACE-challenge/Treewidth-PACE-2017-instances>. All instances are based on real-world data, but about 50 were boosted in hardness using a natural random process. For verification and precommitment purposes, we also publish the sha1sum of the public and secret archives:

    41659bfd2af78296419468a4dbe7334a9466b437 ex-instances-PACE2017-public-2016-12-02.tar.bz2
    cd14c2eab0eae8415cbc5265a3227ce19c3b8ea5 ex-instances-PACE2017-secret-2016-12-02.tar.bz2

Submitted implementations will essentially be executed as follows:

```
./tw-exact -s 4321 < ex001.gr > ex001.td
```

If your program is deterministic, it should ignore the option -s 4321; otherwise, this integer between 0 and (2^32)-1 should be used as the initial random seed for your program (and the program should be deterministic if the random seed is given). While your algorithm can use randomness to speed up its computation in expectation, the randomness should be zero-error since we will disqualify any final submission that prints a solution that is non-optimal. The input format is specified in Appendix A and the output format in Appendix B. In Appendix C, we provide a validity checker for the file formats, and we also include an automatic tester that checks whether your software produces valid and optimal tree-decompositions on a given database of test graphs:

```
./autotest-tw-solver.py --full /path/to/my/tw-exact
```


### Evaluation and Ranking

-   We run your submission on the secret instances, for 30 minutes each.
-   If any output produced is invalid according to [td-validate](https://github.com/holgerdell/td-validate/) or not optimal, the submission gets disqualified.
-   If your submission solves more instances than the submissions of other participants, you win. As a tie-breaker, we use the running time to rank submissions using the [Schulze method](https://en.wikipedia.org/wiki/Schulze_method#Comparison_table).


## Challenge 2: Compute a decent tree decomposition fast

The implementation you submit must compute a tree decomposition of the graph within the allotted time. <span style="font-weight:400;">You don’t need to implement a timer: We will send the Unix signal SIGTERM when the timeout is reached.</span>

There are 200 benchmark instances, labeled he001.gr to he200.gr. The odd instances are public and the even instances are secret. You can download the instances at <https://github.com/PACE-challenge/Treewidth-PACE-2017-instances> (~1 GB when extracted). For verification and precommitment purposes, we also publish the sha1sum of the public and secret archives:

    4ac30341a54bc0ced46c1294882cd820589b660f  he-instances-PACE2017-public-2016-12-02.tar.bz2
    28e5dd3c67db617076ff50ec3faa68f85e4ac005  he-instances-PACE2017-secret-2016-12-02.tar.bz2

**SIGTERM**<span style="font-weight:400;">: When your process receives this signal, it must immediately print the current best tree decomposition to standard output and then halt. We will send the signal by issuing the following command:</span>

```
kill -SIGTERM $pid
```

<span style="font-weight:400;">To avoid race conditions with other printing operations, your SIGTERM handler should probably only set an atomic flag (see also </span>[<span style="font-weight:400;">http://en.cppreference.com/w/c/program/sig\_atomic\_t</span>](http://en.cppreference.com/w/c/program/sig_atomic_t)<span style="font-weight:400;">), which indicates to the rest of your program that it should print a tree decomposition as soon as it is safe to do so, and then halt. If the process blocks for too long, say 30 seconds, we will forcefully kill it with SIGKILL. For convenience, we recommend your program handles SIGINT the same way as SIGTERM.</span>

Analogously to the *exact* challenge, your program will be executed as follows:

```
./tw-heuristic -s 4321 < he001.gr > he001.td
```


### Evaluation and Ranking

1.  For each instance separately, we rank the implementations based on the width of the valid tree decomposition that they produce after up to 30 minutes.
2.  We combine these rankings into a global ranking of implementations using the [Schulze method](https://en.wikipedia.org/wiki/Schulze_method#Comparison_table)*.*


## Bonus Challenge: Submit Instances

We also welcome the submissions of interesting *instances*, which must be released under an open data license (e.g. [CC0](https://wiki.creativecommons.org/wiki/CC0_use_for_data) or [CC BY](https://wiki.creativecommons.org/wiki/Data_and_CC_licenses)) in a public repository. The license must be indicated in a LICENSE.txt or LICENSE.md file, and the Instances must conform to the indicated .gr format, that is, they must be declared valid by the validity checker.

Submitted instances may be used in future challenges; ideally, they are computationally challenging and contextually rich—for instance, they have arisen in a concrete industrial challenge, model scientific phenomena, or represent a particularly elegant family of combinatorial structures.


## Detailed Submission Requirements for Implementations

**Implementations must be entirely in source code** and must include automatic build instructions such as a *Makefile* that builds the operating-system executable binary on the target platform. As the sole exception to the entire source code requirement, the use of standard libraries installed on the target platform is permitted. If you use any libraries not present in Debian jessie, we encourage you to provide a suitable [Dockerfile](https://docs.docker.com/engine/reference/builder/) as part of your submission (in particular, this applies to [Java 8](https://hub.docker.com/_/java/), [Sage](https://github.com/sagemath/docker-images), and certain versions of [boost](https://hub.docker.com/r/kcyeu/boost/); contact us in case you have problems with this). Implementations prepared with the C programming language, the C++ programming language, and/or CUDA C are strongly preferred, including the use of microarchitecture-specific instruction set extensions (e.g., via intrinsics or assembly language) tailored towards extreme performance on the target platform.

**Input and output formats.** An implementation must conform to the detailed problem-specific format for giving input to and output from an executable binary. Input to an executable binary is given via (a) the command-line parameters, and (b) the standard input. Output from an executable binary is given via the standard output.

**Implementations must be deterministic.** Randomized algorithms are encouraged, but the entropy to the executable binary must be supplied via the command-line parameter “-s 4321”. To ensure repeatable experiments, repeated executions of the executable binary with identical input must produce identical output. Any variable output from an executable binary subject to nondeterminism, such as running time statistics, must be given via the standard error stream. The only exception to this rule is nondeterministic behavior caused by UNIX signals.

**Target platform.** The competition will be carried out on the following platform:

-   *Compute platform*. A Dell PowerEdge R920 with four 3.0GHz Intel Xeon E7-8857 v2 CPUs (Haswell microarchitecture, 48 cores, 12 cores/CPU, no HT) and 1.5 TB of main memory (96 x 16 GiB RDIMM). The operating system is Debian jessie with linux 4.4.30.1.amd64-smp.

For further reference on the target platform and its programming interfaces:

[http://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-optimization-manual.html
](http://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-optimization-manual.html)[http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html
](http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html)<https://software.intel.com/sites/landingpage/IntrinsicsGuide/>


## Appendix A: Graph format

We describe the file format .gr, which is similar to the format used by DIMACS challenges.

Lines are separated by the character ‘\\n’. Each line that starts with the character c is considered to be a comment line. The first non-comment line must be a line starting with p followed by the problem descriptor tw and the number of vertices n and edges m (separated by a single space each time). No other line may start with p. Every other line indicates an edge, and must consist of two decimal integers from 1 to n separated by a space; moreover, graphs are considered undirected (though they may contain isolated vertices, multiple edges, and loops). For example, a path with four edges can be defined as follows:

```
c This file describes a path with five vertices and four edges.
p tw 5 4
1 2
2 3
c we are half-way done with the instance definition.
3 4
4 5
```


## Appendix B: Tree decomposition format

Recall the definition of a tree decomposition of a graph G: It is a tree T such that every vertex x in V(T) has an associated bag B(x) that is a subset of V(G). Every edge e in E(G) must be a subset of at least one bag B(x). Moreover, for every vertex v in V(G), the set of tree vertices whose bags contain v induce a connected subtree of T. The width of T is the maximum size of its bags minus one. The goal is to compute a tree decomposition of minimum width.

We define the file format .td. As above, c lines are comments and can occur throughout the file. Instead of a p-line, we now expect a unique solution line s as the first non-comment line, which contains the string td, followed by the number N of bags of the tree decomposition, the width of the tree decomposition plus one (i.e., the largest bag size), as well as the number of vertices of the original input graph. The next non-comment lines we expect start with b and specify the contents of each bag; for example, b 4 3 4 6 7 specifies that bag number 4 contains the vertices 3, 4, 6, and 7 of the original graph. Bags may be empty. For every bag i, there must be exactly one line starting with b i. All remaining non-comment lines indicate an edge in the tree decomposition, so it must consist of two decimal integers from 1 and N where the first integer is smaller than the second, and the graph described this way must be a tree. For example, the following is a suboptimal tree decomposition of the path with four edges.

```
c This file describes a tree decomposition with 4 bags, width 2, for a graph with 5 vertices
s td 4 3 5
b 1 1 2 3
b 2 2 3 4
b 3 3 4 5
b 4
1 2
2 3
2 4
```


## Appendix C: Validity checker

The validity checker at <https://github.com/holgerdell/td-validate/> verifies that a given tree decomposition (specified in the .td file format) is indeed a valid tree decomposition of a given graph (specified in the .gr format). The validity checker will be used to evaluate whether your submitted implementation computed a correct tree decomposition.
