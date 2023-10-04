import unittest
import simulation
import creature
import population
import os
class TestSim(unittest.TestCase):
    def testSimExist(self):
        sim = simulation.Simulation()
        self.assertIsNotNone(sim)

    def testSimId(self):
        sim = simulation.Simulation()
        self.assertIsNotNone(sim.physicsClientId)

    def testRun(self):
        sim = simulation.Simulation()
        self.assertIsNotNone(sim.run_creature)
    
    def testRunXML(self):
        sim = simulation.Simulation()
        cr = creature.Creature(gene_count=3)
        sim.run_creature(cr)
        self.assertTrue(os.path.exist("temp0.urdf"))

    def testRunPos(self):
        sim = simulation.Simulation()
        cr = creature.Creature(gene_count=3)
        sim.run_creature(cr)
        #print(cr.start_position)
        #print(cr.end_position)
        self.assertNotEqual(cr.start_position, cr.end_position)

    def testDist(self):
        sim = simulation.Simulation()
        cr = creature.Creature(gene_count=3)
        sim.run_creature(cr)
        dist = cr.get_distance_travelled()
        #print(dist)
        self.assertGreater(dist,0)

    def testPop(self):
        pop = population.Population(pop_size=10, gene_count=3)
        sim = simulation.Simulation()
        for cr in pop.creatures:
            sim.run_creature(cr)
        dist = [cr.get_distance_travelled() for cr in pop.creatures]
     
        #print(dist)
        self.assertIsNone(dist)

    def testProc(self):
        pop = population.Population(pop_size=10, gene_count=3)
        tsim = simulation.ThreadedSim(pool_size=4)
        tsim.eval_population(pop, 2400)
        dist = [cr.get_distance_travelled() for cr in pop.creatures]
        #print(dist)
        self.assertIsNotNone(dist)

unittest.main()
