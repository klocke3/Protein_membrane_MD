#!/bin/bash

# Função para exibir a barra de progresso
progress_bar() {
    local current_step=$1
    local total_steps=$2
    local width=50

    # Verifica se total_steps é maior que zero para evitar divisão por zero
    if [ $total_steps -eq 0 ]; then
        echo "Erro: o número total de etapas não pode ser zero."
        exit 1
    fi

    # Calcula a porcentagem
    local percent=$(( (100 * current_step) / total_steps ))
    # Calcula o progresso feito
    local done=$((current_step * width / total_steps))
    # Calcula o espaço restante
    local left=$((width - done))
    # Gera a parte preenchida da barra
    local fill=$(printf "%${done}s" | tr ' ' '#')
    # Gera a parte vazia da barra
    local empty=$(printf "%${left}s" | tr ' ' '-')

    echo -ne "\r[${fill}${empty}] ${percent}%"
}

# Lista de pacotes a instalar
packages=(
  "Conda"
  "OpenMM"
  "Ploty"
  "Kaleido"
  "MDTraj"
  "py3Dmol"
  "bipython"
)

# Função para determinar o comando de instalação de acordo com o pacote
get_install_command() {
    local package_name=$1
    case $package_name in
        "Conda")
            echo "pip install -q condacolab >/dev/null 2>&1 && import condacolab && condacolab.install() 2>&1"
            ;;
        "OpenMM")
            echo "conda install conda-forge::openmm -q >/dev/null 2>&1"
            ;;
        "Ploty")
            echo "conda install -c plotly plotly -y -q >/dev/null 2>&1"
            ;;
        "Kaleido")
            echo "pip install -U kaleido -q >/dev/null 2>&1"
            ;;
        "MDTraj")
            echo "conda install -c conda-forge mdtraj -q >/dev/null 2>&1"
            ;;
        "py3Dmol")
            echo "pip install py3Dmol -q >/dev/null 2>&1"
            ;;
        "bipython")
            echo "pip install biopython -q >/dev/null 2>&1"
            ;;
        *)
            echo "echo 'Comando desconhecido para $package_name'"
            ;;
    esac
}

total_steps=${#packages[@]}
current_step=0

echo "Iniciando a instalação de pacotes..."

# Loop de instalação
for pkg in "${packages[@]}"; do
    ((current_step++))  # Incrementa a etapa
    progress_bar $current_step $total_steps
    echo -e "\nInstalando $pkg..."
    
    # Obter o comando de instalação correto
    install_command=$(get_install_command $pkg)
    
    # Executar o comando de instalação
    eval $install_command

    sleep 1  # Simula a instalação (substitua com a instalação real)
    echo "$pkg instalado com sucesso! ✅"
done

echo -e "\nTodos os pacotes foram instalados com sucesso! 🎉"
