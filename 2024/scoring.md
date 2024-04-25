---
layout: page 
title: "PACE 2024 - Scoring Methods"
---

Submissions will be ranked by the following methods. In all tracks,
if the output of your program turns out to be not a valid contraction
sequence, your program will be disqualified. Furthermore, your
submission will be disqualified from the exact and parameterized track 
if a non-optimal solution is output.

## Exact Track & Parameterized Track

You will be ranked by the <em style="color:#db8a00">number of solved instances</em>.
In case of a tie, the winner is determined by 
the total time spent on the
<em>solved</em> instances. In particular, there is no need to abort a
"hopeless" run early.

## Heuristic Track

You will be ranked by the <em style="color:#db8a00">sum
over all instances</em> of `(PC #crossings) / (your #crossings)`. 
Here, `(your #crossings)` is the number of crossings in
your submission and `(PC #crossings)` is the number of crossings in
the best solution known to the PC 
*(which may not be optimal and may decrease in the course of the contest)*.  

If there is a crossing-free solution, then you receive 1 point if you find
it and 0 points if your solution has crossings.

Note that the [optil.io](https://www.optil.io) platform ranking differs here,
as we cannot input a custom scoring function. On optil.io, the best solution
gets a score of 1, the worst solution a score of 0, and there's a linear score
scale for solutions with a crossing number between these values. The correct
score can be seen on the [results](../results) page.

## Final Score

Since the hardware on optil.io is not reliable and can provide different results
upon uploading the same solver, we will compute the final score on our own hardware.
Note that this hardware is slightly stronger than the one on optil.io:
They use [Intel(R) Xeon(R) CPU E5-2695 v3 computing cores at 2.30GHz](https://www.optil.io/optilion/environment),
while we will use Intel(R) Xeon(R) Gold CPU 6342 computing cores at 2.80GHz.

