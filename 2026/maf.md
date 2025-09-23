---
layout: page 
title: "PACE 2026 - (rooted) Maximum-Agreement Forest"
---

## Maximum-Agreement Forest

The challenge problem for this year is (rooted) **Maximum-Agreement Forest**:

**Input:** A list of phylogenetic trees on the same leaf-set $X$ <br/>
**Output:** An agreement forest for all input trees with a minimum number of trees

### What is a phylogenetic tree?

A _phylogenetic tree_ $T$ is a tree whose edges are directed away from the unique _root_. Its sinks/leaves (vertices with out-degree zero) are bijectively labelled with a set $X$ (for simplicity, it is often assumed that $X$ **is** the set of leaves of $T$).

### What is an agreement-forest?

An _agreement forest_ of a set of trees $T_1$, $T_2$, $\ldots$ on the same set $X$ of leaves (leaf-labels) is a forest $F$ of phylogenetic trees whose leaf-set is $X$ such that $F$ can be obtained from each $T_i$ by first removing directed edges and then exhaustively contracting vertices that are not in $X$ but have in- and out-degree at most one ("cleanup").

![Example](/2026/img/example_MAF.png)

It is worth to note that a maximum-agreement forest for two phylogenetic trees $T_1$ and $T_2$ contains exactly one more tree than the so-called "rooted subtree prune and regraft" (SPR) distance between $T_1$ and $T_2$. Formally, the distance is defined as the smallest number of "SPR-moves" necessary to turn $T_1$ into $T_2$ (or vice versa -- the distance is a metric), where an SPR-move consist of removing any edge $uv$, subdividing any edge $xy$ of the weak component of $u$ with a new vertex $z$, contracting $u$ and adding the edge $zv$.
Results for computing the rooted SPR-distance are often applicable for computing MAFs **for two trees**.

### Complexity

Deciding whether two rooted binary trees on $n$ leaves have an agreement forest with $k$ trees is known to be NP-complete.
However, this problem can be solved in $O^*(2.35^k)$ time and there is a kernel with $28k$ leaves.
It also admits a polynomial-time 2-approximation algorithm.
If the input consists of $t>2$ trees, then the problem can be solved in $O(3^knt)$ time or $O*2.42^kn^4t^3)$ time.
Structural parameters have not been explored for either case.

## Verifier and test set
A verifier with a small test set will be made available.

## Public instances
Public instances will be made available.


## Tracks

### Exact Track

The task is to compute an optimal agreement forest for the given phylogenetic trees. For each instance, the solver has to output a solution within a time limit of $x$ minutes and a memory limit of $y$ GB ($x$ and $y$ to be determined).

Instances in this track will come with precomputed parameter values and proofs (i.e. decompositions of certain width).
We will take requests for parameters to be included in this list.

Submissions should be based on provably optimal algorithms. Submissions that output an incorrect solution or a solution that is known to be non-optimal will be disqualified. Besides dedicated algorithms, we also encourage submissions based on other paradigms such as SAT, MaxSAT, or ILPs. We allow the use of non-commercial SAT solvers and ILP solvers provided they are not subject to licenses that restrict the free distribution of your solvers.

### Heuristic Track

In this track, the solver shall compute a good solution quickly. The solver will be run on each instance for a short time with limited memory. After this time, the solver receives the Unix signal SIGTERM. When receiving this signal, the process has to output a solution to the standard output and terminate. 
If the program does not halt in a reasonable time after receiving the signal, it will be stopped via SIGKILL. In this case, the instance is counted as "time limit exceeded". 

For this track, solutions do not have to be optimal. However, solvers that produce an incorrect solution will still be disqualified.

### Lower-Bound Track

The goal of this track is to encourage research on good lower bounds. The idea is that good lower bound allow solvers to determine early that a solution is "good enough" to be within some radius of the optimum. Only solutions within a fixed radius will be considered valid and valid solutions will be scored by their running time.


### Final Evaluation
The final score will be computed over a set of $x$ private instances that are similar to the public instances.


## Input and Output

### Input Format

We use the standard [[Newick format]](https://en.wikipedia.org/wiki/Newick_format) for phylogenetic trees.

Each tree is represented by a valid parenthesis-expression. Each internal vertex $u$ of the tree is represented by the expression $(E_1,E_2,\ldots,E_d)$ where each $E_i$ is an expression for the subtree rooted at the $i$'th child of $u$. Each leaf of the tree is represented by its label. The whole expression is terminated with a semi-colon.

The two trees above can be represented as follows:
```
(((E,F),(C,D)),(A,B));
(((((D,B),A),E),C),F);
```

### Output Format
The output format is the same as the input format, but consisting of $k$ phylogenetic trees whose leaf-labels are a partition of the leaf-labels of each input tree.

The solution for the example above could be the following:
```
(F,E);
D;
C;
(A,B);
```

## Literature

- M. Bordewich, C. Semple (2005). On the Computational Complexity of the Rooted Subtree Prune and Regraft Distance. Ann. Comb. 8. [DOI](https://doi.org/10.1007/s00026-004-0229-z)
- C. Semple, M. Steel (2003). Phylogenetics. Oxford University Press. [Publisher](https://global.oup.com/academic/product/phylogenetics-9780198509424)
- D. H. Huson, R. Rupp, C. Scornavacca (2011). Phylogenetic Networks. Cambridge University Press. [DOI](https://doi.org/10.1017/CBO9780511974076)
- C. Whidden, N. Zeh, (2009). A Unifying View on Approximation and FPT of Agreement Forests. Algorithms in Bioinformatics. WABI 2009. LNCS, vol 5724. [DOI](https://doi.org/10.1007/978-3-642-04241-6_32)
- C. Whidden, R. G. Beiko, N. Zeh (2013). Fixed-Parameter Algorithms for Maximum Agreement Forests. SIAM J. Comput. 42(4). [DOI](https://doi.org/10.1137/110845045)
- Z. Chen, Y. Harada, Y. Nakamura, L. Wang (2020). Faster Exact Computation of rSPR Distance via Better Approximation. IEEE/ACM Trans. Comput. Biol. Bioinform. 17(3). [DOI](https://doi.org/10.1109/TCBB.2018.2878731).
- C. Widden (2013). Efficient Computation and Application of Maximum Agreement Forests. PhD Thesis. Dalhousie Univeristy. [PDF](https://dalspace.library.dal.ca/bitstreams/3b246ff4-5ec2-452f-95ab-ef1aed255373/download)
- F. Shi, J. Wang, J. Chen, Q. Feng, J. Guo (2014). Algorithms for parameterized maximum agreement forest problem on multiple trees. Computing and Combinatorics 554. [DOI](https://doi.org/10.1016/j.tcs.2013.12.025)
- F. Shi, J. Chen, Q. Feng, J. Wang (2018). A parameterized algorithm for the Maximum Agreement Forest problem on multiple rooted multifurcating trees. Journal of Computer and System Sciences 97. [DOI](https://doi.org/10.1016/j.jcss.2018.03.002)
- N. Olver, F. Schalekamp, S. van der Ster, L. Stougie, A. van Zuylen (2023). A duality based 2-approximation algorithm for maximum agreement forest. Math. Program. 198. [DOI](https://doi.org/10.1007/s10107-022-01790-y)
- L. Bulteau, M. Weller (2019). Parameterized Algorithms in Bioinformatics: An Overview. Algorithms 12(12). [DOI](https://doi.org/10.3390/a12120256)
