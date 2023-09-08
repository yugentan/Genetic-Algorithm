import numpy as np
import copy

class Genome:

    @staticmethod
    def get_random_gene(_size):
        gene = np.array([np.random.random() for i in range (_size)])
        return gene

    @staticmethod
    def get_random_genome(_size, _gene_count):
        genome = [Genome.get_random_gene(_size) for i in range (_gene_count)]
        return genome

    @staticmethod
    def get_gene_spec():
        gene_spec = {
            "link-shape" : {"scale":1}, 
            "link-length" : {"scale":5},
            "link-radius" : {"scale":1},
            "link-recurrence" : {"scale":6},
            "link-mass" : {"scale":1},
            "joint-type" : {"scale":1},
            "joint-parent" : {"scale":1},
            "joint-axis-xyz" : {"scale":1},
            "joint-origin-rpy-1" : {"scale":np.pi * 2},
            "joint-origin-rpy-2" : {"scale":np.pi * 2},
            "joint-origin-rpy-3" : {"scale":np.pi * 2},
            "joint-origin-xyz-1" : {"scale":1},
            "joint-origin-xyz-2" : {"scale":1},
            "joint-origin-xyz-3" : {"scale":1},
            "control-waveform" : {"scale":1},
            "control-amp" : {"scale":0.25},
            "control-freq" : {"scale":1},
        }
        index = 0
        for key in gene_spec.keys():
            gene_spec[key]["ind"] = index
            index += 1
        return gene_spec

    @staticmethod
    def get_gene_dict(_gene, _spec):
        gdict = {}
        for key in _spec:
            ind = _spec[key]["ind"]
            scale = _spec[key]["scale"]
            gdict[key] = _gene[ind] * scale
        return gdict

    @staticmethod
    def get_genome_dicts(_dna, _spec):
        gdicts = []
        for gene in _dna:
            gdicts.append(Genome.get_gene_dict(gene, _spec))
        return gdicts

    @staticmethod
    def expandLinks(_parent_links, _unique_parent_name, _flat_links, _exp_links):
        children = [l for l in _flat_links if l.parent_name = _parent_links.name]
        sibling_ind = 1
        for c in children:
            for r in range(c.recur):
                sibling_ind = sibling_ind + 1
                c_copy = copy.copy(c)
                c_copy.parent_name = _unique_parent_name
                uniq_name = c_copy.name + str(len(_exp_links))
                c_copy.name = uniq_name
                c_copy.sibling_ind = sibling_ind
                _exp_links.append(c_copy)
                Genome.expandLinks(c, uniq_name, _flat_links, _exp_links)

















