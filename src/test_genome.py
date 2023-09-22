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

    #Test if genome has URDFLink
    def testFlatLinks(self):
        links = [
                genome.URDFLink(name="A", parent_name= None, recur=1),
                genome.URDFLink(name="B", parent_name= "A", recur=1),
                genome.URDFLink(name="C", parent_name= "B", recur=2),
                genome.URDFLink(name="D", parent_name= "C", recur=1)
                ]
        self.assertIsNotNone(links)

    #Test if expanded links have 6 gene of URDFLink
    def testExpandLinks(self):
        links = [
                genome.URDFLink(name="A", parent_name= None, recur=1),
                genome.URDFLink(name="B", parent_name= "A", recur=1),
                genome.URDFLink(name="C", parent_name= "B", recur=2),
                genome.URDFLink(name="D", parent_name= "C", recur=1)
                ]
        exp_links = [links[0]]
        genome.Genome.expandLinks(links[0], links[0].name, links, exp_links)
        name = [n.name + "-Parent: " + str(n.parent_name) for n in exp_links]
        #print(name)
        self.assertEqual(len(exp_links),6)

    #Test conversion of gene to dict
    def testGeneToGeneDict(self):
        spec = genome.Genome.get_gene_spec()
        gene = genome.Genome.get_random_gene(len(spec))
        gene_dict = genome.Genome.get_gene_dict(gene, spec)
        self.assertIn("link-recurrence", gene_dict)

   #Test conversion of genome to a array of dicts
    def testGeneToGenomeDict(self):
        spec = genome.Genome.get_gene_spec()
        dna = genome.Genome.get_random_genome(len(spec), 3)
        genome_dicts = genome.Genome.get_genome_dicts(dna, spec)
        self.assertEqual(len(genome_dicts), 3)

    #Test get_links from genome dicts
    def testGetLinks(self):
        spec = genome.Genome.get_gene_spec()
        dna = genome.Genome.get_random_genome(len(spec), 3)
        genome_dicts = genome.Genome.get_genome_dicts(dna, spec)
        links = genome.Genome.genome_to_links(genome_dicts)
        self.assertEqual(len(links), 3)

    #Test urdflink to xml conversion
    def testLinkToXML(self):
        link = genome.URDFLink(name="A", parent_name="None", recur=1)
        domimpl = getDOMImplementation()
        adom = domimpl.createDocument(None, "robot", None)
        xml_str = link.to_link_xml(adom)
        #print(xml_str)
        self.assertIsNotNone(xml_str)

    def testXO(self):
        g1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
        g2 = np.array([[10,11,12],[13,14,15],[16,17,18]])
        g3 = genome.Genome.crossover(g1,g2)
        #print(g1,g2,g3)
        self.assertEqual(len(g3), len(g1))

    def test_point(self):
        g1 = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
        #print(g1)
        g2 = genome.Genome.point_mutate(g1, rate=0.5, amount=0.25)
        #print(g1)

    def test_shrink(self):
        g1 = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
        g2 = genome.Genome.shrink_mutate(g1, rate=1)
        #print(g1, g2)
        self.assertNotEqual(len(g1), len(g2))

    def test_grow(self):
        g1 = np.array([[1.0,2.0,3.0],[4.0,5.0,6.0],[7.0,8.0,9.0]])
        g2 = genome.Genome.grow_mutate(g1, rate = 1)
        #print(g1, g2)
        self.assertGreater(len(g2), len(g1))

    def testToCsv(self):
        g1=[[1,2,3]]
        genome.Genome.to_csv(g1, 'test.csv')
        self.assertTrue(os.path.exists('test.csv'))

    def testReadCsv(self):
        g1=[[1,2,3]]
        genome.Genome.to_csv(g1, 'test.csv')
        expect = "1,2,3,\n"
        with open("test.csv") as f:
            csv_str = f.read()
        self.assertEqual(csv_str, expect)

    def testReadCsvMult(self):
        g1 = [[1,2,3], [4,5,6]]
        genome.Genome.to_csv(g1, 'test.csv')
        expect = "1,2,3,\n,4,5,6,\n"
        with open("test.csv") as f:
            csv_str = f.read()
        self.assertEqual(csv_str, expect)

    def testFromCsv(self):
        g1 = [[1,2,3],[4,5,6]]
        genome.Genome.to_csv(g1, "test.csv")
        g2 = genome.Genome.from_csv("test.csv")
        print(g1,g2)
        self.assertTrue(np.array_equal(g1,g2))
unittest.main(argv=['ignore','-v'], exit=False)





































          
