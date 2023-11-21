# Rigid Body Creature Simulation with PyBullet using Genetic Algorithms

This project emulates Karl Sims' evolutionary approach to generate and simulate creatures using PyBullet's physics engine. The system employs a Genetic Algorithm (GA), a fundamental component of Evolutionary Computation (EC), to evolve and optimize creatures for locomotion and robustness.

## Background
**Genetic Algorithm (GA) Overview**

- **Representation (Genome):** Creatures are represented as genomes, composed of genes encapsulating various structural and behavioral characteristics such as joint types, lengths, control mechanisms, and more.

- **Mutation Operators:** 
    - **Point Mutation:** Randomly alters individual genes within a genome based on a specified mutation rate and amount.
    - **Shrink Mutation:** Removes genes from the genome with a certain probability, reducing complexity.
    - **Grow Mutation:** Adds new genes to the genome with a given probability, increasing complexity.

- **Crossover Operator:** Facilitates the combination of genetic material from two parent creatures to produce offspring genomes.

## Fitness Evaluation and Selection
- **Fitness Function:** Evaluates each creature's performance within the simulation based on distance travelled or other locomotion metrics.

- **Selection Mechanism:** Utilizes a fitness-proportional selection method (roulette wheel selection) to determine parent creatures for the next generation.

- **Elitism:** Retains a certain portion of the best-performing individuals from the current population to ensure their inclusion in the next generation, promoting convergence toward higher fitness solutions.

## Files and Structure + Test Suite Overview
-   `main.py:` Starts the simulation in PyBullet.
-   **src directory:**
    - `genome.py:` Contains Genome-related functions, including gene representation, mutation, crossover, genome-to-links conversion and etc.
    - `creature.py:` Manages creature generation from genes, and XML serialization.
    - `population.py:` Responsible for managing populations of creatures.
    - `simulation.py:` Handles the simulation process using PyBullet.
-   **test directory:** Contains test suite + the generation of GA process
    - `test_ga.py:` Runs the genetic algorithm and evaluates its functionality
    - `test_genome.py:` Unit test for Genome class functionalities
    - `test_creature.py:` Unit test for Creature class functionalities
    - `test_population.py:` Unit test for Population class functionalities
    - `test_simulation.py:` Unit test for Simulation class functionalities
- **data directory:** Contains all the data files generated from `test_ga.py` and file required to run `main.py`.
- **findings directory:** Contains a short writeup in jupyter notebook on the simulation.
- **build & dist directory:** Currently empty, will be use for future development purpose
  
## Dependencies
- PyBullet
- NumPy

## Usage
- Run the `main.py` to initiate the simulation
    - Simulation will use the 9th generation of the genetic algorithm along side the creature.urdf file found in the `data` directory.
- Generation and Testing
    - Execute `test_ga.py` for the evaluation of the genetic algorithm process. This will generate `idx_elite.csv` into the `data` directory where idx will be the current generation % 10. Default generation is set at **100 iterations**, you may change so if you wish to improve result over a longer period of iterations. Similarly, rate of mutation can be tweak here as well. 
    - Execute specified test files with `test` directory to conduct unit testing on various functionalities
      
## Acknowledgements
Karl Sims' Creature Influence

The simulation draws inspiration from Karl Sims' pioneering work on evolving virtual creatures. It emphasizes generative methods for evolving diverse and functional forms of artificial life.

[Evolving Virtual Creatures - Karl Sims (1994)](https://www.karlsims.com/papers/siggraph94.pdf)
