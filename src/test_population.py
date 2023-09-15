import unittest
import population
class TestPop(unittest.TestCase):
    def testPopExist(self):
        pop = population.Population(pop_size=10, gene_count=4)
        self.assertIsNotNone(pop)

    def testPopHasIndis(self):
        pop = population.Population(pop_size=10, gene_count=4)
        self.assertEqual(len(pop.creatures), 10)

    def testFitMap(self):
        fits = [2.5, 1.2, 3.4]
        want = [2.5, 3.7, 7.1]
        fitmap = population.Population.get_fitness_map(fits)
        self.assertEqual(fitmap, want)

    def testSelfPar(self):
        fits = [2.5, 1.2, 3.4]
        fitmap = population.Population.get_fitness_map(fits)
        pid = population.Population.select_parent(fitmap)
        self.assertLess(pid, 3)
unittest.main()
