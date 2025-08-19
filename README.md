# Instalar sudo
1. su -
2. apt update
3. apt install sudo
4. usermod -aG sudo seu_usuario

# Instalar firefox e git
sudo apt update
sudo apt install firefox-esr
sudo apt install git

# Clonar repositorio
git clone 

# Executar installing.sh
chmod +x ~/MeuSetup/scripts/installing.sh
~/MeuSetup/scripts/installing.sh

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
chmod +x ~/MeuSetup/scripts/copy-configs.sh
~/MeuSetup/scripts/copy-configs.sh