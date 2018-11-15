---
layout: page
title: PACE 2019 (Vertexcover / Format) 
sidebar_link: true
sidebar_sort_order: 7
---

## Checker
See: TBA

## Input Format

### Graph (.gr)

The graph format coincides with [PACE2017 graph](https://pacechallenge.wordpress.com/pace-2017/track-a-treewidth/) format.

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
  * Line: "1 3\n" indicates an edge
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

Alternative (works by autodetection):
* Problem line in DIMACS edge format: "p edge NumVertices NumEdges"
* Starting a line edge lines with character 'e', i.e., "e 1 2"

```AsciiDoc
c This file describes a graph in td PACE2019 format with 6 vertices and 4 edges
p edge 6 4
e 1 2
e 2 3
c this is a comment and will be ignored
e 4 5
e 4 6
```



### Vertexcover Format (.vc)

* Line separator ‘\n’
* Lines starting with character c are interpreted as comments
* Vertices are consecutively numbered from 1 to n
* Solution description
  * Form "s vc NumVertices NumVerticesInVertexcover"
    * Line starting with character s
    * followed by the problem descriptor vc
    * followed by number n of vertices
    * followed by the number v of vertices in the vertexcover
    * each separated by space each time
  * Unique (No other line may start with p)
  * Has to be the first line (except comments)
* Vertexcover description
  * Lists the vertices in the vertexcover (at most v many)
  * Form "Vertex"
    * Lines consist only of one vertex identifier
* Empty lines or lines consisting of spaces may occur and only will be ignored  


```AsciiDoc
c This file describes for a graph with 5 vertices
c a vertexcover consisting of 2 vertices 
s vc 5 2
2
4
```
