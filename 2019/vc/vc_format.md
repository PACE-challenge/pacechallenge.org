---
layout: page
title: PACE 2019 (Vertex Cover / Format) 
sidebar_link: false
sidebar_sort_order: 7
---

## Checker
See: [vc_validate](https://github.com/hmarkus/vc_validate/tree/master)


## Input Format

### Graph (.gr)

The graph format is similar to the PACE2016 and [PACE2017 graph](/2017/treewidth/) format.

* Line separator ‘\n’
* Lines starting with character c are interpreted as comments
* Vertices are consecutively numbered from 1 to n
* Problem description
  * Form "p td NumVertices NumHyperedges"
    * Line starting with character p 
    * followed by the problem descriptor td 
    * followed by number n of vertices
    * followed by number m of edges
    * each separated by space each time
  * Unique (No other line may start with p)
  * Has to be the first line (except comments)
* Remaining lines indicate edges
  * consisting of two decimal integers separated by space
  * Line "1 3\n" indicates an edge between vertex 1 and vertex 3
* Empty lines or lines consisting of spaces may occur and only will be ignored  
* Graphs may contain isolated vertices, multiple edges, and loops

Example:

```AsciiDoc
c This file describes a graph in td PACE2019 format with 6 vertices and 4 edges
p td 6 4
1 2
2 3
c this is a comment and will be ignored
4 5
4 6
```

### Vertex Cover Format (.vc)

* Line separator ‘\n’
* Lines starting with character c are interpreted as comments
* Vertices are consecutively numbered from 1 to n
* Solution description
  * Form "s vc NumVertices NumVerticesInVertexcover"
    * Line starting with character s
    * followed by the problem descriptor vc
    * followed by number n of vertices
    * followed by the number v of vertices in the vertex cover
    * each separated by space each time
  * Unique (No other line may start with s)
  * Has to be the first line (except comments)
* Vertex cover description
  * Lists the vertices in the vertex cover (at most v many)
  * Form "Vertex"
    * Lines consist only of one vertex identifier
* Empty lines or lines consisting of spaces may occur and only will be ignored  


```AsciiDoc
c This file describes for a graph with 5 vertices
c a vertex cover consisting of 2 vertices 
s vc 5 2
2
4
```
