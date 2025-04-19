import argparse
from openmm.app import PDBFile, Modeller, ForceField, Simulation
from openmm import unit, app
import os

# === Argumentos de linha de comando ===
parser = argparse.ArgumentParser(
    description='🧬 Prepara uma proteína inserida em uma membrana lipídica solvatada usando OpenMM.'
)

parser.add_argument(
    '-i', '--input', required=True,
    help='🧾 Arquivo PDB da proteína (ex: aquaporina.pdb)'
)

parser.add_argument(
    '-l', '--lipid', default='POPC',
    help='🧫 Tipo de lipídeo da bicamada (ex: POPC, DPPC, POPE, etc). Padrão: POPC'
)

parser.add_argument(
    '-m', '--minimumPadding', type=float, default=3.0,
    help='📏 Distância mínima (em nm) entre a proteína e os lipídios. Padrão: 3.0 nm'
)

parser.add_argument(
    '-c', '--ionicStrength', type=float, default=0.15,
    help='🧪 Força iônica do sistema (em mol/L). Padrão: 0.15 M'
)

args = parser.parse_args()

# === Carregar a proteína do arquivo PDB ===
print(f"📂 Carregando estrutura: {args.input}")
pdb = PDBFile(args.input)
modeller = Modeller(pdb.topology, pdb.positions)
modeller.addHydrogens()

# === Definir campos de força ===
print(f"🧬 Aplicando força: amber14 + lipid17")
forcefield = ForceField(
    'amber14-all.xml',
    'amber14/tip3p.xml',
    'amber14/lipid17.xml'
)

# === Inserir em membrana lipídica ===
print(f"🧫 Adicionando membrana: {args.lipid}")
modeller.addMembrane(
    forcefield,
    lipidType=args.lipid,
    membraneCenterZ=0 * unit.nanometer,
    minimumPadding=args.minimumPadding * unit.nanometer,
    positiveIon='Na+',
    negativeIon='Cl-',
    ionicStrength=args.ionicStrength * unit.molar,
    neutralize=True
)

# === Criar sistema ===
print("⚙️  Criando sistema com PME e restrições em ligações de hidrogênio...")
system = forcefield.createSystem(
    modeller.topology,
    nonbondedMethod=app.PME,
    nonbondedCutoff=1.0 * unit.nanometer,
    constraints=app.HBonds
)

# === Salvar saída ===
base_name = os.path.splitext(os.path.basename(args.input))[0]
output_filename = f"{base_name}_membrana.pdb"

with open(output_filename, 'w') as f:
    PDBFile.writeFile(modeller.topology, modeller.positions, f)

print(f"✅ Estrutura com membrana salva como: {output_filename}")
