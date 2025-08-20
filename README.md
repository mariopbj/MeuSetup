# Instalar sudo
1. su -
2. apt update
3. apt install sudo
4. usermod -aG sudo seu_usuario

# Instalar o git
1. sudo apt update
2. sudo apt install git

# Clonar repositorio
git clone https://github.com/mariopbj/MeuSetup.git

# Executar installing.sh
1. chmod +x ~/MeuSetup/scripts/installing.sh
2. ~/MeuSetup/scripts/installing.sh

# Abra o i3
startx

# Instalar manualmente:

## Brave
## Polybar
## JetBrainsMono Nerd Font Mono
1. mkdir NerdFont
2. unzip NOME_DA_FONTE
3. mkdir -p ~/.local/share/fonts
4. cp JetBrainsMonoNerdFontMono-*.ttf ~/.local/share/fonts/
5. fc-cache -fv

# Executar copy-configs.sh
1. chmod +x ~/MeuSetup/scripts/copy-configs.sh
2. ~/MeuSetup/scripts/copy-configs.sh