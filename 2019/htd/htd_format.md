---
layout: page
title: Format - Hypertree decomposition (Draft Updated 2018-12-02)
sidebar_link: false
sidebar_sort_order: 6
---

## Checker
See: [htd_validate](https://github.com/daajoe/htd_validate/tree/pace2019)

## Input Format

### Hypergraph (.hgr)

The hypergraph format extends the PACE2016 and [PACE2017 graph](/2017/treewidth/) format.

Example:

```AsciiDoc
c This file describes a hypergraph in htd PACE2019 format
c with 6 vertices and 4 hyperedges
p htd 6 4
1 1 2 3
2 2 3 4
c this is a comment and will be ignored
3 3 4 5
4 4 5 6
```
Description
* Line separator ‘\n’
* Lines starting with character c are interpreted as comments
* Vertices are consecutively numbered from 1 to n
* Problem description
  * Form "p htd NumVertices NumHyperedges"
    * Line starting with character p 
    * followed by the problem descriptor htd 
    * followed by number of vertices n
    * followed by number of hyperedges m
    * each separated by space each time
  * Unique (No other line may start with p)
  * Has to be the first line (except comments)
* Remaining lines indicate a hyperedge
  * consisting of decimal integers separated by space
  * Starting with an integer that identifies the number of the hyperedge
  * followed by the hyperedge
  * _Line: "1 1 2 3\n" indicates a hyperedge No 1 on vertices 1, 2, and 3_
* Empty lines or lines consisting of spaces may occur and only will be ignored  
* Hypergraphs may contain isolated vertices, multiple hyperedges, and loops


### Hypertree Decomposition Format (.htd)

See: https://arxiv.org/abs/1611.01090 for a compact definition of various hypertree decompositions.

```AsciiDoc
c This file describes a hypertree decomposition
c with 5 bags, width 2 
c for a hypergraph with 5 vertices and 5 hyperedges
s htd 5 2 5 5
b 1 1 2 3
b 2 2 3 4 1
b 3 3 4 5 1 2
b 4 4 5 1 2 3
b 5 5 1 2
2 1
3 2
4 3
5 4
w 1 1 0
w 1 2 0
w 1 3 1
w 1 4 0
w 1 5 1
c
w 2 1 0
w 2 2 0
w 2 3 1
w 2 4 0
w 2 5 1
c
w 3 1 0
w 3 2 0
w 3 3 1
w 3 4 0
w 3 5 1
c
w 4 1 1
w 4 2 0
w 4 3 1
w 4 4 0
w 4 5 0
c
w 5 1 0
w 5 2 0
w 5 3 0
w 5 4 0
w 5 5 1
```

Description
* Line separator ‘\n’
* Lines starting with character c are interpreted as comments
* Vertices are consecutively numbered from 1 to n
* Solution description
  * Form "s htd NumBags Width NumVertices NumHyperedges"
    * Line starting with character s
    * followed by the problem descriptor htd
    * followed by number l of bags
    * followed by the computed width
    * followed by number n of vertices
    * followed by number m of hyperedges
    * each separated by space each time
  * Unique (No other line may start with s)
  * Has to be the first line (except comments)
* Bag description
  * BagIDs run consecutively from 1 to l
  * Form "b BagID Vertex1 Vertex2 Vertex3 ..."
    * Lines starting with character b
    * followed by an identifier of the bag
    * followed by the contents of the bag
    * each separated by space each time
  * Example: "b 4 3 4 6 7"
    * specifies that bag number 4 
    * contains the vertices 3, 4, 6, and 7 of the original hypergraph
  * Bags may be empty
  * Bags can contain at most z many vertices
  * For every bag i, there must be exactly one line starting with b i. 
* Width description
  * Describe the width function mapping for the bags
  * Value is in {0,1}
  * Form "w BagID Hyperedge Value"
    * Lines starting with character w
    * followed by an identifier for the bag
    * followed by the hyperedge
    * followed by the value in {0,1} the function maps to 
    * each separated by space each time
  * In order to save space we allow to skip width descriptions for (bag,hyperedge) -> 0 (i.e., if the function is not specified for a (bag,hyperedge), we implicitly assume value 0.)
* Tree description
  * NodeIDs run consecutively from 1 to l
  * Lines not starting with a character in {c,s,b,w} indicate an edge in the tree decomposition
  * Form: "Node1 Node2"
    * Lines starting with an identifier Node1 of the parent node
    * followed by an identifier Node2 of the child node
    * each separated by space each time
  * The graph described in this way must be a tree, i.e., root nodes do not have a preceding node
* Empty lines or lines consisting of spaces may occur and only will be ignored  
