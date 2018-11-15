---
layout: page
title: PACE 2019 (Track Hypertreewidth/Heuristic)
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

Download: tba

There are 200 benchmark instances, labeled htd-heur_001.hgr to htd-heur_200.hg.. 

 
Larger numbers in the filename should (as a rule of thumb) correspond to harder instances. The odd instances are public and the even instances are secret. 

For verification and precommitment purposes, we also publish the sha1sum of the public and secret archives:

Details:
tba