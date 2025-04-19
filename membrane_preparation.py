import argparse
from openmm.app import PDBFile, Modeller, ForceField, Simulation
from openmm import unit, app
from pathlib import Path
import time
import sys

# Função de animação de carregamento para cada etapa
def loading_animation(step_name, steps_total, delay=0.5):
    spin = ['⏳', '🔄', '🔃', '🔁']
    for i in range(steps_total):  # Cada etapa
        sys.stdout.write(f"\r{spin[i % 4]} {step_name} ({i+1}/{steps_total})")
        sys.stdout.flush()
        time.sleep(delay)

# Argumentos CLI
parser = argparse.ArgumentParser(description="Prepara uma proteína em membrana com OpenMM.")
parser.add_argument('-i', '--input', required=True, help='Arquivo PDB da proteína de entrada')
parser.add_argument('-l', '--lipid', default='DPPC', help='Tipo de lipídio (ex: POPC, DPPC)')
parser.add_argument('-m', '--minimumPadding', type=float, default=1.0, help='Distância mínima (nm) entre proteína e membrana')
parser.add_argument('-c', '--ionicStrength', type=float, default=0.15, help='Força iônica (mol/L)')
args = parser.parse_args()

# Etapa 1: Carregar proteína
loading_animation("Carregando proteína", 5)  # 5 iterações para o carregamento
pdb = PDBFile(args.input)
modeller = Modeller(pdb.topology, pdb.positions)
modeller.addHydrogens()
sys.stdout.write(f"\r✅ Proteína carregada e hidrogênios adicionados.\n")
sys.stdout.flush()

# Etapa 2: Definir campo de força
loading_animation("Definindo campo de força", 5)
forcefield = ForceField('amber14-all.xml', 'amber14/tip3p.xml', 'amber14/lipid17.xml')
sys.stdout.write(f"\r✅ Campo de força definido.\n")
sys.stdout.flush()

# Etapa 3: Adicionar membrana lipídica
loading_animation("Adicionando membrana lipídica", 5)
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
sys.stdout.write(f"\r✅ Membrana {args.lipid} adicionada.\n")
sys.stdout.flush()

# Etapa 4: Criar sistema de simulação
loading_animation("Criando sistema de simulação", 5)
system = forcefield.createSystem(modeller.topology, nonbondedMethod=app.PME,
                                 nonbondedCutoff=1.0 * unit.nanometer, constraints=app.HBonds)
sys.stdout.write(f"\r✅ Sistema de simulação criado.\n")
sys.stdout.flush()

# Etapa 5: Salvar o arquivo PDB final
loading_animation("Salvando estrutura final", 5)
output_filename = Path(args.input).stem + "_membrane.pdb"
with open(output_filename, 'w') as f:
    PDBFile.writeFile(modeller.topology, modeller.positions, f)

# Finalizando
sys.stdout.write(f"\r✅ Estrutura salva como {output_filename}\n")
sys.stdout.flush()

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
