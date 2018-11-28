---
layout: page
title: PACE 2019 (Track Hypertreewidth)
sidebar_link: false
sidebar_sort_order: 6
---

## Hypertree Width 
Given:
A hypergraph.

Task:
Output a hypertree decomposition.


#### What is a hypertree decompositon?


A _hypergraph_ is a pair $H=(V(H),E(H))$, consisting of a set
$V(H)$ of _vertices_ and a set $E(H)$ of _hyperedges_, each
hyperedge being a subset of $V(H)$. 


A _tree decomposition_ of a hypergraph $H=(V,E)$ is a pair
$\mathcal{T}=(T,\chi)$ where $T=(V(T),E(T))$ is a tree and $\chi$ is a mapping
that assigns each $t\in V(T)$ a set $\chi(t)\subseteq V$ (called
the _bag_ at $t$) such that
the following properties hold:

1) for each $v\in V$ there is some  $t\in V(T)$ with $v\in \chi(t)$
  (_$v$ is covered by $t$_),

2) for each $e\in E$ there is some  $t\in V(T)$ with $e \subseteq
  \chi(t)$   (_$e$ is covered by $t$_),

3) for any three $t_1,t_2, t' \in V(T)$ where $t'$ lies on the path
  between $t_1$ and $t_2$, we have
  $\chi(t')\subseteq \chi(t_1)\cap \chi(t_2)$ (_bags containing the
  same vertex are connected_).


Consider a hypergraph $H=(V,E)$ and a set $S\subseteq V$. An
_edge cover_ of $S$ is a set $F\subseteq E$ such that for every
$v\in S$ there is some $e\in F$ with $v\in e$.

A _generalized hypertree decomposition_ of $H$ is a triple
$\mathcal{G}=(T,\chi,\lambda)$ where $(T,\chi)$ is a tree decomposition of
$H$ and $\lambda$ is a mapping that assigns each $t\in V(T)$ an
_edge cover_ $\lambda(t)$ of $\chi(t)$. The _width_ of
$\mathcal{G}$ is the size of a largest edge cover $\lambda(t)$ over all
$t\in V(T)$. A __hypertree decomposition__ is a generalized
hypertree decomposition that satisfies the following additional property:
for every $n \in V(T)$ and every $h \in \lambda(n)$, we have $h \cap \chi^+(n) \subseteq \chi(n)$, 
where $T_n$ denotes the subtree of $T$ rooted at $n$, and $\chi^+(n)$ the set of all vertices
occuring in the $\chi$ labeling of the subtree $T_n$ (_special condition or Decendant Condition_). 

  
  The _hypertree width_ $htw(H)$ is the smallest width over all hypertree
decompositions of $H$.


We refer to [[GottlobGrecoScarcello02]](https://www.sciencedirect.com/science/article/pii/S0022000001918094).


### Input format

See [Details](htd_format)

### Tracks
2a. [Exact Track](htd_exact)
    
2b. [Heuristic Track](htd_heur)

### Literature


[[GottlobGrecoScarcello02](https://www.sciencedirect.com/science/article/pii/S0022000001918094):
 Georg Gottlob, Nicola Leone, Francesco Scarcello. 
 Hypertree Decompositions and Tractable Queries. Journal of Computer and System Sciences. Elsevier. 2002.


[[GottlobGrecoScarcello09](https://www.mat.unical.it/~ggreco/files/GottlobGrecoScarcello.pdf)]: 
Georg Gottlob, Gianluigi Greco, and Francesco Scarcello. Treewidth and Hypertree Width. ICALP'09.

[[FischEtAl18](https://arxiv.org/abs/1611.01090)]:  
Wolfgang Fischl, Georg Gottlob, Reinhard Pichler. General and Fractional Hypertree Decompositions: Hard and Easy Cases. CoRR 1611.01090.
 




