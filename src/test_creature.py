import unittest
import creature

class TestCreature(unittest.TestCase):
    def testCreatureCreature(self):
        self.assertIsNotNone(creature.Creature)

    def testCreatureGetFlatLinks(self):
        c = creature.Creature(gene_count=4)
        links = c.get_flat_links()
        self.assertEqual(len(links), 4)

    def testCreatureExpandedLinks(self):
        c = creature.Creature(gene_count=25)
        links = c.get_flat_links()
        exp_links = c.get_expanded_links()
        self.assertGreaterEqual(len(exp_links), len(links))

    def testToXML(self):
        c = creature.Creature(gene_count=2)
        c.get_expanded_links()
        xml_str = c.to_xml()
        with open('creature1.urdf', 'w') as f:
            f.write('<?xml version="1.0"?>' + "\n" + xml_str)

        self.assertIsNotNone(xml_str)

    def testMotor(self):
        m = creature.Motor(0.1, 0.5, 0.5)
        self.assertIsNotNone(m)

    def testMotorValue(self):
        m = creature.Motor(0.1, 0.5, 0.5)
        self.assertEqual(m.get_output(), 1)

    def testMotorValue2(self):
        m = creature.Motor(0.6, 0.5, 0.5)
        m.get_output()
        m.get_output()
        m.get_output()
        self.assertGreater(m.get_output(), 0)

    def testCMotor(self):
        c = creature.Creature(gene_count=4)
        ls = c.get_expanded_links()
        ms = c.get_motors()
        self.assertEqual(len(ls) - 1, len(ms))
unittest.main(argv=['ignore', '-v'], exit=False)
