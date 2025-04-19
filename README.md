# 🧬 membrane_preparation.py

Este script prepara uma estrutura de proteína inserida em uma **bicamada lipídica** (membrana) com **solvatação iônica**, usando o **OpenMM**. Ideal para simulações de dinâmica molecular com proteínas de membrana.

---

## 🚀 Requisitos

- Python 3.8+
- OpenMM 8+
- Arquivo `.pdb` da proteína

---

## 📦 Instalação dos pacotes necessários

Você pode instalar o OpenMM com:

```bash
pip install openmm
---
Código | Nome Completo
POPC | 1-palmitoil-2-oleoil-sn-glicero-3-fosfocolina
DPPC | 1,2-dipalmitoil-sn-glicero-3-fosfocolina
POPE | 1-palmitoil-2-oleoil-sn-glicero-3-fosfoetanolamina
DLPC | 1,2-dilauroil-sn-glicero-3-fosfocolina
DMPC | 1,2-dimiristoil-sn-glicero-3-fosfocolina
DSPC | 1,2-distearoil-sn-glicero-3-fosfocolina
DOPC | 1,2-dioleoil-sn-glicero-3-fosfocolina
POPS | 1-palmitoil-2-oleoil-sn-glicero-3-fosfoserina
POPG | 1-palmitoil-2-oleoil-sn-glicero-3-fosfoglicerol
CHOL | Colesterol
