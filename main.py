import pybullet as p
import time
import pybullet_data as pd
from src import creature
from src import genome as genlib

p.connect(p.GUI)
p.setPhysicsEngineParameter(enableFileCaching=0)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)
p.setGravity(0, 0, -10)

c = creature.Creature(gene_count=10)
dna = genlib.Genome.from_csv('./data/9_elite.csv')
c.set_dna(dna)

with open("./data/creature.urdf", "w") as f:
    c.get_expanded_links()
    f.write(c.to_xml())

cid = p.loadURDF("./data/creature.urdf")

p.setRealTimeSimulation(1)
c.update_position([0,0,0])

p.resetBasePositionAndOrientation(cid, [0,0,3], [0,0,0,1])

while True:
    for jid in range(p.getNumJoints(cid)):
        m = c.get_motors()[jid]
        p.setJointMotorControl2(cid,jid,
                                controlMode = p.VELOCITY_CONTROL,
                                targetVelocity = m.get_output(),
                                force = 5)
        new_pos, orn = p.getBasePositionAndOrientation(cid)
        c.update_position(new_pos)
        print("Distance Travelled: " + str(c.get_distance_travelled()))
    time.sleep(0.1)




