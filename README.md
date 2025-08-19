# Instalar sudo
1. su -
2. apt update
3. apt install sudo
4. usermod -aG sudo seu_usuario

# Instalar firefox e git
1. sudo apt update
2. sudo apt install firefox-esr
3. sudo apt install git

# Clonar repositorio
git clone git@github.com:mariopbj/MeuSetup.git

# Executar installing.sh
1. chmod +x ~/MeuSetup/scripts/installing.sh
2. ~/MeuSetup/scripts/installing.sh

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
