%define oname KOSD

Name: kosd
Version: 0.4.1
Release: %mkrel 1
Summary: An application showing OSD to respond volume buttons
License: GPLv2+
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://www.kde-apps.org/content/show.php?content=81457
Source: http://www.kde-apps.org/CONTENT/content-files/81457-%{name}-%{version}.tar.gz
Patch0: kosd-0.4-fix-build.patch
BuildRequires: kdebase4-workspace-devel
Requires: kmix
Obsoletes: kde3-kvolumeosd < %version
Obsoletes: kde3-kosd < %version

%description
KOSD is a simple KDE application that runs in the background and
responds to volume buttons by showing a little OSD. It delegates the
actual job of adjusting the volume to KMix.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%find_lang kosd --with-html

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
%{_kde_bindir}/*
