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

## Exemplo:
```bash
python membrane_preparation.py -i entrada.pdb -l LIPID -m PADDING -c IONIC
