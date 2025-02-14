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
 - April 2025. Submission via [optil.io](https://optil.io/) opens
 - June 2025. Submission deadline
 - July 2025. Results

## Instances 
Currently, we provide a *preliminary* set of 50 instances for the exact track of the Dominating Set Challenge. Find them on [GitHub](https://github.com/MarioGrobler/PACE2025-instances).

## Evaluation and correctness of exact solvers

This year we will take special efforts to ensure the correctness of the exact solvers. 

- We kindly ask all teams to publish their source code (open source) and make it available to the other teams after submission (on github or a similar platform). 
- With the submission we ask for a sketch of proof of correctness of the solver. 
- Within two weeks after submission the teams may inspect the code of the other teams and point out mistakes or simply provide instances that yield wrong results for these solvers. 
- In a following rebuttal phase of one week the teams may respond, and in close contact with the organizers fix small bugs in the code. Fundamentally wrong solvers will be disqualified. In particular, solvers that are based on heuristics only will be disqualified. 
- We will also verify the solvers against a huge database of smaller random instances. These instances will be made publicly available. 
- The evaluation of the solvers will be based on a set of 100 private instances that are similar to 100 publicly available test instances. 

## Program Committee

- [Sebastian Siebertz](https://www.uni-bremen.de/en/theorie/team/profiles/prof-dr-sebastian-siebertz) (Universität Bremen, chair)
- [Mario Grobler](https://user.informatik.uni-bremen.de/grobler/) (Universität Bremen)