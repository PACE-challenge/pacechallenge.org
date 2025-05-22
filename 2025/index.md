---
layout: page
title: "PACE 2025"
sidebar_link: true
sidebar_sort_order: 10
---

<style media="screen and (max-width:1020px)"> img {display:none;} </style>

## Problems <img src="/2025/img/turtle2.png" width=300 height=300 style="position:absolute; top:50px; right:30px" />

This year features two problems. 
1. [Dominating Set](./ds)
2. [Hitting Set](./hs)

## Timeline

 - September 2024. Announcement of the challenge and tracks
 - October 2024. Definition of input and output formats
 - November 2024. Tiny test set and verifier are provided
 - ~~January 2025~~ February 2025. Release of public instances and details about the benchmark
 - ~~April 2025~~ May 2025. Submission via [optil.io](https://optil.io/) opens
 - **Friday, 13.06.2025, 23:59 AOE** Submission deadline for the solvers
 - **Friday, 20.06.2025, 23:59 AOE** Submission deadline for the solver descriptions
 - **Friday, 27.06.2025, 23:59 AOE** End of the public reviewing phase for the correctness of the solvers (see below)
 - **Sunday, 29.06.2025, 23:59 AOE** Deadline for a declaration if you want to change your solver as a result of the reviewing phase
 - **Friday, 04.07.2025, 23:59 AOE** Final submission deadline
 - July 2025. Results

## Submission Guideline
We ask all participants to publish their codebase and solver description on Github or a similar platform that is publicly available.
The following files are required.
 - A license file at the root containing the license
 - An installation guide at the root that also contains information about external dependencies
 - the codebase
 - the solver description

The deadlines mentioned above apply. Note that changes on the codebase and the solver description after their respective deadlines are prohibited, except for small changes resulting from the reviewing phase in close contact with the organizers.

## Scoring
We will use the following scoring system. For the exact tracks as well the heuristic tracks a maximum of 100 points can be achieved. Note that this system is **not** used on optil.
 - **Exact tracks**: every correctly solved instance awards 1 point. Whenever a solver does not finish an instance in time (time limit exceeded), this instance awards 0 points. If a solver produces an incorrect answer on any instance, it will be disqualified. Solvers achieving the same score will be ranked according to their total runtimes.
 - **Heuristic tracks**: every instance produces a score between 0 and 1. Fix an instance with $n$ vertices and optimal solution $k^\*$. Note that $k^\* < n$ holds for every instance (as all instances have at least a single edge). Let $k$ be the solution produced by a solver and let $u = \min(n, 2\cdot k^*)$. The score for the instance is computed according to the formula
 $$f(k) = \left(\frac{u - k}{u - k^*}\right)^2$$.
 This means that producing an optimal solution yields 1 point, producing a trivial solution or a solution outside factor 2 of the optimal solution yields 0 points, and improving an already good solution is more beneficial than improving a bad solution. The following shows an example where $k^\* = 50$ and $n = 100$.

 ![Scoring](/2025/img/heur.png)

## Preliminary leaderboard on optil
The preliminary leaderboard on [optil](https://optil.io) is now live. You can submit your solvers on this platform and compare your results with the solvers of other participants.
 - The input is provided via the standard input `stdin`, eg `sys.stdin` in Python or `System.in` in Java.
 - Please write your output to the standard output stream, eg by calling `print` in Python or `System.out.print` in Java
 - In addition to the exact and heuristic tracks for this years problems, you will find two "Lite" tracks on optil. These tracks contain only five instances each, their main purpose being to test your solvers on a technical level (does the program compile, do input and output work correctly, etc). Please use these tracks first to ensure that your programs run on the platform, as you can only submit a solver every 12 hours for the full tracks.
 - In case you need external libraries that are not already installed on the platform, please contact the team behind optil directly.

## Instances 
You find the set of public instances on [Github](https://github.com/MarioGrobler/PACE2025-instances).

## Evaluation and correctness of exact solvers

This year we will take special efforts to ensure the correctness of the exact solvers. 

- We kindly ask all teams to publish their source code (open source) and make it available to the other teams after submission (on Github or a similar platform). Shortly after the submission deadline for the solvers (13.06.2025), we provide a list of links for all solvers on this webpage.
- With the submission we ask for a sketch of proof of correctness of the solver. 
- Within two weeks after submission the teams may inspect the code of the other teams and point out mistakes or simply provide instances that yield wrong results for these solvers. The deadline is the 27.06.2025
- In a following rebuttal phase of one week the teams may respond, and in close contact with the organizers fix small bugs in the code. Fundamentally wrong solvers will be disqualified. In particular, solvers that are based on heuristics only will be disqualified. 
In case you want to apply changes, please contact us **latest Sunday, 29.06.2025**. The final deadline for these updates is 04.07.2025.
- We will also verify the solvers against a huge database of smaller random instances. These instances will be made publicly available. 
- The evaluation of the solvers will be based on a set of 100 private instances that are similar to 100 publicly available test instances. 

## FAQ

**Is there a leaderboard for submissions where students are the main contributors?** <br>
Yes. For each problem and track there is a global ranking as well as a student ranking, that is, 8 leaderboards in total.
The student ranking is only eligible for submission where students are the main contributors, for example, teams of student being part of a student project. These student groups may be supervised by non-student people as long as the students are the main contributors. If your submission is eligible for the student ranking, please send a short mail to the [program committee](#program-committee). <br>

**Are external solvers allowed?** <br>
The use of external solvers such as ILP solvers, SAT solvers, etc, is allowed and encouraged, provided they are non-commercial and not subject to licenses that restrict the free distribution of your solvers. <br>

**What are the specs of the machine the final evaluation is done? Are parallel, multi-threaded algorithms allowed?**<br>
For each solver, we provide 16 GB of memory and a single thread, as we believe that the focus of the competition is novel algorithm engineering instead of parallel programming. We encourage all teams to configure their software to be single-threaded to obtain results as representative as possible.<br>

**How many submissions per team are allowed?**<br>
We allow three submission per team. However, we allow exceptions for big students groups. For example, for a student group of 10 people divided into 2 (more or less independent) subgroups of 5 students each, we allow both subgroups to submit three solvers each. However, the ranking will be per team, not per solver. If you are unsure, feel free to contact us.<br>

**Are the private instances similar to the public instances?**<br>
Yes. The private instances have similar structural properties and sizes as the public instances.<br>

If you have further questions feel free to contact us via mail or write a ticket on Github.

## Program Committee

- [Sebastian Siebertz](https://www.uni-bremen.de/en/theorie/team/profiles/prof-dr-sebastian-siebertz) (Universität Bremen, chair)
- [Mario Grobler](https://user.informatik.uni-bremen.de/grobler/) (Universität Bremen)