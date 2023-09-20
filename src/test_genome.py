import unittest
import genome
import numpy as np
import os
from xml.dom.minidom import getDOMImplementation

class GenomeTest(unittest.TestCase):
    #Test if Genome class exist
    def testClassExist(self):
        self.assertIsNotNone(genome.Genome)

    #Test if Genome.get_random_gene method exist
    def testRandomGene(self):
        self.assertIsNotNone(genome.Genome.get_random_gene)

    #Test if Genome.get_random_gene method does not return None
    def testRandomGeneNotNone(self):
        self.assertIsNotNone(genome.Genome.get_random_gene(5))

    #Test if Genome.get_random_gene method returns Value 
    def testRandomGeneHasValue(self):
        gene = genome.Genome.get_random_gene(5)
        #print(gene)
        self.assertIsNotNone(gene[0])

    #Test if Genome.get_random_gene method returns the same amount of gene
    #as params
    def testRandomGeneLength(self):
        gene = genome.Genome.get_random_gene(5)
        self.assertEqual(len(gene), 5)

    #Test if Genome.get_random_gene return type of np.ndarry
    def testRandomGeneType(self):
        gene = genome;genome.Genome.get_random_gene(20)
        self.assertEqual(type(gene), np.ndarray)



    #Test if Genome.get_random_genome method exist
    def testRandomGenomeExist(self):
        data = genome.Genome.get_random_genome
        self.assertIsNotNone(data)

    #Test if Genome.get_random_genome method des not return None
    def testRandomeGenomeNotNone(self):
        self.assertIsNotNone(genome.Genome.get_random_genome(5, 10))

    #Test if Genome.get_gene_spec method exist
    def testGeneSpecExist(self):
        spec = genome.Genome.get_gene_spec
        self.assertIsNotNone(spec)

    #Test if Genome.get_gene_spec method does not return None
    def testGeneSpecNotNone(self):
        spec = genome.Genome.get_gene_spec()
        self.assertIsNotNone(spec)

    
    #Test if gene_spec has key: link-length
    def testGeneSpecHasLinkLength(self):
        spec = genome.Genome.get_gene_spec()
        self.assertIsNotNone(spec['link-length'])

    #Test if gene_spec has key: link-length has a IndexError
    def testGeneSpecHasLinkLengthIndex(self):
        spec = genome.Genome.get_gene_spec()
        #print(spec)
        self.assertIsNotNone(spec['link-length']['ind'])

    #Test if gene spec link-length is greater than 0
    def testGeneSpecScale(self):
        spec = genome.Genome.get_gene_spec()
        gene = genome.Genome.get_random_gene(20)
        #print(spec['link-length']['ind'])
        self.assertGreater(gene[spec['link-length']['ind']], 0)













































          
