from os import get_inheritable, stat
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

    @staticmethod
    def genome_to_links(_genome_dicts):
        link_ind = 0
        parent_names = [str(link_ind)]
        links = []
        
        for gdict in _genome_dicts:
            link_name = str(link_ind)
            parent_ind = parent_names[int(parent_ind)]
            recur = gdict["link-recurrence"]
            link = URDFLink(name = link_name,
                            parent_name = parent_name,
                            recur = recur + 1,
                            link_length = gdict["link-length"],
                            link_radius = gdict["link-radius"],
                            link_mass = gdict["link-mass"],
                            joint_type = gdict["joint-type"],
                            joint_parent = gdict["joint-parent"],
                            joint_axis_xyz = gdict["joint-axis-xyz"],
                            joint_origin_rpy_1 = gdict["joint-origin-rpy-1"],
                            joint_origin_rpy_2 = gdict["joint-origin-rpy-2"],
                            joint_origin_rpy_3 = gdict["joint-origin-rpy-3"],
                            joint_origin_xyz_1 = gdict["joint-origin-xyz-1"],
                            joint_origin_xyz_2 = gdict["joint-origin-xyz-2"],
                            joint_origin_xyz_3 = gdict["joint-origin-xyz-3"],
                            control_waveform = gdict["control-waveform"],
                            control_amp = gdict["control-amp"],
                            control_freq = gdict["control-freq"])
            links.append(link)
            if link_ind != 0:
                parent_names.append(link_name)
            link_ind = link_ind + 1

            links[0].parent_name = "None"
        return links

    @staticmethod
    def crossover(g1,g2):
        xo = np.random.randint(len(g1))
        if xo == 0:
            return g2
        if xo == len(g1) - 1:
            return g1
        if xo > len(g2):
            xo = len(g2) - 1
        g3 = np.concatenate((g1[0:xo], g2[xo:]))
        return g3
    
    @staticmethod
    def point_mutate(g1, rate, amount):
        for gene in g1:
            if np.random.rand() < rate:
                ind = np.random.randint(len(gene))
                r = (np.random.rand() - 0.5) * amount
                gene[ind] = gene[ind] + r
            return g1

    @staticmethod
    def shrink_mutate(g1, rate):
        if len(g1) == 1:
            return g1
        if np.random,rand() < rate:
            ind = np.random.randint(len(g1))
            g1 = np.delete(g1, ind, 0)
        return g1

    @staticmethod
    def grow_mutate(g1, rate):
        if np.random.rand() < rate:
            gene = Genome.get_random_gene(len(g1[0]))
            g1 = np.append(g1, [gene], axis=0)
        return g1































