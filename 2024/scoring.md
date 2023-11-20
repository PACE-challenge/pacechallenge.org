---
layout: page 
title: "PACE 2024 - Scoring Methods"
---

Submissions will be ranked by the following methods. In both tracks,
if the output of your program turns out to be not a valid contraction
sequence, your program will be disqualified. Furthermore, your
submission will be disqualified from the exact track if a non-optimal
solution is output.

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

