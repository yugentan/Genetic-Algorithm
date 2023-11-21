import unittest
import os 
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import simulation as simlib
from src import population as poplib
from src import creature as crlib
from src import genome as genlib
import numpy as np

class TestGA(unittest.TestCase):
    def testGA(self):
        pop = poplib.Population(pop_size=3, gene_count=4)
        sim = simlib.ThreadedSim(pool_size=4)

        for generation in range(500):
            sim.eval_population(pop, 2400)
            fits = [cr.get_distance_travelled() for cr in pop.creatures]
            fitmap = poplib.Population.get_fitness_map(fits)

            #print (generation, np.max(fits), np.mean(fits))
            print("Gen: " + str(generation) + ", Mean Fitness: " + str(np.mean(fits)))
            fmax = np.max(fits)
            for cr in pop.creatures:
                if cr.get_distance_travelled() == fmax:
                    elite = cr
                    break

            new_gen = []
            for cid in range(len(pop.creatures)):
                p1_ind = poplib.Population.select_parent(fitmap)
                p2_ind = poplib.Population.select_parent(fitmap)
                dna = genlib.Genome.crossover(pop.creatures[p1_ind].dna, pop.creatures[p2_ind].dna)
                dna = genlib.Genome.point_mutate(dna, 0.25, 0.25)
                dna = genlib.Genome.grow_mutate(dna, 0.25)
                dna = genlib.Genome.shrink_mutate(dna, 0.25)

                cr = crlib.Creature(1)
                cr.set_dna(dna)
                new_gen.append(cr)
            new_gen[0] = elite
            csv_filename = "../data/" + str(generation % 10) + "_elite.csv"
            genlib.Genome.to_csv(elite.dna, csv_filename)
            pop.creatures = new_gen
unittest.main()
