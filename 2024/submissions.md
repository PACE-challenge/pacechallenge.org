---
layout: page 
title: "PACE 2024 - Submission requirements"
---

## Registration

If you plan to participate in the challenge, please register your team
as follows:

1. Register an account for your team at [optil.io](https://www.optil.io/optilion/login).
2. Submit your solution via [optil.io](https://www.optil.io/optilion/login).

## Source Code Requirements

All submissions have to be published with the following requirements:

1. The source code must be available in a repository (e.g.,
   [Bitbucket](https://bitbucket.org), [GitHub](https://github.com),
   [Gitlab](https://gitlab.com)).   
2. The project must be publicly visible by June 10th, 2024 (AoE).      
3. The submission has to have an <em style="color:#db8a00">open
   source</em> licence (e.g., GPL, MIT, or public domain).   
4. The repository has to contain a release with the name <em
   style="color:#db8a00">pace-2024</em>.
5. The release must be placed in a digital library (e.g.,
      [Zenodo](https://zenodo.org/)) and has to be equipped with a DOI. 

The repository must contain the following files:

- a `LICENSE.md` or `LICENSE.txt` file at the root that contains the
  used license.
- a `README.md` or `README.txt` file at the root that contains:
  - a brief description of the submission;
  - detailed description on how to build and run the solver;
  - requirements on external libraries (if any);
- the solver description as PDF.

## Solver Description Requirements

Each solver has to be shipped with a brief solver description in
PDF. The document:

- has to be set with the
  [LIPIcs](https://www.dagstuhl.de/en/publications/lipics/instructions-for-authors/)
  LaTeX style;
- should briefly describe the used techniques and references to the original publications. The description can have <em
   style="color:#db8a00">at most 3 pages</em> including title page and excluding references.
- Use as paper title your login name from [optil.io](https://www.optil.io/optilion/login);
- Place your login name from [optil.io](https://www.optil.io/optilion/login), the name of your solver and a reference
  to the public source code repository in the paper.

## Build Tool Requirements

While we do not require the use of a specific building tool, we highly encourage to use one, e.g., cmake, cargo, etc.
This allows other researchers to later use your code and improve upon your solver. 

## Library Requirements

We allow a limited use of external <em style="color:#db8a00">open
source</em> dependencies, preferably with source code included in
the submission. If you need to install software on the target
platform, please contact the organizers in advance, and we will ask the
[optil.io](https://www.optil.io/optilion/login) team if it is
possible.

## Sequential Requirement

Only sequential algorithms are permitted. Submissions that actively use
parallelism will be <em style="color:#db8a00">disqualified</em>. 
*Non-active* parallelism such as Java's garbage collector are, however,
allowed. If you are unsure whether some subroutine falls under this
rule, it probably does not. Please contact the organizers in advance, if
you have questions.

## Submission Process

Solvers have to be submitted via [optil.io](https://www.optil.io/) and
Google Drive as follows:

1. Submit the solver via [optil.io](https://www.optil.io/), please refer
      to their [help page](https://www.optil.io/optilion/help). 
2. Create a release in the repository of the solver (name:
      <em style="color:#db8a00">pace-2024</em>).   
3. Make the repository publicly visible until June 10th, 2024 (AoE).
4. Place the source code of the solver in a digital library (e.g.,
      [Zenodo](https://zenodo.org/)) and generate a DOI. 
5. Submit the link to the public repository containing your release via [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSeOfYj3jKWZa7gEqfjRGhUj5lVypoX5FXuCTwD7KetOWhgBVg/viewform?usp=sharing) until June 9th, 2024 (AoE).
6. Submit the solver description via [Google Form](https://docs.google.com/forms/d/e/1FAIpQLScAH0yhQn6C_h8Aec27hvePpaAVm3mtcfM3mi1tOJ7UaDrlew/viewform?usp=sharing) and use the DOI to refer to the solver and include a reference to the public source code repository until June 23rd, 2024 (AoE).

## Student Submissions

A student is someone who is not and has not been enrolled in a PhD
program before the submission deadline. A submission is eligible for a
Student Submission Award if either all its authors are students, or
besides student co-author(s) there is one non-student co-author that
confirms, at the moment of submission, that a clear majority of
conceptual and implementation work was done by the student
co-author(s).

## Submitting Multiple Solvers

While we do not strictly limit the number of solvers
submitted by a team, please refrain from submitting multiple solvers
that share significant parts of algorithmic code to the same track. Instead,
try unifying these solvers and optimizing the parameters used to
submit a single solver. We reserve the right to remove solvers (or
teams, if necessary) from the competition that heavily violate this
rule. For instance, you are not allowed to submit the same solver
multiple times using different parameters.
