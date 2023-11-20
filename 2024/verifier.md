---
layout: page 
title: "PACE 2024 - Verifier"
---

This package can be used to verify a given solution against a set of crossing counting algorithms.

## Installation

Install the (verifier)[https://pypi.org/project/pace2024-verifier/] from (pip)[https://pypi.org/project/pip/]:

```console
$ pip install pace2024verifier
```

Alternatively you can download the code [here](./pace2024_verifier-0.2.0.tar.gz). Building the project works easily with [poetry](https://python-poetry.org/). After installing poetry, download and unpack the verifier, switch to the unpacked directory and execute:

```console
$ poetry build
```

This generates a `dist` directory containing the necessary wheel-file that can be installed via pip.

## Usage

To verify a solution use the following command:

```console
$ pace2024verify <path/to/graph.gr> <path/to/solution.sol>
```

The verifier has three different methods for verification usable via the switches:
* --segtree = Use a segment tree to count the crossings. `[default]`
* --interleave = Count the crossings by checking for each pair of edges if they interleave.
* --stacklike = Count the crossings by checking how many pairs are out of order in a one-sided book embedding.

There is also the option to only print the number of crossings via `-c/--only-crossings`.
