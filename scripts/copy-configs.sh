echo "Copiando configurações (dotfiles)..."

# i3
mkdir -p ~/.config/i3
cp -r ~/MeuSetup/i3/.xinitrc ~/
cp -r ~/MeuSetup/i3/config ~/.config/i3/

# kitty
mkdir -p ~/.config/kitty
cp -r ~/MeuSetup/kitty/ ~/.config/

# polybar
mkdir -p ~/.config/polybar
cp -r ~/MeuSetup/polybar/config.ini ~/.config/polybar/

# rofi
sudo mkdir -p /usr/share/rofi/themes
sudo cp -r ~/MeuSetup/rofi/rounded* /usr/share/rofi/themes/
mkdir -p ~/.config/rofi
cp -r ~/MeuSetup/rofi/config.rasi ~/.config/rofi/

# picom
mkdir -p ~/.config/picom
cp -r ~/MeuSetup/picom/picom.conf ~/.config/picom/

# neofetch
cp -r ~/MeuSetup/neofetch/ ~/.config/

# nvim
cp -r ~/MeuSetup/nvim/ ~/.config/

# wallpapers
mkdir -p ~/WallPapers

# .bashrc
sudo cp ~/MeuSetup/bashrc/.bashrc ~/

echo "Pronto. Sistema configurado."