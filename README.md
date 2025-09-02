# Instalar sudo
1. `su -`
2. `apt update`
3. `apt install sudo`
4. `usermod -aG sudo seu_usuario`

# Instalar o git
1. `sudo apt update`
2. `sudo apt install git`

# Clonar repositorio
`git clone https://github.com/mariopbj/MeuSetup.git`

# Executar installing.sh
1. `chmod +x ~/MeuSetup/scripts/installing.sh`
2. `~/MeuSetup/scripts/installing.sh`

# Abrir o i3
`startx`

# Instalar manualmente:

## [Brave](https://brave.com/pt-br/)
## [Polybar](https://github.com/polybar/polybar)
1. `cd ~/Downloads`
2. `tar -xzf polybar-3.7.2.tar.gz`
3. `cd polybar-3.7.2`
4. `mkdir build`
5. `cd build`
6. `cmake ..`
7. `make -j$(nproc)`
8. `sudo make install`

## [JetBrainsMono Nerd Font Mono](https://www.nerdfonts.com/font-downloads)
1. `mkdir NerdFont`
2. `unzip NOME_DA_FONTE`
3. `mkdir -p ~/.local/share/fonts`
4. `cp JetBrainsMonoNerdFontMono-*.ttf ~/.local/share/fonts/`
5. `fc-cache -fv`

## [Neovim](https://github.com/neovim/neovim/blob/master/INSTALL.md)
1. `Download nvim-linux-x86_64.tar.gz`
2. `tar xzvf nvim-linux-x86_64.tar.gz`
3. `sudo mv nvim-linux-x86_64 /opt/nvim`
4. `sudo ln -s /opt/nvim/bin/nvim /usr/local/bin/nvim`

# Executar copy-configs.sh
1. `chmod +x ~/MeuSetup/scripts/copy-configs.sh`
2. `~/MeuSetup/scripts/copy-configs.sh`