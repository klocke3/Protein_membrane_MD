from openmm.app import PDBFile, Modeller, ForceField, Simulation
from openmm import unit
from openmm import app

# Carregar a proteína a partir de um arquivo PDB (sem usar o PDBFixer)
pdbfile = 'proteina.pdb'  # Substitua com o caminho do seu arquivo PDB
pdb = PDBFile(pdbfile)

# Criar um modelo com a proteína
modeller = Modeller(pdb.topology, pdb.positions)
modeller.addHydrogens()

# Definir o campo de força: Amber14 para a proteína Lipid17 para a membrana
forcefield = ForceField('amber14-all.xml', 'amber14/tip3p.xml', 'amber14/lipid17.xml')

#Define uma membrana entre o eixo XY
modeller.addMembrane(
    forcefield,
    lipidType='DPPC',
    membraneCenterZ=0*unit.nanometer,
    minimumPadding=1.0*unit.nanometer,
    positiveIon='Na+',
    negativeIon='Cl-',
    ionicStrength=0.15*unit.molar,
    neutralize=True
)

# Criar o sistema com a proteína e a água
system = forcefield.createSystem(modeller.topology, nonbondedMethod=app.PME,
                                 nonbondedCutoff=1.0*unit.nanometer, constraints=app.HBonds)


#@title 💾 Salvar sistema solvatado
output_filename = "proteina_membrana.pdb"
with open(output_filename, 'w') as f:
    PDBFile.writeFile(modeller.topology, modeller.positions, f)
files.download(output_filename)
print(f"✅ Estrutura centralizada e solvatada com margem salva como {output_filename}")
