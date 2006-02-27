Summary:	NWN Tools
Summary(pl):	Narzêdzia dla NWN
Name:		nwntools
Version:	2.3.2
Release:	1
License:	BSD
Group:		Applications/Games
#Source0:	http://www.torlack.com/nwntools/%{name}-%{version}.tar.gz
Source0:	http://dl.sourceforge.net/openknights/%{name}-%{version}.tar.gz
# Source0-md5:	495936ac6319c778b3dd074471cd2b67
Patch0:		%{name}-nowxWindows.patch
URL:		http://www.torlack.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cocom-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NWN Tools contain the following programs:
- NWN Explorer
- NWN Treasure Editor
- NWN Model Compiler
- NWN Script Compiler

%description -l pl
Pakiet NWN Tools zawiera nastêpuj±ce programy:
- NWN Explorer
- NWN Treasure Editor (edytor skarbów)
- NWN Model Compiler (kompilator modeli)
- NWN Script Compiler (kompilator skryptów)

%prep
%setup -q
#patch0 -p1

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README-1.2.html
%attr(755,root,root) %{_bindir}/*
