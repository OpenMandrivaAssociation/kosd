%define oname KOSD

Name: kde3-kosd
Version: 0.2.3
Release: %mkrel 1
Summary: An application showing OSD to respond volume buttons
License: GPLv2+
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.kde-apps.org/content/show.php?content=81457
Source: http://www.kde-apps.org/CONTENT/content-files/81457-%{oname}-%{version}.tar.bz2
BuildRequires: kdelibs-devel
Requires: kde3-kmix
Obsoletes: kde3-kvolumeosd < %version

%description
KOSD is a simple KDE application that runs in the background and
responds to volume buttons by showing a little OSD. It delegates the
actual job of adjusting the volume to KMix.

%prep
%setup -q -n %{oname}

%build
make -f Makefile.cvs
%configure_kde3
%make

%install
rm -rf %buildroot
%makeinstall_std

%find_lang kosd --with-html

mkdir -p %buildroot%_kde3_datadir/applications/kde
mv %buildroot/share/applications/*.desktop %buildroot%_kde3_datadir/applications/kde

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post
%{update_menus}
%update_kde3_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_kde3_icon_cache hicolor
%endif

%files -f kosd.lang
%defattr(-,root,root)
%{_kde3_bindir}/kosd
%{_kde3_appsdir}/kosd
%{_kde3_datadir}/applications/kde/*.desktop
%{_kde3_iconsdir}/hicolor/*/apps/*
