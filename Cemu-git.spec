%global timestamp %(date +%%Y%%m%%d%%H%%M%%S)
Name:           Cemu-git
Version:        %{timestamp}
Release:        1%{?dist}
Summary:        Cemu is a Wii U emulator (Git Version)

License:        MPL-2.0
URL:            https://cemu.info

BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  ninja-build
BuildRequires:  nasm
BuildRequires:  kernel-headers
BuildRequires:  gtk3-devel
BuildRequires:  libsecret-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  systemd-devel
BuildRequires:  freeglut-devel
BuildRequires:  perl-core
BuildRequires:  zlib-devel
BuildRequires:  cubeb-devel
BuildRequires:  SDL2-devel
BuildRequires:  jbigkit-devel
BuildRequires:  libwebp-devel
BuildRequires:  libzstd-static


%description
Software to emulate Wii U games and applications on PC

%prep
%{__git} clone --recursive https://github.com/cemu-project/Cemu ./
%{__git} clone https://github.com/nezd5553/Cemu-git-copr

patch --verbose %{_builddir}/vcpkg.json %{_builddir}/Cemu-git-copr/vcpkg.json.patch


%build
cmake -S . -B build -DCMAKE_BUILD_TYPE=release -DPORTABLE=OFF -DCMAKE_C_COMPILER=/usr/bin/gcc -DCMAKE_CXX_COMPILER=/usr/bin/g++ -G Ninja
cmake --build build


%install
mkdir -p %{buildroot}/opt/Cemu
cp -r %{_builddir}/bin/* %{buildroot}/opt/Cemu

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
cp %{_builddir}/src/resource/logo_icon.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/info.cemu.Cemu.png

mkdir -p %{buildroot}%{_bindir}
cp %{_builddir}/Cemu-git-copr/run-Cemu.sh %{buildroot}%{_bindir}/Cemu
chmod +x %{buildroot}%{_bindir}/Cemu

mkdir -p %{buildroot}%{_datadir}/applications
cp %{_builddir}/dist/linux/info.cemu.Cemu.desktop %{buildroot}%{_datadir}/applications/


%files
%license LICENSE.txt
%doc README.md

/opt/Cemu/*
%{_datadir}/icons/hicolor/128x128/apps/info.cemu.Cemu.png
%{_bindir}/cemu
%{_datadir}/applications/info.cemu.Cemu.desktop


%changelog
* Sat Nov 5 2022 Max Fletcher <jdhfxjx@outlook.com>
- Fix capitalization of Cemu executable

* Fri Oct 14 2022 Max Fletcher <jdhfxjx@outlook.com>
- Use system SDL2

* Wed Oct 12 2022 Max Fletcher <jdhfxjx@outlook.com>
- Turn off portable mode

* Sat Sep 24 2022 Max Fletcher <jdhfxjx@outlook.com>
- Remove public release flag

* Mon Sep 19 2022 Max Fletcher <jdhfxjx@outlook.com>
- Use public release flag

* Thu Sep 1 2022 Max Fletcher <jdhfxjx@outlook.com>
- Initial version
