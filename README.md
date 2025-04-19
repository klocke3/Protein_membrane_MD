# 🧬 Preparação de uma membrana bilipídica contendo uma proteína utilizando o OpenMM

Este script prepara uma estrutura de proteína inserida em uma **bicamada lipídica** (membrana) com **solvatação iônica**, usando o **OpenMM**. Ideal para simulações de dinâmica molecular com proteínas de membrana. Neste caso, será construída uma membrana no plano XY.

Para centralizar a proteína, use o servidor: https://opm.phar.umich.edu/ppm_server2

Após gerar o arquivo pdb, faça o download e adicione na pasta contendo o arquivo membrane_preparation.py

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
Faça o donwload do arquivo membrane_preparation.py. Execute o comando abaixo na mesma pasta que contém o arquivo pdb da proteína:
```bash
python membrane_preparation.py -i PROTEIN -l LIPID -m PADDING -c IONIC_STRENGTH
```
---

Argumentos:

| Parâmetro       | Valor                 |
|----------------|------------------------|
| -i [PROTEIN]       | Arquivo proteína pdb        |
| -l [LIPID]       | Código lipídeo         |
| -m [PADDING]        | Ajuste tamanho da membrana (nm) |
| -c [IONIC_STRENGTH]   | Força iônica (mol/L) |

---

## Flag	Descrição	Exemplo
```
python membrane_preparation.py -i aquaporina.pdb -l POPC -m 3.0 -c 0.15
```
## 🧫 Tipos de Lipídios Suportados

| **Código** | **Nome Completo**                              |
|------------|------------------------------------------------|
| POPC       | 1-palmitoil-2-oleoil-sn-glicero-3-fosfocolina   |
| POPE       | 1-palmitoil-2-oleoil-sn-glicero-3-fosfoetanolamina |
| DLPC       | 1,2-dilauroil-sn-glicero-3-fosfocolina          |
| DLPE       | 1,2-dilauroil-sn-glicero-3-fosfoetanolamina     |
| DMPC       | 1,2-dimiristoil-sn-glicero-3-fosfocolina        |
| DOPC       | 1,2-dioleoil-sn-glicero-3-fosfocolina           |
| DPPC       | 1,2-dipalmitoil-sn-glicero-3-fosfocolina        |


## ℹ️ Esses lipídios estão disponíveis no campo de força amber14/lipid17.xml do OpenMM.

## 💾 Saída
O script gera um arquivo .pdb com a estrutura da proteína embebida em uma membrana, solvatada e neutralizada, pronta para simulação.
Exemplo de saída: proteina_membrana.pdb


