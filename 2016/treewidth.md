---
title: "PACE 2016 – Track A: Tree Width"
---

The ambition of this track is to turn *tree width*, a concept that has been tremendously successful in theoretical work, into a practically useful tool. Many algorithms in parameterized complexity rely on the existence of tree decompositions of small width, and yet in practice we don’t have a good understanding for how to actually compute such a decomposition. This has to change.

We offer four ranked challenges in this track: *exact sequential*, *exact parallel*, *heuristic sequential*, and *heuristic parallel*. Individuals and teams submit implementations by making them available in a public github repository, where the code is released under an open source license. The implementations will be executed on a high-end computing platform, and the produced solutions will be validated using the official [validity checker](https://github.com/holgerdell/td-validate/). Submissions will be ranked in each of the four challenges based on their performance. To understand the rules and the expected input-output behavior in detail, please make sure to read this entire page.

We also welcome submissions of interesting *instances *as well as randomized programs that *generate* instances, and we invite participants to submit implementations targeted at a desktop platform or a GPU platform, where implementations may be tested but not ranked.

If you have any questions, comments, or concerns about the tree width challenges, please contact us.

## Registration

In order to register for *tw-exact* or *tw-heuristic*, please send the following information to us:

-   Your name and email address
-   The approximate size of your team, as well as the affiliation of the members of your team
-   Which of the four ranked challenges (exact / heuristic and sequential / parallel) you plan to participate in; in case you want your implementation(s) to be informally tested on the desktop or GPU platform, indicate this as well
-   Whether you have any special needs regarding software packages (we will install any software that is available in the official Debian repositories)

## **Test version**

We require all participating teams to send us a preliminary version of their program **by July 25** to make sure everything compiles and runs properly. You are encouraged to submit a test version earlier; each team can submit up to two test versions before July 25. We will manually run ‘make’ and ‘make test’ on the target machine, and send the output to you. We cannot commit to run any tests that are more involved than this, but we’re happy to answer questions.

## tw-exact: Compute an optimal tree decomposition

The implementation you submit to *tw-exact* should compute an optimal tree decomposition of the given graph. We anticipate submissions to be based on a provably optimal algorithm, although we do not make this a formal requirement. Instead, if your submission halts on some instance within the allotted time and produces a solution that is known to be non-optimal, the submission will be disqualified from *tw-exact*. We also do not prescribe the algorithmic paradigm that is to be used; if a SAT-solver based submission consistently outperforms more direct approaches, this will be valuable information.

The test instances for *tw-exact* are divided into the categories easy (~71%), medium (~8%), hard (~7%), and random (~14%). We anticipate easy instances to be solvable in about one second or less (in a single thread on a laptop), medium instances can take about one minute, and hard instances anything beyond that. The numbers of edges have the following distributional properties: min=20, max=6,561, mean=122, median=48; the maximum number of vertices is 3,282. Half of the archive is public, the other half remains secret until the conclusion of the competition. You can download the public instances at <http://bit.ly/pace16-tw-instances-20160307>.

In the competition, we try to reduce the influence of  I/O by prefetching the instance into RAM, and we record the execution time of each test run (both real and CPU time). Submitted implementations will essentially be executed as follows:

```
./tw-exact -s 4321 < instance1.gr
```

Here and elsewhere, the random seed 4321 can be any integer between 0 and (2^32)-1; if the implementation is deterministic, the random seed can be ignored. The input format is specified in Appendix A and the output format in Appendix B. In Appendix C, we provide an automatic validity checker.

## tw-heuristic: Compute a decent tree decomposition fast

The implementation you submit to *tw-heuristic* must compute a tree decomposition of the graph. The implementation does not have to rely on an approximation algorithm with a provable approximation guarantee.

Your implementation can decide at any point to print the current best tree decomposition and halt. However, we may send the Unix signal SIGTERM before the process ends to abort the process when a timeout is reached. Your implementation does not get told in advance how much time it has.

**SIGTERM**: When your process receives this signal, it must immediately print the current best tree decomposition to standard output and then halt. We will send the signal by issuing the following command:

```
kill -SIGTERM $pid
```

To avoid race conditions with other printing operations, your SIGTERM handler should probably only set an atomic flag (see also [http://en.cppreference.com/w/c/program/sig\_atomic\_t](http://en.cppreference.com/w/c/program/sig_atomic_t)), which indicates to the rest of your program that it should print a tree decomposition as soon as it is safe to do so, and then halt. (If the process blocks for too long, say 100 milliseconds, it will receive SIGKILL)

**SIGINT**: We do not formally require this in the competition, but it could be helpful for users if a SIGINT signal (triggered when the user presses Ctrl+C to abort the process) gets interpreted the same way as SIGTERM.

**Status updates**: Whenever your program would be ready to output a better tree decomposition, it must write this information, together with a timestamp, to standard output in the form of a single, well-formatted comment line. The format is as follows:

```
c status [max_bag_size] [current time]
```

Here, \[max\_bag\_size\] is the size of the largest bag in the current best tree decomposition, and \[current time\] is the current Unix time in milliseconds. In C++, you could use the following:

```
struct timeval tv;
gettimeofday(&tv, NULL);
unsigned long long msSinceEpoch = (unsigned long long)(tv.tv_sec) * 1000
   + (unsigned long long)(tv.tv_usec) / 1000;
std::cout << "c status " << max_bag_size << " " << msSinceEpoch << std::endl;
```

Do not output other lines that start with “c status“.

Our test instances for *tw-heuristic* are also divided into the categories easy (~64%), medium (~21%), hard (~3%), and random (~13%), but the graphs are larger (\#edges: min=20, max=252,490, mean=4,028, median=630; the maximum number of vertices is 34,033). The instances are contained in the same archive as for *tw-exact*.

Analogously to *tw-exact*, your program will be executed as follows:

```
./tw-heuristic -s 4321 < instance2.gr
```

## tw-generate: Generate hard random instances

This experimental antagonistic challenge is to generate hard random instances: Given integers n and k, the goal is to output an n-vertex graph with tree width at most k such that the implementations submitted in *tw-exact* and *tw-heuristic* fail as badly as possible. The input parameters n and k, as well as the random seed, are given as command line parameters in the following manner:

```
./tw-generate -n 200 -k 4 -s 4321
```

The output format is specified in Appendix A.

## tw-instance: Submit Instances

The instances submitted here may be used in future challenges. Ideally, they are computationally challenging and contextually rich—for instance, they have arisen in a concrete industrial challenge, model scientific phenomena, or represent a particularly elegant family of combinatorial structures.

## Submission Requirements for *Implementations*

A submission to tw-exact, tw-heuristic, or tw-generate consists of two parts:

1.  The *source code* of the implementation hosted in a public repository on [GitHub](https://github.com/), released under an open source license (e.g. [MIT](http://choosealicense.com/licenses/mit/), [GPL](http://choosealicense.com/licenses/gpl-3.0/), or [public domain](https://creativecommons.org/publicdomain/zero/1.0/)); the repository must contain a LICENSE.md or LICENSE.txt file at the root.
2.  A 2-page *abstract* outlining the implementation; it must indicate the URL of your repository and the commit id of the submitted revision. The abstract should be sent to us by email. For submissions to tw-exact and tw-heuristic, the abstract must further indicate whether the implementation is sequential or parallel.

Multiple submissions by the same authors (for example, one for each platform) are permitted. All submissions will be evaluated and ranked on the *compute platform. *For exploratory reasons, we also invite submissions to the *desktop* and *GPU* platforms.

**Implementations must be entirely in source code** and must include automatic build instructions such as a *Makefile* that builds the operating-system executable binary on the target platform. As the sole exception to the entire source code requirement, the use of standard libraries installed on the target platform is permitted. Implementations prepared with the C programming language, the C++ programming language, and/or CUDA C are strongly preferred, including the use of microarchitecture-specific instruction set extensions (e.g., via intrinsics or assembly language) tailored towards extreme performance on the target platform.

**Input and output formats.** An implementation must conform to the detailed problem-specific format for giving input to and output from an executable binary. Input to an executable binary is given via (a) the command-line parameters, and (b) the standard input. Output from an executable binary is given via the standard output.

**Implementations must be deterministic.** Randomized algorithms are encouraged, but the entropy to the executable binary must be supplied via the command-line parameter “-s 4321”. To ensure repeatable experiments, repeated executions of the executable binary with identical input must produce identical output. Any variable output from an executable binary subject to nondeterminism, such as running time statistics, must be given via the standard error stream. The only exceptions to this rule are nondeterministic behavior caused by UNIX signals, by parallelism, or by our request to output status updates.

**The abstract.** The abstract must be submitted in Portable Document Format (PDF) and must be at most 2 pages in length (not including the appendix), use 11-point font or larger on A4 or letter paper, with ample margins. Experiments reported in the abstract must be repeatable (preferably script-automated and/or documented in the accompanying github repository or in a detailed appendix to the abstract as appropriate) and must document the detailed, preferably component-by-component, hardware and software installation on any experimental platforms together with the detailed performance measurement conventions used in the experiments. (Cf. the platform descriptions above and the baseline implementation for conformant conventions.) The abstract may include a clearly marked appendix documenting further relevant material that will be consulted at the discretion of the program committee.

## Submission Requirements for *Instances*

A submission to tw-instances consists of two parts:

1.  A public repository on [GitHub](https://github.com/) containing the *instances*, released under an open data license (e.g. [CC0](https://wiki.creativecommons.org/wiki/CC0_use_for_data) or [CC BY](https://wiki.creativecommons.org/wiki/Data_and_CC_licenses)); the repository must contain a LICENSE.md or LICENSE.txt file at the root.
2.  A 2-page *abstract* describing the instances; it must indicate the URL of your repository and the commit id of the submitted revision. The abstract should be sent to us by email.

Instances must conform to the indicated .gr format. All instances included in a submission must correctly parse on the validity checker or the submission risks rejection without any consideration of its merits. The abstract must conform to the same general requirements as an abstract accompanying an implementation.

## Our Evaluation Criteria

Here are the precise rules and our ranking scheme for Track A. Recall that we have four contests: exact sequential, exact parallel, heuristic sequential, and heuristic parallel.

**Ranking**

In the *exact* contests, we evaluate implementations as follows:

-   For each instance separately, we determine a ranking of implementations based on the CPU time (*sequential*) or the wall time (*parallel*)
-   We determine the global ranking using the [Schulze method](https://en.wikipedia.org/wiki/Schulze_method#Comparison_table)

In the *heuristic* contests, we evaluate implementations as follow:

1.  We run each implementation on each instance; when the timeout is reached and the process is still running, we send the SIGTERM Unix signal to it, in which case the current best tree decomposition it has computed so far must be printed to stdout and the process terminated ([more on the expected signal behavior](#tw-heuristic-compute-a-decent-tree-decomposition-fast))
2.  For each instance separately, we determine a ranking of implementations based on the width of the tree decomposition it has printed (smaller is better)
3.  We determine the global ranking of implementations using the [Schulze method](https://en.wikipedia.org/wiki/Schulze_method#Comparison_table)*.*

**Timeouts**

We abort the execution of an implementation after a certain time, depending on the difficulty of the instance (which we determined using our reference implementation). The timeouts will be chosen roughly as follows:

-   1 minute for *easy* instances
-   5 minutes for *medium* instances
-   60 minutes for *hard* instances
-   10 minutes for *random* instances

Your implementation does *not* get told in advance what the timeout will be.

### **Disqualification**

An implementation gets disqualified from a contest if 

1.  it ever prints an invalid tree decomposition
2.  (in the *exact* contests only) it prints a non-optimal tree decomposition 
3.  (in the *sequential* contests only) it ever uses more than one thread

### **Disclaimer**

Since this is the first PACE challenge, we don’t know whether these evaluation rules will work out and make sense. Hence we reserve the right to change any of them after the submission deadline.

## Appendix A: Graph format

We describe the file format .gr, which is similar to the format used by DIMACS challenges. This is the file format that a submission to tw-exact or tw-heuristic receives on its standard input, that a submission to tw-generate must write to its standard output, and that a submission to tw-instances must use.

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

We define the file format .td. This is the file format that a submission to tw-exact and tw-heuristic must write to its standard output. As above, c lines are comments and can occur throughout the file. Instead of a p-line, we now expect a unique solution line s as the first non-comment line, which contains the string td, followed by the number N of bags of the tree decomposition, the width of the tree decomposition plus one (i.e., the largest bag size), as well as the number of vertices of the original input graph. The next non-comment lines we expect start with b and specify the contents of each bag; for example, b 4 3 4 6 7 specifies that bag number 4 contains the vertices 3, 4, 6, and 7 of the original graph. Bags may be empty. For every bag i, there must be exactly one line starting with b i. All remaining non-comment lines indicate an edge in the tree decomposition, so it must consist of two decimal integers from 1 and N where the first integer is smaller than the second, and the graph described this way must be a tree. For example, the following is a suboptimal tree decomposition of the path with four edges.

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

## Appendix D: Competition platforms for the tree width challenge

The main *target platform* is the *compute platform.* If you want your software to be tested on the other two platforms listed below, we may be able to accommodate this. Your Implementation will have exclusive access to the respective machine, so we strongly encourage you to optimize your software for the platform. The platforms are as follows:

-   *Compute platform*. A Dell PowerEdge R920 with four 3.0GHz Intel Xeon E7-8857 v2 CPUs (Haswell microarchitecture, 48 cores, 12 cores/CPU, no HT) and 1.5 TB of main memory (96 x 16 GiB RDIMM). The operating system is Debian jessie with linux 3.18.27.1 and gcc 5.3.1-8. Additional compilers and libraries can be installed as needed; however, we will only install the most recent packages that are available in the official Debian repositories.
-   *Desktop platform*. A Fujitsu Esprimo E920 E90+ with one 3.20-GHz Intel Core i5-4570 CPU (Haswell microarchitecture, 4 cores, 4 cores/CPU) and 16 GiB of main memory (4 × 4 GiB DDR3-1600 Hynix HMT451U6AFR8C-PB).
-   *GPU platform*. The host node for the GPUs is a bullx B715 DLC blade server with two 2.1-GHz Intel Xeon E5-2620v2 CPUs (Ivy Bridge microarchitecture, 12 cores, 6 cores/CPU) and 32 GiB of main memory (8 × 4 GiB DDR3-1600 Samsung M393B5273DH0-CMA). The host and the GPUs are connected by a 16-lane PCI Express 3.0 bus. The node has two NVIDIA Tesla K40t cards, each with one 745-MHz NVIDIA GK110B GPU (Kepler microarchitecture, 2880 cores, 15 SMX, 192 cores/SMX) and 12288 MiB of on-device GDDR5-3004 memory with ECC enabled.

For further reference on target platforms and their programming interfaces:

- <http://www.intel.com/content/www/us/en/architecture-and-technology/64-ia-32-architectures-optimization-manual.html>
- <http://www.intel.com/content/www/us/en/processors/architectures-software-developer-manuals.html>
- <https://software.intel.com/sites/landingpage/IntrinsicsGuide/>
- <https://docs.nvidia.com/cuda/cuda-c-programming-guide/>
- <http://docs.nvidia.com/cuda/parallel-thread-execution/>
