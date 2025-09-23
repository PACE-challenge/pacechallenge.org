---
layout: page
title: "PACE 2026"
sidebar_link: true
sidebar_sort_order: 10
---

<style media="screen and (max-width:1020px)"> img {display:none;} </style>

## Problem

This year features the [Maximum-Agreement Forest (MAF)](./maf) problem arising in <a href="https://en.wikipedia.org/wiki/Phylogenetics">phylogenetics</a> (the study of evolutionary histories). The slides of the announcement made at IPEC'25 can be found [here](./announcement_slides.pdf).

## Timeline

 - September 2025: Announcement of the challenge and tracks
 - October 2025: Definition of input and output formats
 - November 2025: Tiny test set and verifier are provided
 - January 2026: Release of public instances and details about the benchmark
 - April 2026: Submission via [optil.io](https://optil.io/) opens
 - July 2026: Final submission deadline and Results

## Results
No results yet.

## Submission Guideline
We ask all participants to publish their codebase and solver description on Github or a similar platform that is publicly available.
The following files are required.
 - A license file at the root containing the license
 - An installation guide at the root that also contains information about external dependencies
 - the codebase
 - the solver description

The deadlines mentioned above apply. Note that changes on the codebase and the solver description after their respective deadlines are prohibited, except for small changes resulting from the reviewing phase in close contact with the organizers. We kindly ask all participants to send us an email by the submission deadline, including a link to their Github repository (or a similar platform). If your submission is eligible for the student ranking, please also include a brief note indicating this.

## Docker environment
A docker stack containing the evaluation environment is being prepared.

## Tracks
The challenge features three distinct tracks:
1. an "exact" track, solving MAF on an arbitrary number of trees -- for this track, the instances come with precomputed values of some parameters (along with proofs, e.g. decompositions of certain width)
2. a "heuristic" track, solving MAF on two trees -- the instances will consist of two large trees and the alloted computation-time will be short
3. a "lower-bound" track, also with two trees per instance -- the aim is to reach an approximate solution quickly

## Scoring
The exact and heuristic tracks will be scored simmilarly to previous installments of PACE.
The scoring for the lower-bound track will emphasize running time, among all solutions falling close enough to the optimum/known best solution.
The exact scoring rules are to be determined.

## Preliminary leaderboard on optil
As in previous years, a preliminary leaderboard on [optil](https://optil.io) will be available.

## Instances 
Public instances are to be published shortly.

## Program Committee

- [Alexander Leonhardt](https://ae.cs.uni-frankfurt.de/staff/alexander_leonhardt.html) (Goethe-Universität Frankfurt)
- [Manuel Penschuck](https://portal.findresearcher.sdu.dk/en/persons/manuel-penschuck) (University of Southern Denmark, Odense)
- [Mathias Weller](https://igm.univ-mlv.fr/~mweller/) (Université Gustave Eiffel, Paris)
