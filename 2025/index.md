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

## Preliminary leaderboard on optil
The preliminary leaderboard on [optil](https://optil.io) is now live. You can submit your solvers on this platform and compare your results with the solvers of other participants.
 - The input is provided via the standard input `stdin`, eg `sys.stdin` in Python or `System.in` in Java.
 - Please write your output to the standard output stream, eg by calling `print` in Python or `System.out.print` in Java
 - In addition to the exact and heuristic tracks for this years problems, you will find two "Lite" tracks on optil. These tracks contain only five instances each, their main prupose being to test your solvers on a technical level (does the program compile, do input and output work correctly, etc). Please use these tracks first to ensure that your programs run on the platform, as you can only submit a solver every 12 hours for the full tracks.
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
The student ranking is only eligible for submission where students are the main contributors, for example, teams of student being part of a student project. These student groups may be supervised by non-student people as long as the students are the main contributors. If your submission is eligible for the student ranking, please send a short mail to the [program committee](#program-committee) <br>

**Are external solvers allowed?** <br>
The use of external solvers such as ILP solvers, SAT solvers, etc, is allowed and encouraged, provided they are non-commercial and not subject to licenses that restrict the free distribution of your solvers. <br>

**What are the specs of the machine the final evaluation is done? Are parallel, multi-threaded algorithms allowed?**<br>
For each solver, we provide 16 GB of memory and a single thread, as we believe that the focus of the competition is novel algorithm engineering instead of parallel programming. We encourage all teams to configure their software to be single-threaded to obtain results as representative as possible.<br>

**Are the private instances similar to the public instances?**<br>
Yes. The private instances have similar structural properties and sizes as the public instances.<br>

If you have further questions feel free to contact us via mail or write a ticket on Github.

## Program Committee

- [Sebastian Siebertz](https://www.uni-bremen.de/en/theorie/team/profiles/prof-dr-sebastian-siebertz) (Universität Bremen, chair)
- [Mario Grobler](https://user.informatik.uni-bremen.de/grobler/) (Universität Bremen)