import argparse
from openmm.app import PDBFile, Modeller, ForceField, Simulation
from openmm import unit, app
from pathlib import Path

# Argumentos CLI
parser = argparse.ArgumentParser(description="Prepara uma proteína em membrana com OpenMM.")
parser.add_argument('-i', '--input', required=True, help='Arquivo PDB da proteína de entrada')
parser.add_argument('-l', '--lipid', default='POPC', help='Tipo de lipídio (ex: POPC, DPPC)')
parser.add_argument('-m', '--minimumPadding', type=float, default=1.0, help='Distância mínima (nm) entre proteína e membrana')
parser.add_argument('-c', '--ionicStrength', type=float, default=0.15, help='Força iônica (mol/L)')
args = parser.parse_args()

# Carregar proteína
pdb = PDBFile(args.input)
modeller = Modeller(pdb.topology, pdb.positions)
modeller.addHydrogens()

# Campo de força
forcefield = ForceField('amber14-all.xml', 'amber14/tip3p.xml', 'amber14/lipid17.xml')

# Adicionar membrana
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

# Criar sistema
system = forcefield.createSystem(modeller.topology, nonbondedMethod=app.PME,
                                 nonbondedCutoff=1.0 * unit.nanometer, constraints=app.HBonds)

# Nome de saída
output_filename = Path(args.input).stem + "_membrana.pdb"
with open(output_filename, 'w') as f:
    PDBFile.writeFile(modeller.topology, modeller.positions, f)

print(f"✅ Estrutura salva como {output_filename}")

# Criar README.md dinâmico
readme = f"""# 🧬 Simulação com Membrana: {args.input}

Este sistema foi preparado automaticamente com os seguintes parâmetros:

| Parâmetro       | Valor                 |
|----------------|------------------------|
| Proteína       | `{args.input}`         |
| Lipídio        | `{args.lipid}`         |
| Padding        | `{args.minimumPadding} nm` |
| Força Iônica   | `{args.ionicStrength} mol/L` |
| Campo de força | `amber14-all + lipid17`|

💾 Arquivo de saída: `{output_filename}`

## 🧫 Descrição

A proteína foi centralizada e inserida em uma bicamada lipídica do tipo `{args.lipid}` com uma margem de solvatação de `{args.minimumPadding} nm`, e a solução foi neutralizada com íons (Na⁺, Cl⁻) para uma força iônica de `{args.ionicStrength} M`.

Para mais informações, consulte o [repositório do OpenMM](https://github.com/openmm/openmm/wiki/Membrane-Systems).
"""

with open("README.md", "w") as f:
    f.write(readme)

print("📘 README.md gerado com sucesso!")
