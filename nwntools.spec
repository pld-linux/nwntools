Summary:	NWN Tools
Summary(pl):	NWN Tools
Name:		nwntools
Version:	1.2
Release:	1
License:	GPL
Group:		Games
Group(pl):	Gry
Source0:	http://www.torlack.com/nwtools/%{name}-%{version}.tar.gz
# Source0-md5:	9c8f809bf40b7c382b10d8aba08fc9d2
#BuildRequires:
#Requires:
URL:		http://www.torlack.com/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- -- empty --

%description -l pl
- -- pusty --

%prep
%setup -q

#%patch

%build
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%{configure}
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/*
