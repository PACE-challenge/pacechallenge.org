---
layout: page
title: PACE 2019
---

## Problems
1. [Vertex Cover](vc/index)
2. [Hypertree Width](htd/index)

## Outcomes
- [Report](https://doi.org/10.4230/LIPIcs.IPEC.2019.25) published in the IPEC proceedings
- [Slides](https://pacechallenge.org/files/PACE19-slides.pdf) presented at IPEC 2019

## Preliminary Results
1a. Vertex Cover:
1. [WeGotYouCovered](https://github.com/sebalamm/pace-2019/releases/tag/pace-2019)  [[doi:10.5281/zenodo.2816116](https://doi.org/10.5281/zenodo.2816116)] (87 solved)
2. [peaty](https://github.com/jamestrimble/peaty) [[doi:10.5281/zenodo.308235](https://doi.org/10.5281/zenodo.3082356)] (77 solved)
3. [bogdan](https://github.com/zbogdan/pace-2019) [[doi:10.5281/zenodo.3228802](https://zenodo.org/badge/latestdoi/185278234)] (76 solved)

2a. Hypertree Width Exact
1. [asc](https://github.com/ASchidler/frasmt_pace) [[doi:10.5281/zenodo.3236333](https://zenodo.org/record/3236333#.XScU2yaxU5k)]
2. [TULongo](https://github.com/TULongo/pace-2019-HD-exact) [[doi:10.5281/zenodo.3236358
](https://zenodo.org/record/3236358#.XScTYS2ZM_M)]
3. [heidi](https://github.com/jamestrimble/heidi) [[doi:10.5281/zenodo.3237427](https://doi.org/10.5281/zenodo.3237427)]

2b. Hypertree Width Heuristic

| Rank | Score  | Solver                                                                        | doi                                                                               | Solved    | PAR1      | cumwidth | cumdiff| 1st vs 2nd |  
| ---  | ---:   | ---                                                                           |:---:                                                                              | ---:      | ---:      | ---:     | ---:| ---:       |
| -    |        |Judge: [htdecomp](https://www.dbai.tuwien.ac.at/proj/hypertree/downloads.html) |                                                                                   |100        | -         | 603      | |-          |
| 1    |   5.0  |[hypebeast](https://github.com/jamestrimble/hypebeast)                             | [[doi:10.5281/zenodo.3082314](https://doi.org/10.5281/zenodo.3082314)]    |100        | 430.5     | 1104     | 501 |0          | 
| 2    |  14.1  |[TULongo](https://github.com/TULongo/pace-2019-HD-Heuristic)                       |  [[doi:10.5281/zenodo.3236369](https://doi.org/10.5281/zenodo.3236369)]   |98         | 8161.2    | 614      | 20 |86         |
| 3    | 128.9  |[asc](https://github.com/ASchidler/frasmt_pace)                                | [[doi:10.5281/zenodo.3236333](https://zenodo.org/record/3236333#.XScU2yaxU5k)]             | 30          | 98995.9  | na      | 11  | na         |


Score: 
(50,000 + wall + 50 * (user_width - judge_with)) /1000000

PAR1:
Cumulated sum of the wall clock 

Cumwidth: 
Solution quality by cumulating the computed widths by summing up over all computed widths

Cumdiff: 
Cumulated difference from the best known value

1st vs. 2nd:
Number of instances where solver X was better than solver Y (TULongo performed better on 86 instances)


## Tracks / Challenges
1a. *Vertex Cover* **Exact**
(Compute a vertex cover of smallest size):
[Details for the track (Exact)](vc/vc_exact); [**Download Instances (Exact, Updated: March 05, 2019)**](/files/pace2019-vc-exact-public-v2.tar.bz2);  [Input Format](vc/vc_format)


2a. *Hypertree Width* **Exact**
 (Compute a hypertree decomposition of hypertree width):
 [Details for the track (Exact)](htd/htd_exact); [Download Instances (Exact)](/files/pace2019-htd-exact-public.tar.bz2); [Input Format](htd/htd_format)    
    
2b. *Hypertree Width* **Heuristic** 
(Compute a decent hypertree decomposition fast):
[Details for the track (Heuristic)](htd/htd_heur); [Download Instances (Heuristic)](/files/pace2019-htd-heur-public.tar.bz2); [Input Format](htd/htd_format)

## Dates

- October 5th, 2018: Announcement of the challenge (Problems)
- November 16th, 2018: Announcement of the tracks and additional informations (input formats and problem feasibility checker are available online)
- December 10th, 2018: Public htd instances are available
- January 7th, 2019: Public vc instances are available
- March 8th, 2019: Leaderboard online (by organizers) and submission *open* for preliminary versions (bugfixing for the authors and initial comparison on public instances)
- May 6nd, 2019 (AOE)  -- Deadline EXTENDED (DS) -- Submission
- **NEW** **June 3rd, 2019 (AOE) -- Deadline EXTENDED (DD) -- Submission** of a **solver description / short abstract** (via Easychair)
- July 1st, 2019: Announcement of the results
- September 11-13, 2019 (International Symposium on Parameterized and Exact Computation ([IPEC 2019](http://fpt.wikidot.com/ipec)) in Munich, Germany)
  - Award ceremony
  - Poster Session (tbd) 

## Submission 
[Submission details](submissions)

## Restrictions
- External Dependencies
   - likely upon request, see [submission details](submissions)
   - please **contact us in time** after optil setup is available


## Evaluation
For details consult the page of the separate tracks.


Then, to participate, you will just upload your code to the platform optil.io as stated on this page. Current leader board on public instances will be live on optil.io. The final ranking will be done on the private instances, using the last valid submission on public instances on optil.io. We kindly ask the participants to send by email to the PC the name of the participants in the team, the name used on optil.io for each track, a link to the public repository as well as a short description of the program and algorithm.



## Program Committee

- [Johannes Fichte](https://iccl.inf.tu-dresden.de/web/Johannes_Fichte) (TU Dresden, Germany)
- [Markus Hecher](https://www.dbai.tuwien.ac.at/staff/hecher/) (TU Vienna, Austria)


## Sponsors


On behalf of the Organization Committee of the 4th PACE Challenge, we invite you to participate in the sponsoring of metals and travel support for PACE-19.


[NETWORKS](http://thenetworkcenter.nl/) already announced sponsoring for PACE 2019. 

<img src="/assets/img/networks-logopartners-lang-rgb-1000px.jpg" alt="NETWORKS logo" style="width: 300px;"/>
