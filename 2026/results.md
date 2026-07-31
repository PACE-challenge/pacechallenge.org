---
layout: page 
title: "PACE 2026 - Results (preliminary)"
---

**The results are currently marked as preliminary to allow teams to voice concerns until 6th August 23:59 AoE**

We are happy to announce the results of PACE 2026.
Congratulations to the winners and all the participants!

## Experimental setup
- Evaluation was carried out using [SDU's uCloud servers](docs.cloud.sdu.dk):
  - Lenovo ThinkSystem SR645 V3
  - 2x AMD EPYC 9534 64-Core @ 2.45Ghz (at most 96 cores used due to limited RAM)
  - 1536 GB DDR5-4800 RAM

- Each track contains [400 instances (see details on selection)](./data)
- Each solver is evaluated thrice on random (but identical) machines in their own container, each time working on all 400 instances.
- Thus each solver can score a **total of 1200 points**

## Exact Track

| Rank      | Stud Rank | Solver                                                                                                                   | Authors                                                                                                                     | Solved     | Runtime    | Score | Delta |
| --------: | --------: | :----------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------- | ---------: | ---------: | ----: | ----: |
| 1         | 1         | [maffe](https://github.com/roehrt/maffe/tree/eb55f1a3c5c1a7c47e7d5f97c1c2d8943171875c)                                   | Anton Hoof, Tobias Röhr                                                                                                     | 1063       | 35043.6s   | 1063  |       |
| 2         |           | [woodcutter](https://github.com/jovarga/woodcutter/tree/530d29aca7543dd19abb4f50fa1ca7d76c4addc4)                        | Johannes Varga, Enrico Iurlano, Hai Xia                                                                                     | 1056       | 31544.8s   | 1056  | -7    |
| 3         | 2         | [klados](https://github.com/Buchineers/klados/tree/c3d2d556a979216a8ffcef7326918611060bd24d)                             | Christian Inhetveen, Marcin Mennemann, Marius Maximilian Hille                                                              | 866        | 117499.0s  | 866   | -190  |
| 4         |           | [TreeOfLife](https://github.com/HerrPixel/tree_of_life/tree/5382daef4b6de8aaf5e9e4777c94cd5565ba7385)                    | Jonas Seiler                                                                                                                | 691        | 80836.2s   | 691   | -175  |
| 5         |           | [sherby](https://github.com/bmarchand/sherby-pace-2026-solver/tree/983c0fa05b6cdc4d8336e3fb9cc4eb539f66a9e3)             | Nicolas Bousquet, Bertrand Marchand, Arnaud Mary, Sven Meyer                                                                | 648        | 94248.6s   | 648   | -43   |
| 6         | 3         | [Rens](https://github.com/TemporarilyTired/pace26-exact/tree/f58bd417c3e0e5f73bd1a8641f20bf3214ab827c)                   | Rens                                                                                                                        | 584        | 35258.2s   | 584   | -64   |
| 7         | 4         | [uni-bremen](https://github.com/pace26unibremen/PACE2026/tree/ba91eee5deec719c242f2faec0ec95973eff5f23)                  | Jonas Schramm, Philip Kail, Jurin Hoffmann, Alexander Wachowski, Leon Flaack, André Kaufmann, Florian Feegel                | 575        | 46271.0s   | 575   | -9    |
| 8         | 5         | [LazyBunch](https://github.com/GalambosAbel/pace/tree/3051830333532a0ea92c688b772fd7dc8eb935d9)                          | Ábel Galambos, Márton Tot Bagi                                                                                              | 544        | 35948.3s   | 544   | -31   |
| 9         |           | [UiB AlgoRythm](https://github.com/mlgorithm/UiB-AlgoRythm-Exact/tree/df080938e6a74960c946ab1adfba3147067e35f3)          | Juni Weisteen Bjerde, Wim Van den Broeck, Krishnan Dehaleesan, Yash Hiren More, Jakob Rødal Skaar, Tomáš Turek, Sam Urmian  | 493        | 57640.0s   | 493   | -51   |
| 10        |           | [UiB AlgoRhythm](https://github.com/metury/pace26/tree/b04684e12dfe6a0845fcc7ecd6ee48251087a780)                         | Juni Weisteen Bjerde, Wim Van den Broeck, Krishnan Dehaleesan, Yash Hiren More, Jakob Rødal Skaar , Tomáš Turek, Sam Urmian | 334        | 98215.8s   | 334   | -159  |
| 11        | 6         | [tospfrepe](https://github.com/fredpetersen/PACE26/tree/012347286912697accdc7c3ecaa5fc9acdefb0e3)                        | Tobias Gad SpoorenDonk and Frederik Petersen                                                                                | 318        | 32956.2s   | 318   | -16   |
| 12        | 7         | [NeckarCut](https://github.com/David-K0ch/NeckarCut/tree/c980f34f2b83bdf1bd34fcead38de245f794ecd3)                       | David Koch, Henning Woydt                                                                                                   | 253        | 30012.4s   | 253   | -65   |
| 13        |           | [Biahos](https://github.com/sohaibafifi/maf/tree/24f37e8369a43d5ed8e247dab320bf879e2c6f59)                               | Biahos                                                                                                                      | 137        | 45872.8s   | 137   | -116  |
| (WD)      |           | [PAAS](https://codeberg.org/uCYA9g3YursX9NTIanXzSLBwz/PACE2026_PAAS/src/commit/51f807c82effbe51ab705e55eaf8fd7994362026) | Shannon Gibbson                                                                                                             | 843        | 225043.8s  | (843) |       |
| (DQ)      |           | [CUFE](https://github.com/MichaelIbrahim-GaTech/PACE-2026/tree/3950cadfd14da045467f2a705b9a4e66fb38e9d1)                 | Michael Ibrahim                                                                                                             | 1197 (782) | 66226.5s   | (415) |       |
| (DQ) (WD) |           | [AAI](https://codeberg.org/lucas-isenmann/pace26/src/commit/7437d507f68d0de1f93608b6527f6a1d045a2194)                    | Mohamed Mahmoud Abdelwahab, Faisal Abu-Khzam, Lucas Isenmann                                                                | 1083 (918) | 1780929.6s | (279) |       |
| (DQ) (LS) |           | [ClusterLuck](https://github.com/alienblack/ClusterLuck/tree/8d98e4ab2b8629834fc46f111aeb9f0a31486f49)                   | Rishank Goyal, Srinibas Swain                                                                                               | 648 (22)   | 192511.5s  | (626) |       |
| (LS)      |           | [CherryPicker 2](https://github.com/alienblack/CherryPicker/tree/000fce46eeeae415f5a85adbf48568a188b3b96f)               | Rishank Goyal, Srinibas Swain                                                                                               | 510        | 172181.1s  | (510) |       |

**(WD)**: authors withdrew submission, **(LS)**: code was submitted after deadline, **(DQ)**: solver produced illegal solutions (number indicated in brackets in column *Solved*)


## Heuristic Track

| Rank | Stud Rank | Solver                                                                                                              | Authors                                                                                                                    | Solved   | Runtime   | Score     | Delta    |
| ---: | --------: | :------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------- | -------: | --------: | --------: | -------: |
| 1    | 1         | [maffe](https://github.com/roehrt/maffe/tree/eb55f1a3c5c1a7c47e7d5f97c1c2d8943171875c)                              | Anton Hoof, Tobias Röhr                                                                                                    | 1197     | 155934.5s | 1196.109  |          |
| 2    | 2         | [searchsPACE](https://github.com/ManuelRonhaar/searchsPACE/tree/1e10a2bc0d0984175172fa7b60cba9ede402d3d6)           | Manuel Ronhaar                                                                                                             | 1199     | 142675.5s | 1195.654  | -0.455   |
| 3    | 3         | [Dakopen](https://github.com/dakopen/PACE-2026-Submission/tree/8e5dc38ec019e4b4ac7110396ad061fadf2f7a27)            | Daniel Busch                                                                                                               | 1200     | 198280.9s | 1195.266  | -0.388   |
| 4    | 4         | [CherryPicker 1](https://github.com/jdziura/PACE2026_CherryPicker/tree/cc2b3e9ba2dc9d445e76840e712f7452cd2d147c)    | Jakub Dziura, Tomáš Masařík                                                                                                | 1200     | 359996.7s | 1195.113  | -0.152   |
| 5    |           | [woodcutter](https://github.com/jovarga/woodcutter/tree/1721bc4e4853f31559205238252e0e332bd7f1b5)                   | Johannes Varga, Enrico Iurlano, Hai Xia                                                                                    | 1199     | 240010.3s | 1185.757  | -9.356   |
| 6    | 5         | [klados](https://github.com/Buchineers/klados/tree/c3d2d556a979216a8ffcef7326918611060bd24d)                        | Christian Inhetveen, Marcin Mennemann, Marius Maximilian Hille                                                             | 1181     | 201259.6s | 1171.974  | -13.783  |
| 7    | 6         | [MAFia 1](https://github.com/SmithinJRaj/PACE-Heuristic-Track-Solver/tree/0a34a219cb5d347444956a10d5704f3c7014d770) | Smithin J Raj, Fahad Ali Habeeb, Ashwin Jacob                                                                              | 1200     | 357318.7s | 1153.416  | -18.557  |
| 8    |           | [Bocconi](https://github.com/adampolak/samaf/tree/288a799c5d71aa2ed1e63ac9a4ee3c8efbe99b12)                         | Adam Polak                                                                                                                 | 1200     | 359277.9s | 1128.838  | -24.579  |
| 9    | 7         | [MAFia 2](https://github.com/alienblack/MAFia/tree/65eec0621cc5c07003569e101c314d054554bbf8)                        | Rishank Goyal, Shrey Sharma, Srinibas Swain                                                                                | 1200     | 352890.9s | 1108.483  | -20.355  |
| 10   | 8         | [pace_nitw](https://github.com/aadit-n/pace2026/tree/5f5a92fdc3adfed225509de850932df89ae89250)                      | Aadit Nair, Anish Deodhar, Sumit Mishra                                                                                    | 1200     | 87077.4s  | 1099.687  | -8.796   |
| 11   |           | [monet](https://github.com/TMonet2/PACE_2026_heuristic_monet/tree/316ae312d0219bdc968a94bd70d59481ef9ea723)         | Xinyu Wang, Chenghao Zhu, Yi Zhou, Yiping Liu                                                                              | 1200     | 349044.0s | 1047.893  | -51.795  |
| 12   |           | [axs](https://github.com/TMonet2/PACE_2026_heuristic_monet/tree/498b27689e3f1be245927fa13cc1d02d9450e7ed)           | Xinyu Wang, Chenghao Zhu, Yi Zhou, Yiping Liu                                                                              | 1200     | 352805.3s | 1005.493  | -42.400  |
| 13   |           | [UiB AlgoRythm](https://github.com/mlgorithm/UiB-AlgoRythm-Heuristic/tree/476431abedeeef2f8471ccbbb1a607e3e16e82b1) | Juni Weisteen Bjerde, Wim Van den Broeck, Krishnan Dehaleesan, Yash Hiren More, Jakob Rødal Skaar, Tomáš Turek, Sam Urmian | 1200     | 333554.0s | 956.044   | -49.448  |
| 14   |           | [Panda Squad](https://github.com/ShadowCreator/pace-2026-algorithm/tree/37db038db6bf599374dc4d02f64f53ec4d847496)   | Liam and Narges                                                                                                            | 1200     | 355209.9s | 892.734   | -63.310  |
| 15   | 9         | [uni-bremen](https://github.com/pace26unibremen/PACE2026/tree/ba91eee5deec719c242f2faec0ec95973eff5f23)             | Jonas Schramm, Philip Kail, Jurin Hoffmann, Alexander Wachowski, Leon Flaack, André Kaufmann, Florian Feegel               | 1200     | 333864.5s | 745.134   | -147.600 |
| 16   |           | [DeltaSearch](https://github.com/rebinsilva/MAF_DS/tree/4aec0e77f0e0624c02a8ec41c897d99532c16c0c)                   | Arnav Bajjuri, Farhana Akter Tumpa, Rebin Silva Valan Arasu, Rajiv Gupta                                                   | 1200     | 359996.5s | 550.012   | -195.122 |
| 17   |           | [Biahos](https://github.com/sohaibafifi/maf/tree/24f37e8369a43d5ed8e247dab320bf879e2c6f59)                          | Biahos                                                                                                                     | 1200     | 346845.0s | 546.937   | -3.075   |
| (DQ) |           | [CUFE](https://github.com/MichaelIbrahim-GaTech/PACE-2026/tree/3950cadfd14da045467f2a705b9a4e66fb38e9d1)            | Michael Ibrahim                                                                                                            | 1193 (7) | 299440.9s | (993.316) |          |

**(DQ)**: solver produced illegal solutions (number indicated in brackets in column *Solved*)

## Lower Bound

| Rank | Stud Rank | Solver                                                                                                           | Authors                                                                                                      | Solved    | Runtime   | Score     | Delta    |
| ---: | --------: | :--------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------- | --------: | --------: | --------: | -------: |
| 1    | 1         | [maffe](https://github.com/roehrt/maffe/tree/48a08df701cb6e6eb20074d5c5c6c5f59f1bff31)                           | Anton Hoof, Tobias Röhr                                                                                      | 1128      | 6785.4s   | 1122.438  |          |
| 2    | 2         | [CherryPicker 1](https://github.com/jdziura/PACE2026_CherryPicker/tree/cc2b3e9ba2dc9d445e76840e712f7452cd2d147c) | Jakub Dziura, Tomáš Masařík                                                                                  | 1104      | 21721.2s  | 1086.196  | -36.242  |
| 3    | 3         | [searchsPACE](https://github.com/ManuelRonhaar/searchsPACE/tree/1e10a2bc0d0984175172fa7b60cba9ede402d3d6)        | Manuel Ronhaar                                                                                               | 1107      | 26028.5s  | 1085.665  | -0.531   |
| 4    | 4         | [klados](https://github.com/Buchineers/klados/tree/c3d2d556a979216a8ffcef7326918611060bd24d)                     | Christian Inhetveen, Marcin Mennemann, Marius Maximilian Hille                                               | 1045      | 20434.0s  | 1028.251  | -57.414  |
| 5    |           | [woodcutter](https://github.com/jovarga/woodcutter/tree/1721bc4e4853f31559205238252e0e332bd7f1b5)                | Johannes Varga, Enrico Iurlano, Hai Xia                                                                      | 993       | 38677.7s  | 961.297   | -66.954  |
| 6    | 5         | [CutSetGo](https://github.com/alienblack/CutSetGo/tree/aaa0fd32a2709bf3c791bfff475104dae3b022bf)                 | Rishank Goyal, Srinibas Swain                                                                                | 786       | 65813.0s  | 732.055   | -229.242 |
| 7    | 6         | [uni-bremen](https://github.com/pace26unibremen/PACE2026/tree/ba91eee5deec719c242f2faec0ec95973eff5f23)          | Jonas Schramm, Philip Kail, Jurin Hoffmann, Alexander Wachowski, Leon Flaack, André Kaufmann, Florian Feegel | 232       | 5202.9s   | 227.735   | -504.320 |
| 8    | 7         | [uni-bremen-lb](https://github.com/pace26unibremen/PACE2026_LB/tree/37dd4eff4cdb769bb8737a53d8f6ca2b4c6948a2)    | Jonas Schramm, Philip Kail, Jurin Hoffmann, Alexander Wachowski, Leon Flaack, André Kaufmann, Florian Feegel | 231       | 6178.5s   | 225.936   | -1.800   |
| (DQ) |           | [CUFE](https://github.com/MichaelIbrahim-GaTech/PACE-2026/tree/3950cadfd14da045467f2a705b9a4e66fb38e9d1)         | Michael Ibrahim                                                                                              | 465 (735) | 395.7s    | (464.942) |          |
| (DQ) |           | [Biahos](https://github.com/sohaibafifi/maf/tree/24f37e8369a43d5ed8e247dab320bf879e2c6f59)                       | Biahos                                                                                                       | 671 (529) | 689204.2s | (361.490) |          |

**(DQ)**: solver produced illegal solutions (number indicated in brackets in column *Solved*)

### Acknowledgements
We gratefully acknowledge the computing time provided by [UCloud](https://docs.cloud.sdu.dk/) interactive HPC system, which is managed by the eScience Center at the University of Southern Denmark, and the NHR Center NHR@SW at Goethe University Frankfurt. 