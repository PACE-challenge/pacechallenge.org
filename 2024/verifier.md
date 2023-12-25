---
layout: page 
title: "PACE 2024 - Verifier and Tester"
---

This package can be used to verify a given solution against a set of crossing counting algorithms.

## Installation

Install the [verifier](https://pypi.org/project/pace2024-verifier/) from [pip](https://pypi.org/project/pip/):

```console
$ pip install pace2024verifier
```

Alternatively you can download the code [here](./pace2024_verifier-0.3.0.tar.gz). Building the project works easily with [poetry](https://python-poetry.org/). After installing poetry, download and unpack the verifier, switch to the unpacked directory and execute:

```console
$ poetry build
```

This generates a `dist` directory containing the necessary wheel-file that can be installed via pip.

## Usage

### Verifier

To verify a solution use the following command:

```console
$ pace2024verify <path/to/graph.gr> <path/to/solution.sol>
```

The verifier has three different methods for verification usable via the switches:
* --segtree = Use a segment tree to count the crossings. `[default]`
* --interleave = Count the crossings by checking for each pair of edges if they interleave.
* --stacklike = Count the crossings by checking how many pairs are out of order in a one-sided book embedding.

There is also the option to only print the number of crossings via `-c/--only-crossings`.

### Tester

To test a solver against a set of tests use:

```console
$ pace2024tester <solver>
```

where `<solver>` has to be an executable. So if for example you run your solver via a shell-script `solver.sh` run the command `$ pace2024tester solver.sh`. The solver will then be run using the [tiny test set](https://pacechallenge.org/2024/tiny_test_set-overview.pdf). The instances and solutions of this set are included with the verifier. To add your own tests create a folder `mytests` containing a subfolder `instances` and a subfolder `<solutions>`. You can then run 

```console
$ pace2024tester --test <path/to/mytests> <solver>
```

and the tester will check the solver against this test set. You can also supply multiple test sets via

```console
$ pace2024tester --test <path/to/mytests1> --test <path/to/mytests2> <solver>
```

For each instance in an `instances` folder we match it to the same-named file in the solutions folder. The provided solver is then executed on each instance and the `pace2024verifier` is used to check the results. If you do not want to use the tiny test set you can switch it off using:

```console
$ pace2024tester --no-tiny --test <path/to/mytests1> --test <path/to/mytests2> <solver>
```

By default the tester assumes that the solver uses files for input and output and calls it as:

```console
$ <solver> path/to/input path/to/output
```

If you prefer using `stdin` or `stdout` use the following switches:
* --instanceas file/stdin = provide the input file as a path to the `file` or on `stdin`
* --solutionas file/stdin = expect the output to be written to a `file` or on `stdout`

For solution files the tester creates temporary file using the `tempdir` library of `python`. All created files are deleted by this library after execution.

Finally, for easier parsable output you can use the flag:
* --only-compare/-c which prints only the line `Testing now <instancename>...` followed by the string `<crossingssolver>,<crossingssolution>`.