%define	name	cryopid
%define	version	0.5.9.1
%define	rel     1
Summary:	A Process Freezer for Linux
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	BSD
Group:		Development/Other
URL:		http://cryopid.berlios.de/
Source0:	%{name}-%{version}-i386.tar.bz2
Source1:	%{name}-%{version}-x86_64.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
ExclusiveArch:	%ix86 x86_64
BuildRequires:  zlib-devel

%description
CryoPID allows you to capture the state of a running process in Linux and save
it to a file. This file can then be used to resume the process later on, either
after a reboot or even on another machine.

%prep
%setup -q -b1

%build
cd src
%__make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_bindir
cp src/freeze $RPM_BUILD_ROOT%_bindir

%files
%defattr(-,root,root)
%{_bindir}/freeze
%doc LICENSE ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT


