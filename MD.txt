from openmm.app import *
from openmm import *
from openmm.unit import *
from sys import stdout
from tqdm.notebook import tqdm  # Progress bar para Jupyter/Colab

# Carrega estrutura e prepara simulação
pdb = PDBFile('human_aquaporin_4CSK_membrane.pdb')
forcefield = ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
system = forcefield.createSystem(pdb.topology, nonbondedMethod=PME,
        nonbondedCutoff=1*nanometer, constraints=HBonds)
integrator = LangevinMiddleIntegrator(310*kelvin, 1/picosecond, 0.002*picoseconds)
simulation = Simulation(pdb.topology, system, integrator)
simulation.context.setPositions(pdb.positions)
simulation.minimizeEnergy()

# Adiciona os "reporters"
simulation.reporters.append(PDBReporter('output.pdb', 5000))
simulation.reporters.append(DCDReporter('output.dcd', 5000))
simulation.reporters.append(StateDataReporter(stdout, 5000, step=True,
        potentialEnergy=True, temperature=True))

# Simula com barra de progresso
total_steps = 100000
step_size = 5000
for _ in tqdm(range(0, total_steps, step_size), desc="Simulando", unit="step"):
    simulation.step(step_size)
