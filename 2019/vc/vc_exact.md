---
layout: page
title: PACE 2019 (Track Vertex Cover/Exact)
sidebar_link: false
sidebar_sort_order: 7
---

## Exact 2a. Vertex Cover/Exact
### Requirement: 
The vertex cover has to be optimal, i.e., of smallest size. 

### Description:
We anticipate submissions to be based on a provably optimal algorithm, although we do not make this a formal requirement. 
Instead, if your submission halts on some instance within the allotted time and *produces a solution* that is *known* to be **non-optimal**, the submission will be **disqualified**. 
We also do not prescribe the algorithmic paradigm that is to be used; if a SAT or SMT-solver based submission consistently outperforms more direct approaches, this will be valuable information.

### Instances

Download: tba

There are 200 benchmark instances, labeled vc-exact_001.hgr to vc-exact_200.hgr. 

 
Larger numbers in the filename should (as a rule of thumb) correspond to harder instances. The odd instances are public and the even instances are secret. 

For verification and precommitment purposes, we also publish the sha1sum of the public and secret archives:

Details:
tba

### Evaluation 
- timeout: 30 minutes per instance
- measure: tba; but likely PAR-10, where timed-out runs are counted as 10 times the given timeout time.
- objective: minimize the measure