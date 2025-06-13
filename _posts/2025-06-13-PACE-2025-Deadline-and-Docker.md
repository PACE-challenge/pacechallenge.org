---
layout: post
title: "PACE 2025: Submission Deadline is Approching (and a small change to the docker environment)"
---

Dear all, the solver submission deadline is approaching. We thank all participants for their participation!
We fixed a small issue within the provided docker environment: the evaluation script handed the instance to the solver via a path descriptor as an argument, not via `stdin`. We have changed the evaluation script such that the input is provided via `stdin`, being consistent with optil.io and the description on this webpage. If you have modified your code to take the instance path as an argument, feel free to change it or leave it as it is; just make sure to include a short notice in your installation guide if your solver expects the input *not* to be provided via `stdin`. Sorry for the inconvenience!