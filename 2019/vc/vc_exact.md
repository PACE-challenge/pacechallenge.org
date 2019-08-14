---
layout: page
title: PACE 2019 (Track Vertex Cover/Exact)
sidebar_link: false
sidebar_sort_order: 7
---

## Exact 1a. Vertex Cover/Exact
### Requirement: 
The vertex cover has to be optimal, i.e., of smallest size. 

### Description:
We anticipate submissions to be based on a provably optimal algorithm, although we do not make this a formal requirement. 
Instead, if your submission halts on some instance within the allotted time and *produces a solution* that is *known* to be **non-optimal**, the submission will be **disqualified**. 
We also do not prescribe the algorithmic paradigm that is to be used; if a SAT or SMT-solver based submission consistently outperforms more direct approaches, this will be valuable information.

### Instances

Download: 
- [**Download (Updated: March 05, 2019) Public Instances (Exact)**](/files/pace2019-vc-exact-public-v2.tar.bz2)
- [Download Public + Private Instances (Exact)](https://doi.org/10.5281/zenodo.3354609)

There are 200 benchmark instances, labeled vc-exact_001.hgr to vc-exact_200.hgr. 

 
Larger numbers in the filename should (as a rule of thumb) correspond to harder instances. The odd instances are public and the even instances will be provided later (secret). 

For verification purposes, we also publish the sha1sum of the public archive:

SHA1 sum | filename 
--- | --- 
e7ca305528a0257235a95c41742f2b3431e1e485  | pace2019-vc-exact-public-v2.tar.bz2

For individual files we refer to [Download SHA1 sums](/files/pace2019-vc-exact-public-shasums-v2.txt)

### Evaluation 
- timeout: 30 minutes per instance
- measure: tba; but likely PAR-10, where timed-out runs are counted as 10 times the given timeout time.
- objective: minimize the measure
