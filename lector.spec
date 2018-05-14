Name:       lector
Version:    0.4
Release:    1%{?dist}
Summary:    Qt based Ebook reader 
License:    GPLv3 and MIT

URL:        https://github.com/BasioMeusPuga/Lector
Source0:    %{url}/archive/%{version}/Lector-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-qt5
BuildRequires:  python3-requests
BuildRequires:  python3-poppler-qt5

Requires:       python3-beautifulsoup4
Requires:       python3-qt5
Requires:       python3-requests
Requires:       python3-poppler-qt5

%description
Qt based ebook reader
Currently supports:
 - pdf
 - epub
 - mobi
 - azw / azw3 / azw4
 - cbr / cbz



%prep
%autosetup -p1 -n Lector-%{version}
mv lector/rarfile/LICENSE LICENSE.rarfile


%build
%py3_build


%install
%py3_install


%files
%doc AUTHORS README.md
%license LICENSE LICENSE.rarfile
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*
%{python3_sitelib}/%{name}*

%changelog
* Sun May 13 2018 Bugzy Little <bugzylittle@outlook.com> - 0.4-1
- upgrade to version 0.4
- Text annotations
- Drag and drop support
- Better spacebar navigation
- More granular progress measurement
- Remove dependency on requests
- Redesign settings dialog
- In-built internet searching
- Miscellaneous UI Improvements
- Bugfixes
- Chinese (simplified) translation by jaccsr

* Sat Apr 21 2018 Bugzy Little <bugzylittle@outlook.com> - 0.3.1-1
- upgrade to version 0.3.1
- Application icon and .desktop file
- Distraction free mode
- Internationalization support
- Context menus for reading views
- UI Improvements
- Bug fixes

* Tue Mar 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2-1
- First RPM release
