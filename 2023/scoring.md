---
layout: page 
title: "PACE 2023 - Scoring Methods"
---

Submissions will be ranked by the following methods. In both tracks,
if the output of your program turns out to be not a valid contraction
sequence, your program will be disqualified. Furthermore, your
submission will be disqualified from the exact track if a non-optimal
solution is output.

## Exact Track

You will be ranked by the <em style="color:#db8a00">number of solved instances</em>.
In case of a tie, the winner is determined by the time required to process all instances.

## Heuristic Track

You will be ranked by the <em style="color:#db8a00">geometric mean
over all instances</em> of `100 × (PC solution size) / (your solution
size)`. Here, `(your solution size)` is the size of the solution returned
by your submission and `(PC solution size)` is the size of the
smallest solution known to the PC *(which may not be optimal)*.  

## Technical Notes on Optil.io

Note that the [optil.io](https://www.optil.io) platform ranking differs here
slightly due to technical reasons: On optil.io if the output of your
program turns out to be invalid, it will use `|V|`.  If your program
does not return an output on SIGKILL for some instance, (solution
size) for the instance will be considered as `|V|`.


