!pip install git+https://github.com/openmm/pdbfixer.git

#@title 📦 Instalar PDBFixer no Google Colab

#@title 📦 Upload do PDB
from google.colab import files
from pdbfixer import PDBFixer
from openmm.app import PDBFile


fixer = PDBFixer(filename='luciferase.pdb')
fixer.findMissingResidues()
fixer.findMissingAtoms()
fixer.addMissingAtoms()
fixer.addMissingHydrogens(pH=7.0)

with open('arquivo_corrigido.pdb', 'w') as f:
    PDBFile.writeFile(fixer.topology, fixer.positions, f)

# Salvar a estrutura corrigida
output_filename = "corrigido_com_pdbfixer.pdb"
with open(output_filename, 'w') as f:
    PDBFile.writeFile(fixer.topology, fixer.positions, f)

# Baixar o arquivo corrigido
from google.colab import files
files.download(output_filename)

print(f"✅ Estrutura corrigida e salva como {output_filename}")
