---
layout: page
title: PACE 2019 (Track Hypertree&nbsp;Width/Heuristic)
sidebar_link: false
sidebar_sort_order: 6
---

## Exact 2b. Hypertree Width/Heuristic
### Description
Compute some hypertree decomposition. 

The implementation you submit must compute a hypertree decomposition of the hypergraph within the allotted time. You don’t need to implement a timer: We will send the Unix signal SIGTERM when the timeout is reached. 

But note that we will bump up submissions that find good solutions very fast.


### Evaluation
- timeout: 30 minutes per instance
- measure: tba; probably difference of the solution * 60 + runtime
- objective: minimize the measure


### Instances

Download: [Download Public Exact Instances (Heuristic)](/files/pace2019-htd-exact-public.tar.bz2)


There are 100 public benchmark instances, labeled htd-exact_001.hgr, htd-exact_003.hgr, ... to htd-exact_199.hgr. 

 
Larger numbers in the filename should (as a rule of thumb) correspond to harder instances. The odd instances are public and the even instances will be provided later (secret). 

For verification purposes, we also publish the sha1sum of the public archives:

SHA1 sum | filename 
--- | --- 
 f58cbe066cc5feffc9d9d0683a1b2dd20cb292b9   | pace2019-htd-heur-public.tar 

For individual files we refer to [Download SHA1 sums](/files/pace2019-htd-heur-public-shasums.txt).

Details:
tba

### Evaluation 
- timeout: 30 minutes per instance
- measure: tba; but likely PAR-10, where timed-out runs are counted as 10 times the given timeout time.
- objective: minimize the measure