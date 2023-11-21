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
        children = [l for l in _flat_links if l.parent_name == _parent_links.name]
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
            parent_ind = gdict["joint-parent"] * len(parent_names)
            parent_name = parent_names[int(parent_ind)]
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
        if np.random.rand() < rate:
            ind = np.random.randint(len(g1))
            g1 = np.delete(g1, ind, 0)
        return g1

    @staticmethod
    def grow_mutate(g1, rate):
        if np.random.rand() < rate:
            gene = Genome.get_random_gene(len(g1[0]))
            g1 = np.append(g1, [gene], axis=0)
        return g1

    @staticmethod
    def to_csv(_dna, _csv_file):
        csv_str = ""
        for gene in _dna:
            for val in gene:
                csv_str = csv_str + str(val) + ","
            csv_str = csv_str + '\n'
        with open(_csv_file, 'w') as f:
            f.write(csv_str)

    @staticmethod
    def from_csv(_filename):
        csv_str = ""
        with open(_filename) as f:
            csv_str = f.read()

        dna = []
        lines = csv_str.split('\n')
        for line in lines:
            vals = line.split(',')
            gene = [float(v) for v in vals if v != '']
            if len(gene) > 0:
                dna.append(gene)
        return dna
class URDFLink:
    def __init__(self,
                 name,
                 parent_name,
                 recur,
                 link_length = 0.1,
                 link_radius = 0.1,
                 link_mass = 0.1,
                 joint_type = 0.1,
                 joint_parent = 0.1,
                 joint_axis_xyz = 0.1,
                 joint_origin_rpy_1 = 0.1,
                 joint_origin_rpy_2 = 0.1,
                 joint_origin_rpy_3 = 0.1,
                 joint_origin_xyz_1 = 0.1,
                 joint_origin_xyz_2 = 0.1,
                 joint_origin_xyz_3 = 0.1,
                 control_waveform = 0.1,
                 control_amp = 0.1,
                 control_freq = 0.1):

        self.name = name
        self.parent_name = parent_name
        self.recur = int(recur)
        self.link_radius = link_radius
        self.link_length = link_length
        self.link_mass = link_mass
        self.joint_type = joint_type
        self.joint_parent = joint_parent
        self.joint_axis_xyz = joint_axis_xyz
        self.joint_origin_rpy_1 = joint_origin_rpy_1
        self.joint_origin_rpy_2 = joint_origin_rpy_2
        self.joint_origin_rpy_3 = joint_origin_rpy_3
        self.joint_origin_xyz_1 = joint_origin_xyz_1
        self.joint_origin_xyz_2 = joint_origin_xyz_2
        self.joint_origin_xyz_3 = joint_origin_xyz_3
        self.control_waveform = control_waveform
        self.control_amp = control_amp
        self.control_freq = control_freq
        self.sibling_ind = 1

    def to_link_xml(self, adom):

        link_tag = adom.createElement("link")
        link_tag.setAttribute("name", self.name)

        #segment for link visual
        vis_tag = adom.createElement("visual")
        geom_tag = adom.createElement("geometry")
        cyl_tag = adom.createElement("cylinder")
        cyl_tag.setAttribute("length", str(self.link_length))
        cyl_tag.setAttribute("radius", str(self.link_radius))

        #merge
        geom_tag.appendChild(cyl_tag)
        vis_tag.appendChild(geom_tag)
        link_tag.appendChild(vis_tag)

        #segment for link collision 
        collision_tag = adom.createElement("collision")
        c_geom_tag = adom.createElement("geometry") 
        c_cyl_tag = adom.createElement("cylinder")
        c_cyl_tag.setAttribute("length", str(self.link_length))
        c_cyl_tag.setAttribute("radius", str(self.link_radius))

        #merge
        c_geom_tag.appendChild(c_cyl_tag)
        collision_tag.appendChild(c_geom_tag)
        link_tag.appendChild(collision_tag)

        #segment for link inertia
        inertial_tag = adom.createElement("inertial")
        mass_tag = adom.createElement("mass")
        mass = np.pi * (self.link_radius * self.link_radius) * self.link_length
        mass_tag.setAttribute("value", str(mass))
        inertia_tag = adom.createElement("inertia")
        inertia_tag.setAttribute("ixx", "0.03")
        inertia_tag.setAttribute("iyy", "0.03")
        inertia_tag.setAttribute("izz", "0.03")
        inertia_tag.setAttribute("ixy", "0")
        inertia_tag.setAttribute("ixz", "0")
        inertia_tag.setAttribute("iyz", "0")

        #merge
        inertial_tag.appendChild(mass_tag)
        inertial_tag.appendChild(inertia_tag)
        link_tag.appendChild(inertial_tag)
        return link_tag

    def to_joint_xml(self, adom):
        joint_tag = adom.createElement("joint")
        joint_tag.setAttribute("name", self.name + "_to_" + self.parent_name)
        if self.joint_type >= 0.5:
            joint_tag.setAttribute("type", "revolute")
        else:
            joint_tag.setAttribute("type", "fixed")

        #parent_segmentation
        parent_tag = adom.createElement("parent")
        parent_tag.setAttribute("link", str(self.parent_name))

        #child_segmentation
        child_tag = adom.createElement("child")
        child_tag.setAttribute("link", str(self.name))

        #axis segment
        axis_tag = adom.createElement("axis")
        if self.joint_axis_xyz <= 0.33:
            axis_tag.setAttribute("xyz", "1 0 0")
        if self.joint_axis_xyz > 0.33 and self.joint_axis_xyz <= 0.66:
            axis_tag.setAttribute("xyz", "0 1 0")
        if self.joint_axis_xyz > 0.66:
            axis_tag.setAttribute("xyz", "0 0 1")

        #limit segment
        limit_tag = adom.createElement("limit")
        limit_tag.setAttribute("effort","1")
        limit_tag.setAttribute("lower","0")
        limit_tag.setAttribute("upper","1")
        limit_tag.setAttribute("velocity","1")

        #origin segment
        origin_tag = adom.createElement("origin")

        rpy1 = self.joint_origin_rpy_1 * self.sibling_ind
        
        rpy = str(rpy1) + " " + str(self.joint_origin_rpy_2) + " " + str(self.joint_origin_rpy_3)
        origin_tag.setAttribute("rpy", rpy)
        xyz = str(self.joint_origin_xyz_1) + " " + str(self.joint_origin_xyz_2) + " " + str(self.joint_origin_xyz_3)
        origin_tag.setAttribute("xyz", xyz)

        #merge
        joint_tag.appendChild(parent_tag)
        joint_tag.appendChild(child_tag)
        joint_tag.appendChild(axis_tag)
        joint_tag.appendChild(limit_tag)
        joint_tag.appendChild(origin_tag)

        return joint_tag









