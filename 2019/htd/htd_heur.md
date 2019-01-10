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

Download: [Download Public Instances (Heuristic)](/files/pace2019-htd-heur-public.tar.bz2)


There are 100 public benchmark instances, labeled htd-heur_001.hgr, htd-heur_003.hgr, ... to htd-heur_199.hgr. 

 
Larger numbers in the filename should (as a rule of thumb) correspond to harder instances. The odd instances are public and the even instances will be provided later (secret). 

For verification purposes, we also publish the sha1sum of the public archives:

SHA1 sum | filename 
--- | --- 
ee40ca1fb10f8d27b5780175a1cd4eb9cbf2eea2   | pace2019-htd-heur-public.tar.bz2

### Evaluation 
- timeout: 30 minutes per instance
- measure: tba; but likely PAR-10, where timed-out runs are counted as 10 times the given timeout time.
- objective: minimize the measure
