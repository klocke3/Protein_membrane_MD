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
```
---

## Como usar
```bash
python membrane_preparation.py -i proteina.pdb -l LIPIDIO -m PADDING -c IONIC_STRENGTH
```
Argumentos:

---

## Flag	Descrição	Exemplo
-i	Arquivo .pdb da proteína	-i aquaporina.pdb
-l	Tipo de lipídio	-l POPC
-m	Padding mínimo (nm)	-m 3.0
-c	Força iônica (mol/L)	-c 0.15


## 🧫 Tipos de Lipídios Suportados

Código	Nome Completo
POPC	1-palmitoil-2-oleoil-sn-glicero-3-fosfocolina
DPPC	1,2-dipalmitoil-sn-glicero-3-fosfocolina
POPE	1-palmitoil-2-oleoil-sn-glicero-3-fosfoetanolamina
DLPC	1,2-dilauroil-sn-glicero-3-fosfocolina
DMPC	1,2-dimiristoil-sn-glicero-3-fosfocolina
DSPC	1,2-distearoil-sn-glicero-3-fosfocolina
DOPC	1,2-dioleoil-sn-glicero-3-fosfocolina
POPS	1-palmitoil-2-oleoil-sn-glicero-3-fosfoserina
POPG	1-palmitoil-2-oleoil-sn-glicero-3-fosfoglicerol
CHOL	Colesterol

## ℹ️ Esses lipídios estão disponíveis no campo de força amber14/lipid17.xml do OpenMM.

## 💾 Saída
O script gera um arquivo .pdb com a estrutura da proteína embebida em uma membrana, solvatada e neutralizada, pronta para simulação.
Exemplo de saída: proteina_membrana.pdb


