# PACE 2026: Instance selection

The PACE 2026 benchmark is built from a collection of instance generators
and data sources. The goal is not to represent a single model of phylogenetic
data, but to obtain a diverse benchmark that triggers different algorithmic ideas
across the exact, heuristic, and lower-bound tracks.

To do this, we first generate a large pool of candidate instances from several
sources. We then score these candidates using a portfolio of solvers and select
instances that are relevant for the competition: instances that are small enough
to be realistic, diverse enough to avoid overfitting to one model, and difficult
enough to identify strong solvers.

## Data Sources

All tracks use a mix of data sources. The main sources are TreeHub, SimPhy, 
regraft-based random generation, and a composition method we refer to as 
Frankenstein instances.

### TreeHub

[TreeHub](https://www.scidb.cn/en/detail?dataSetId=7d2647fc4ce84af5a3f98d22022c6519)
[(Wu et al.)](https://doi.org/10.1038/s41597-025-05282-4) is a large database
of phylogenetic trees. We use TreeHub to construct instances by combining
different trees with the same set of leaf labels. This provides instances that
are grounded in existing phylogenetic data rather than being fully synthetic.

### SimPhy

[SimPhy](https://github.com/adamallo/SimPhy)
[(Mallo et al.)](https://doi.org/10.1093/sysbio/syv082) is a simulator for gene
family evolution. We use several SimPhy profiles to mimic different biological
settings with various mutation rates, including mammals, fish, and bacteria.
In addition to these biologically motivated profiles, we also use more pathological
parameter choices to generate harder artificial instances.

### Regraft Instances

The regraft generator is an artificial model that builds instances by repeatedly
modifying trees. The two main operations are:

- **Regraft:** remove a subtree and insert it at a random position.
- **Leaf swap:** swap leaf labels without otherwise changing the topology.

This model gives us fine control over the amount and type of disagreement
between trees.

### Frankenstein Instances

Frankenstein instances are built by composing existing instances (with known optimal solution).
Given a set of instances, we merge them by replacing leaves in one instance with another
instance. This is mainly used to construct larger instances that contain hard
kernels inherited from smaller examples while maintaining reasonable upper bounds
on the solution size.

## Selecting the Public Instances

The public instance set is selected from a much larger database of generated
candidates (> 50k). We evaluate each candidate and score it for relevance. The
scoring is based in part on the behavior of five solvers implemented by the PC
that use different algorithmic techniques, giving us a proxy for how difficult
an instance is likely to be for competition submissions.

Several criteria guide the selection:

- Each generation model contributes a significant fraction of the final dataset.
- Smaller instances are generally preferred.
- A few larger instances are included, but the benchmark mostly stays within
  sizes that can be expected in biological applications.
- Instances with long running times for one or more solvers are prioritized.
- Instances where heuristic solvers produce poor approximation ratios are
  considered especially useful.

After the first selection round, it became clear that we had overestimated the
difficulty of most instances. We therefore repeat the same general selection
process with improved solvers and higher running-time limits to obtain harder
instances.

## Best-Known Scores

The minimum MAF sizes are relevant for judging correctness in the exact and
lower-bound tracks, as well as for scoring the heuristic track. For most
instances, submitted solvers are strong enough to compute exact solutions in a 
practical time budget. For the remaining instances, we use either upper bounds 
recorded during the construction process, by retracing the regraft and
Frankenstein models, or heuristic solutions.

## Slack in the Lower-Bound Track

For the lower-bound track, the slack of the approximation line
`#a param_a param_b` is generally chosen as a function of the approximation
ratios observed during instance evaluation.

The instances are grouped into several slack categories:

- Instances where trivial solutions are already good enough and the main task is
  to prove a matching lower bound.
- Instances where existing heuristics are good enough and the main task is again
  to prove a lower bound.
- Instances where non-trivial solutions are needed in addition to strong lower
  bounds.

This allows the lower-bound track to include both proof-oriented instances and
instances where finding a good solution is itself part of the challenge.

## Constructing the Final Benchmark

Before receiving the submissions, we curate three sets of instances for each
track:

- **Set A:** 150 public instances.
- **Set B:** 200 private instances generated with the same scoring system.
- **Set C:** a larger pool of generally hard instances. This pool contains
  1,000 instances for the exact and lower-bound tracks and 9,000 instances for
  the heuristic track.

Set C is used to adapt the final benchmark to the submitted solvers by selecting
difficult instances. No new instances were generate after teams submitted their solvers.
We run the submitted solvers under competition conditions, using the official timeouts,
compute resources, and memory limits. Among the solved instances, we select the 
five (lower bound: ten) worst-performing instances for each solver:

- For the exact track, worst performance means longest running time.
- For the heuristic and lower-bound tracks, worst performance means lowest
  score.

The number of selected instances obtained from Set C differs between tracks,
because the number of submitted solvers differs and because some solvers may
struggle on the same hard instances.

The final benchmark for each track is then constructed as follows:

1. Include all public instances from Set A.
2. Include all selected hard instances from Set C.
3. Add enough instances from Set B to obtain exactly 400 instances.

This produces a 400-instance benchmark for each track, out of which more than 300 
were selected before we received the submissions.
