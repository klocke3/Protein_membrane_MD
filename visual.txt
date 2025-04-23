from google.colab import files
import MDAnalysis as mda
from MDAnalysis.coordinates import PDB
import py3Dmol
import io
import ipywidgets as widgets
from IPython.display import display

# Carrega estrutura e trajetória
u = mda.Universe('/content/analyse1.pdb', '/content/analyse1.dcd')

# Seleciona proteína e água
protein = u.select_atoms('protein')
water = u.select_atoms('resname HOH or resname WAT')
lipids = u.select_atoms('resname POP')

# Gera frames como strings PDB
protein_frames = []
water_frames = []
lipid_frames = []

for ts in u.trajectory:
    buffer_lipid = io.StringIO()
    PDB.PDBWriter(buffer_lipid).write(lipids)
    lipid_frames.append(buffer_lipid.getvalue())
    buffer_lipid.close()

for ts in u.trajectory:
    buffer_protein = io.StringIO()
    PDB.PDBWriter(buffer_protein).write(protein)
    protein_frames.append(buffer_protein.getvalue())
    buffer_protein.close()

    buffer_water = io.StringIO()
    PDB.PDBWriter(buffer_water).write(water)
    water_frames.append(buffer_water.getvalue())
    buffer_water.close()

# Cria visualização
view = py3Dmol.view(width=800, height=600)

# Função para atualizar visualização
def show_frame(i):
    view.removeAllModels()

    view.addModel(protein_frames[i], 'pdb')
    view.setStyle({'model': 0}, {'cartoon': {'color': 'spectrum'}})

    view.addModel(water_frames[i], 'pdb')
    view.setStyle({'model': 1}, {
        'sphere': {
            'color': 'lightblue',
            'radius': 0.5,
            'opacity': 1.0
        }
    })

    view.addModel(lipid_frames[i], 'pdb')
    view.setStyle({'model': 2}, {
        'stick': {
            'radius': 0.15,
            'opacity': 0.5,
            'colorscheme': 'orangeCarbon'
        }
    })
    
    view.zoomTo()
    view.show()

# Botão de seleção de frame
frame_selector = widgets.IntSlider(
    min=0,
    max=len(protein_frames)-1,
    step=1,
    description='Frame:',
    continuous_update=False
)

# Interação com o botão para exibir o frame selecionado
widgets.interact(show_frame, i=frame_selector)

# Exibe o slider
display(frame_selector)
