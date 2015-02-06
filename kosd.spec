Name:		kosd
Version:	0.8.1
Release:	3
Summary:	An application showing OSD to respond volume buttons
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.kde-apps.org/content/show.php?content=81457
Source:		http://www.kde-apps.org/CONTENT/content-files/81457-%{name}-%{version}.tar.bz2
Patch0:		kosd-0.8.1-ru.patch
BuildRequires:	kdebase4-workspace-devel
Obsoletes:	kde3-kvolumeosd < %{version}
Obsoletes:	kde3-kosd < %{version}

%description
KOSD is a simple KDE application that runs in the background and
responds to volume buttons by showing a little OSD. It delegates the
actual job of adjusting the volume to KMix.

%prep
%setup -q
%patch0 -p1 -b .ru

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

rm -fr %{buildroot}%{_kde_includedir} %{buildroot}%{_kde_libdir}/*.so

%find_lang %{name} --with-html

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde_libdir}/*.so.*
%{_kde_libdir}/kde4/*.so
%{_kde_datadir}/config.kcfg/kosd.kcfg
%{_kde_services}/kcm_kosd.desktop
%{_kde_services}/kded/*.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kosd.xml


