name: i3lock-color
Version: 2.12.c.1
Release: 1%{?dist}
Summary: improved improved screen locker - "the ricing fork of i3lock"

License: BSD
URL: https://github.com/PandorasFox/i3lock-color

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

BuildRequires: git
BuildRequires: cairo-devel libev libev-devel libjpeg-turbo pam-devel xcb-util-devel xcb-util-image xcb-util-image-devel
BuildRequires: autoconf automake make gcc-c++

Provides:  i3lock-color
Obsoletes: i3lock

%description
i3lock is a simple screen locker like slock. After starting it, you will see a white screen (you can configure the color/an image). You can return to your screen by entering your password.

%prep
rm -rf i3lock-color
git clone https://github.com/PandorasFox/i3lock-color --recursive
cd i3lock-color
git reset --hard e07c3f0

%build
cd i3lock-color
autoreconf -i
./configure --prefix %{_prefix} --sysconfdir=%{_sysconfdir}
make -j

%install
cd i3lock-color
%make_install

%check

%files
%{_bindir}/i3lock
%{_mandir}/man1/i3lock.1.*
%{_sysconfdir}/pam.d/i3lock

%doc i3lock-color/README.md i3lock-color/i3lock.1 i3lock-color/CHANGELOG

%license i3lock-color/LICENSE

