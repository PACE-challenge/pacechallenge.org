---
layout: page
title: "PACE 2022 - Directed Feedback Vertex Set"
---

The Directed Feedback Vertex Set Problem is defined as follows:

**Input:** A directed graph $G = (V, E)$ and a positive integer $k$. <br/>
**Output:** Is there a subset $X \subseteq V$ with $|X| \leq k$ such that, when all vertices of $X$ and their adjacent edges are deleted from $F$, the remainder is cycle-free?

Thus a feedback vertex set of a graph is a set of vertices whose deletion leaves a graph cycle-free.

### Example

<img src="/2022/img/example.png" alt="example" style="width:200px;"/>
<img src="/2022/img/exampleremoved.png" alt="exampleremoved" style="width:200px;"/>

<!--![Example](/2022/img/example.png =200x)-->

In this example, deleting/removing the red vertex and its edges leaves the remaining graph without any cycles.


