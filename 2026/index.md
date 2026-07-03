---
layout: page
title: "PACE 2026"
sidebar_link: true
sidebar_sort_order: 10
---

<style media="screen and (max-width:1020px)"> img {display:none;} </style>

## Problem

This year features the [Maximum-Agreement Forest (MAF)](./maf) problem arising in <a href="https://en.wikipedia.org/wiki/Phylogenetics">phylogenetics</a> (the study of evolutionary histories). 

See also the [Format Specification](./format) and the [IPEC'25 Announcement Slides](./announcement_slides.pdf).


## Timeline

 - September 2025: Announcement of the challenge and tracks &#x2705;
 - October 2025: Definition of input and output formats &#x2705;
 - November 2025 (last week): **updated 04. Feb** [Tiny test set](https://pace2026.imada.sdu.dk/datasets/tiny02.tar) &#x2705;
 - December 2025 (early): [Checker](https://github.com/manpen/pace26checker) &#x2705;, [STRIDE tool](https://github.com/manpen/pace26stride) and [STRIDE database](https://pace2026.imada.sdu.dk) &#x2705;, [Rust library](https://crates.io/crates/pace26io) &#x2705; for reading instance are provided
 - ~~January~~ February 2026: Release of public instances and details about the benchmark &#x2705;
 - April 2026: Preliminary leaderboard via [optil.io](https://optil.io/) available &#x2705;

 - Solver submission:  5th July 2026 23:59 AoE, see [guideline](#submission-guidelines), [registration form](https://forms.cloud.microsoft/e/XTcX9jTaut)
 - Solver description: 8th July 2026 23:59 AoE
 - End of the public reviewing phase: 19th July 2026 23:59 AoE
 - Final solver submission (see below): 26th July 2026 23:59 AoE

## Instances 
 - [Tiny example instances](https://pace2026.imada.sdu.dk/datasets/tiny02.tar) (changes only to `summary.pdf`)
 - Public instances for **exact track**. [STRIDE list](https://pace2026.imada.sdu.dk/datasets/pace26_exact_pub_v2.lst), [tar.gz](https://pace2026.imada.sdu.dk/datasets/pace26_exact_pub_v2.tar.gz) **updated 08. May** Added 50 new instances (renamed instances with three digit numbers; the first 100 instances are otherwise unmodified).
 - Public instances for **heuristic track**. [STRIDE list](https://pace2026.imada.sdu.dk/datasets/pace26_heuristic_pub_v2.lst), [tar.gz](https://pace2026.imada.sdu.dk/datasets/pace26_heuristic_pub_v2.tar.gz) **updated 13. May** Added 50 new instances (renamed instances with three digit numbers; the first 100 instances are otherwise unmodified).
 - Public instances for **lower-bound track**. [STRIDE list](https://pace2026.imada.sdu.dk/datasets/pace26_lower_pub_v3.lst), [tar.gz](https://pace2026.imada.sdu.dk/datasets/pace26_lower_pub_v3.tar.gz) **updated 13. May** Added 50 new instances (renamed instances with three digit numbers; the first 100 instances are otherwise unmodified).

## Tools
The following software tools are available. There is **no** requirement to use them:
 - [pace26stride](https://github.com/manpen/pace26stride)
   Solver runner and instance verifier with tight integration of the [STRIDE database](https://pace2026.imada.sdu.dk) (see below).
 - [pace26checker](https://github.com/manpen/pace26checker) (deprecated -- use stride!): 
   This tool implements a small verifier for instances and solutions.
 - [pace26io](https://crates.io/crates/pace26io): 
   A software library implemented in Rust to parse input instances and write solution files.

### STRIDE
[STRIDE is a tool](https://github.com/manpen/pace26stride) that has two main objectives:
 - STRIDE offers a runner that allows you to execute and monitor your solver. 
   You simply provide a set of instances and STRIDE will run your solver (in parallel), monitor its resource usage, verify the solution and provide a machine-readable summary.
 - It is tightly integrated with our [STRIDE instance server](https://pace2026.imada.sdu.dk).
   This server hosts several thousand instances together with solutions provided by the community.
   The majority of instances are small and should be relatively fast to solve;
   we recommend regularly testing your solvers against the database to detect errors and find regressions.
 
   The server also accepts solutions, which are verified, stripped of any metadata, stored, and published after the competition is completed.
   In the meantime, we publish only the best known score for each instance.
   If you are using STRIDE instances, we kindly ask that you upload your solutions (this is the default behavior of the STRIDE runner when solving STRIDE instances).

## Results
No results yet.

## Submission Guideline
We ask all participants to publish their codebase and solver description on Codeberg, Github, Gitlab (et cetera) or a ZIP/TAR archivew; the code needs to be publically accessible without registering with the platform.
We will retrieve the sources shortly after the submission deadline.
The following files are required.
 - A license file at the root containing the license
 - An installation guide at the root that also contains information about external dependencies
 - the codebase
 - the solver description
 - recommended, but not required: `docker_setup.sh` containing all steps necessary to build the solver in a Debian 13.5 container.

**Registration link**: [Registration form](https://forms.cloud.microsoft/e/XTcX9jTaut)

Each team may submit up to three different solvers per track if they are substantially different (i.e. exploit different algorithmic ideas that substantially go beyond 'parameter tweaking').
In this case, please submit one registration per solver and use different solver names.

The deadlines mentioned above apply. Note that changes on the codebase and the solver description after their respective deadlines are prohibited, except for small changes resulting from the reviewing phase in close contact with the organizers.

### Solver Description
Each solver has to be accompanied by a solver description (PDF) that outlines the algorithmic and implementation details.
For the exact and lower-bound tracks, we also ask teams to sketch why the solver is correct (no formal proof is required).

We recommend using the LIPIcs template, as in each track the three best-scoring teams will be invited to include a short-paper in the IPEC 2026 proceedings.
After the official ranking has been published, we will reach out to these teams with submission instructions for these short papers.

The solver description is subject to a page limit of four pages (including the title page and bibliography).
In case of a submission to multiple tracks, a shared description may be submitted; 
in this case, the page limit increases by three pages for each additional track.

To simplify the peer-review phase in July, please make sure to include an email address on the title page where other teams can report issues to you.

## Tracks
The challenge features three distinct tracks:
1. an "exact" track, solving MAF on an arbitrary number of trees -- for this track, the instances come with precomputed values of some parameters (along with proofs, e.g. decompositions of certain width)
2. a "heuristic" track, solving MAF on two trees -- the instances will consist of two large trees and the allotted computation-time will be short
3. a "lower-bound" track, also with two trees per instance -- the aim is to reach an approximate solution quickly

## Scoring
The scoring functions are applied for the final evalution of the submitted solvers.
Please note that the scoring on [optil](https://optil.io) deviates for technical reasons.

### Exact track
Every correctly solved instance awards 1 point. 
Whenever a solver does not finish an instance in time (time + grace limit exceeded), this instance awards 0 points.
If a solver produces an infeasible or suboptimal answer on any instance, it will be disqualified.
Solvers achieving the same score will be ranked according to their total runtimes.

### Lower-bound track
Depending on speed, every correctly solved instance awards between 0.5 and 1 points.
Whenever a solver does not finish an instance in time (time + grace limit exceeded), this instance awards 0 points. 
If a solver produces an infeasible solution or a solution violating its size constraint (see below) on any instance, it will be disqualified.

Suppose that a suitable solution was produced in $t$ seconds in time (timeout of 10min + grace period of 10s). 
Then a score of $(2 - t/610)/2$ is awarded (i.e., 0.5 points for the solution and up to 0.5 points depending on speed).

In contrast to the exact track, suboptimal solutions are acceptable to a certain extend.
Each instance contains an approximation line (`#a`) with two parameters $1 \le a < 1.5$ and $0 \le b$.
Let $k^\*$ be the (unknown) size of an MAF. 
Then, a solver needs to produce a solution of size at most $\lfloor a k^\* \rfloor + b$; 
if a solver produces an infeasible solution or exceeds the instance-specific threshold, the solver will be disqualified.

### Heuristic track
Depending on quality, every correctly solved instance awards between 0 and 1 points. 
Whenever a solver does not finish an instance in time (time +grace limit exceeded), this instance awards 0 points. 
If a solver produces an infeasible solution on any instance, it will be disqualified.

Fix an instance with $n$ leaves, and let $k^\*$ be the best solution size known to the PC.
Note that $k^\* < n$ holds for every instance.
Let $k$ be the solution produced by a solver and let $u = \min(n, 2\cdot k^\*)$.
The score for the instance is calculated according to the formula $$f(k) = \left(\max\left(0, \frac{u - k}{u - k^*}\right)\right)^2.$$
This means that producing an optimal solution yields 1 point, producing a trivial solution or a solution outside factor 2 of the optimal solution yields 0 points, and improving an already good solution is more beneficial than improving a bad solution. 

### Overview

|                        | Exact Track   | Lower-Bound Track                               | Heuristic Track                                                                                                                             |
|------------------------|---------------|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Timeout                |         30min | 10min                                           | 5min                                                                                                                                        | 
| Grace Time             |           10s | 10s                                             | 10s                                                                                                                                         | 
| RAM                    |          8 GB | 8 GB                                            | 8 GB                                                                                                                                        |
| Solution size          | Optimal $k^\*$ | $\le \lfloor a k^\* \rfloor + b$ (see `#a` line) | $\le n$                                                                                                                                     |
| Instance score         | 1 per solved  | $(2 - t/610)/2$ with $t$: runtime (in sec)       | $\left(\max\left(0, [u - k]/[u - k^\*]\right)\right)^2 $ with $k^\*$: best known solution size, $k$: produced size, and $u = \min(n, 2k^\*)$   |


## Evaluation and correctness of exact and lower-bound solvers

This year we will again take special care to ensure the correctness of the exact and lower-bound solvers. 
We provide a large dataset of instances to test against, and highly recommend to [STRIDE](#stride) during development and before submission.
Please make sure your solver treats corner cases, such as empty or edgeless intermediate trees correctly.

Shortly after submission, there will be a peer-review phase:
- We ask all teams to publish their source code (open source) and make it available to the other teams after submission (on Github or a similar platform). Shortly after the submission deadline for the solvers, we provide a list of links for all solvers on this webpage.
- With the submission we ask for a sketch of proof of correctness of the solver. 
- Within two weeks after submission the teams may inspect the code of the other teams and point out mistakes or simply provide instances that yield wrong results for these solvers. 
  This may either happen by contacting other teams directly (e.g., via GitHub issues or eMail) or by contacting the PC.
- In a following rebuttal phase of one week the teams may respond, and in close contact with the organizers fix small bugs in the code. Fundamentally wrong solvers will be disqualified.
  In particular, solvers that cannot guarantee the stated constraints for their respective track will be disqualified.
- We will also verify the solvers against a huge database of smaller random instances. 
- The evaluation of the solvers will be based on a set of 100 private instances that are similar to 100 publicly available test instances. 

## Preliminary leaderboard on optil

A preliminary leaderboard is available on [optil](https://optil.io).
We strongly encourage all teams to submit their solvers.

### Zulip

Join us on [Zulip](https://pacechallenge.zulipchat.com/join/l3eavdfbytkcjiypecpzetuw/) for discussions and updates.


## Program Committee

- [Alexander Leonhardt](https://ae.cs.uni-frankfurt.de/staff/alexander_leonhardt.html) (Goethe-Universität Frankfurt)
- [Manuel Penschuck](https://portal.findresearcher.sdu.dk/en/persons/manuel-penschuck) (University of Southern Denmark, Odense)
- [Mathias Weller](https://igm.univ-mlv.fr/~mweller/) (Université Gustave Eiffel, Paris)
