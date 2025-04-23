from IPython.display import clear_output
from tqdm.notebook import tqdm
import time
import subprocess

# Lista de etapas com comandos e descrições
install_steps = [
    ("Instalando Condacolab", "!pip install -q condacolab"),
    ("Executando condacolab.install()", "import condacolab; condacolab.install()"),
    ("Instalando OpenMM", "!conda install -c conda-forge openmm -y -q"),
    ("Instalando Plotly", "!conda install -c plotly plotly -y -q"),
    ("Instalando Kaleido", "!pip install -U kaleido -q"),
    ("Instalando MDTraj", "!conda install -c conda-forge mdtraj -y -q"),
    ("Instalando MDAnalysis", "!pip install MDAnalysis -q"),
    ("Instalando py3Dmol", "!pip install py3Dmol -q"),
    ("Instalando Biopython", "!pip install biopython -q"),
]
def run_command(description, command):
    tqdm.write(f"🔧 {description}...")
    if command.startswith("!"):
        subprocess.run(command[1:], shell=True)
    else:
        exec(command)

# Executa cada etapa com barra de progresso
with tqdm(total=len(install_steps), desc="Instalando pacotes", bar_format="{l_bar}{bar} {n_fmt}/{total_fmt}") as pbar:
    for description, command in install_steps:
        run_command(description, command)
        pbar.update(1)
        time.sleep(0.3)  # só pra dar tempo de ver a barra se movendo

print("✅ Todos os pacotes foram instalados com sucesso!")
