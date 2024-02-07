---
layout: page 
title: "PACE 2024 - Properties of the Exact Benchmark Set"
---

The public benchmark set for the exact track has the following properties, which may be utilized by the submitted solvers (but doesn't have to).

## Number of Vertices
The minimum number of vertices is $562$, the maximum number is $32691$. The graphs have $4183$ vertices on average.

## Number of Edges
The minimum number of edges is $445$, the maximum number is $32807$. The graphs have $4464$ edges on average.

## Graph Classes
Most graphs (but not all) belong to one of the following families:
- Caterpillar
- Lobster
- Tree
- Star forest
- Treewidth <= 3
- Subdivided wheel
- Circular ladder
- Disk intersection
- Planar

## Crossing numbers
We tried to create instances where the crossing number is not *too* large compared to the number of vertices $n$.
- Instances 1 - 12 have at most $n$ crossings
- Instances 13 - 30 have at least $n$ and at most $10n$ crossings
- Instances 31 - 49 have at least $10n$ and at most $50n$ crossings
- Instances 50 - 65 have at least $50n$ and at most $100n$ crossings
- Instances 66 - 91 have at least $100n$ and at most $200n$ crossings
- Instances 92 - 100 have at least $200n$ and at most $300n$ crossings
