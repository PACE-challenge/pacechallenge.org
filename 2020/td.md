---
title: Treedepth
---

## Treedepth

- **Input:**  A connected undirected graph $G=(V,E)$
- **Output:**  A treedepth decomposition of $G$


#### What is a treedepth decompositon?

Treedepth decomposition has many equivalent definitions. Here we mention two of them.

**Definition 1** 
: A *treedepth decomposition* of a connected graph $G=(V,E)$ is a rooted tree $T=(V,E_T)$ such that every edge of $G$ connects a pair of nodes that have an ancestor-descendant relationship in $T$. 

**Definition 2** 
:  A *treedepth  decomposition* of a connected graph $G=(V,E)$ is every rooted  tree  $T=(V,E_T)$ that can be obtained in the following recursive procedure. If $G$ has one vertex, then $T=G$. Otherwise pick a vertex $v\in V$ as the root of $T$, build a  treedepth  decomposition of each connected component of $G-v$ and add all these decompositions to $T$ by joining their roots to $v$.

**Example**
: ![Example](tdsmall.png)

The *depth* of a tree is the maximum number of nodes in a root-vertex path in the tree. The *treedepth* of $G$ is a minimum depth of a treedepth decomposition of $G$.


## Tracks

 1. **Exact**: Compute a treedepth decomposition of minimum depth. You have 30 minutes per instance.  Contestants are ranked by number of instances solved and time required. Detailed ranking method TBA.
 2.  **Heuristic**: Compute some treedepth decomposition of decent depth. You have 30 minutes per instance. Contestants are ranked by quality of results and time required. Detailed ranking method TBA.

Detailed instructions and public instances will be published later.

## Detailed Submission Requirements for Implementations

TBA

## Appendix A: Input format (for both tracks)

TBA


## Appendix B: Output format and validity checker (for both tracks)

TBA




