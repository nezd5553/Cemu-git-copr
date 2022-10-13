#!/bin/bash

# migrate old files to new location
if [ ! -d "$HOME/.config/Cemu" ]; then
  mkdir "$HOME/.config/Cemu"
fi

if [ -f "$HOME/.local/share/Cemu/settings.xml" ]; then
  mv -b "$HOME/.local/share/Cemu/settings.xml" "$HOME/.config/Cemu"
fi

if [ -d "$HOME/.local/share/Cemu/controllerProfiles" ]; then
  mv -b "$HOME/.local/share/Cemu/controllerProfiles" "$HOME/.config/Cemu"
fi

if [ -d "$HOME/.local/share/Cemu/gameProfiles" ]; then
  mv -b "$HOME/.local/share/Cemu/gameProfiles" "$HOME/.config/Cemu"
fi

if [ -d "$HOME/.local/share/Cemu/debugger" ]; then
  mv -b "$HOME/.local/share/Cemu/debugger" "$HOME/.config/Cemu"
fi

if [ -f "$HOME/.local/share/Cemu/network_services.xml" ]; then
  mv -b "$HOME/.local/share/Cemu/network_services.xml" "$HOME/.config/Cemu"
fi

if [ -d "$HOME/.local/share/Cemu/shaderCache" ]; then
  mv -b "$HOME/.local/share/Cemu/shaderCache" "$HOME/.cache/Cemu"
fi

# migrate old files to new location
if [ ! -d "$HOME/.config/Cemu" ]; then
  mkdir "$HOME/.config/Cemu"
fi

if [ -f "$HOME/.local/share/Cemu/settings.xml" ]; then
  mv -b "$HOME/.local/share/Cemu/settings.xml" "$HOME/.config/Cemu"
fi

if [ -d "$HOME/.local/share/Cemu/controllerProfiles" ]; then
  mv -b "$HOME/.local/share/Cemu/controllerProfiles" "$HOME/.config/Cemu"
fi

if [ -d "$HOME/.local/share/Cemu/gameProfiles" ]; then
  mv -b "$HOME/.local/share/Cemu/gameProfiles" "$HOME/.config/Cemu"
fi

if [ -d "$HOME/.local/share/Cemu/debugger" ]; then
  mv -b "$HOME/.local/share/Cemu/debugger" "$HOME/.config/Cemu"
fi

if [ -f "$HOME/.local/share/Cemu/network_services.xml" ]; then
  mv -b "$HOME/.local/share/Cemu/network_services.xml" "$HOME/.config/Cemu"
fi

if [ -f "$HOME/.local/share/Cemu/Cemu" ]; then
  rm "$HOME/.local/share/Cemu/Cemu"
fi

if [ -f "$HOME/.local/share/Cemu/Cemu_release" ]; then
  rm "$HOME/.local/share/Cemu/Cemu_release"
fi

/opt/Cemu/Cemu_release
