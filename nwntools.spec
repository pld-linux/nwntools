Summary:	NWN Tools
Summary(pl):	Narzêdzia dla NWN
Name:		nwntools
Version:	2.1.0
Release:	1
License:	GPL
Group:		Applications/Games
#Source0:	http://www.torlack.com/nwntools/%{name}-%{version}.tar.gz
Source0:	http://osdn.dl.sourceforge.net/openknights/%{name}-%{version}.tar.bz2
# Source0-md5:	c7664eabf3d2ecdaaa1bb4b96e58eeea
Patch0:		%{name}-nowxWindows.patch
URL:		http://www.torlack.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cocom-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- -- empty --

%description -l pl
- -- pusty --

%prep
%setup -q

%patch0 -p1

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
