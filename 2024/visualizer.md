---
layout: page 
title: "PACE 2024 - Visualizer"
---

The [visualizer](visualizer.py) can be used to visualize a given instance and solution.

## Usage

To start the visualizer, use the following command:

```console
$ visualizer <path/to/graph.gr> <path/to/solution.sol>
```

The visualizer has three ways to draw the graph:
- Force layout: draw the given instance with a force-directed algorithm.
- Input: draw the given instance in the order provided by the instance file (<path/to/graph.gr>). The fixed partition is displayed at the top, the free partition at the bottom.
- Solution: draw the given instance in the order provided by the solution file (<path/to/solution.sol>). The fixed partition is displayed at the top, the free partition at the bottom.
