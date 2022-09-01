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
BuildRequires:  jbigkit-devel
BuildRequires:  libwebp-devel
BuildRequires:  libzstd-static


%description
Software to emulate Wii U games and applications on PC

%prep
%{__git} clone --recursive https://github.com/cemu-project/Cemu ./
%{__git} clone https://github.com/nezd5553/Cemu-git-copr


%build
cmake -S . -B build -DCMAKE_BUILD_TYPE=release -DCMAKE_C_COMPILER=/usr/bin/gcc -DCMAKE_CXX_COMPILER=/usr/bin/g++ -G Ninja
cmake --build build


%install
mkdir -p %{buildroot}/opt/Cemu
cp -r %{_builddir}/bin/* %{buildroot}/opt/Cemu

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
cp %{_builddir}/src/resource/logo_icon.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/info.cemu.Cemu.png

mkdir -p %{buildroot}%{_bindir}
cp %{_builddir}/Cemu-git-copr/run-Cemu.sh %{buildroot}%{_bindir}/cemu
chmod +x %{buildroot}%{_bindir}/cemu

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
* Thu Sep 1 2022 Max Fletcher <mfletcher@ucsb.edu>
- Initial version
