# A Genetic Algorithm for the Maximum Independent Set Problem

This repository includes the source code for my implementation of a Genetic Algorithm.

It has been developed as coursework for the *Algorithms and Combinatorial Optimisation* course as part of the M2 GENIOMHE under the supervision of Prof. Franck Delaplace. 

# Usage 

## Installation

To clone this repository, run the following in a terminal:

```bash
$ git clone https://github.com/davidfdr99/GeneticAlgo_MISP.git
```
`algorithms/` contains the functions of the genetic algorithm in `geneticalgo.py` and `brute_force_mis.py`, a brute force solution for the MISP. 


# The Maximum Independent Set problem

In graph theory, an independent set $S$ of a given graph $G=(V,E)$ is a number of vertices $v \in V$ such that no two vertices in $S$ are adjacent, i.e. that no edges $e \in E$ are shared.
*The Maximum Independent Set* (MISP) is the largest possible set of $G$. It can be defined as:

- $V' \subseteq V$ such that $\forall i, j \in V'$ the edge $\langle i, j \rangle \notin E$ and $|V'|$ is maximum (see Bäck & Khuri (1994))


## Example graphs:

The MISP is deemed NP-hard. You can find a `misp.ipynb` notebook visualising the performance of the Genetic Algorithm in the `examples/` folder. 

# References

* **Back, T and Khuri, S**. *An evolutionary heuristic for the maximum independent set problem*. Proceedings of the First IEEE Conference on Evolutionary Computation. IEEE World Congress on Computational Intelligence (1994). https://doi.org/10.1007/s10109-020-00342-2.

# License [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This work is protected under the MIT License.