#!/bin/bash

if [[ ! -d "$HOME/.local/share/Cemu" ]]
then
    echo "Copying Cemu files to user directory"
    cp -R /opt/Cemu "$HOME/.local/share"
    chown -R "$USER":"$USER" "$HOME/.local/share/Cemu"
    chmod -R 750 "$HOME/.local/share/Cemu"
    chmod +x "$HOME/.local/share/Cemu/Cemu"
fi

# Replace Cemu executable if it has updated
cmp --silent /opt/Cemu/Cemu "$HOME/.local/share/Cemu/Cemu" || ( cp -v /opt/Cemu/Cemu "$HOME/.local/share/Cemu" && chmod +x "$HOME/.local/share/Cemu/Cemu" )

cd "$HOME/.local/share/Cemu"
./Cemu
