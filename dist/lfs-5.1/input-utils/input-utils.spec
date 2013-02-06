%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : A Set of Utilities for Input Devices
Name            : input-utils
Version         : 2007.06.22
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Rob Herring
Group           : Hardware/Joystick
URL             : http://linuxconsole.sourceforge.net/input/input.html
Source          : %{name}-%{version}.tar.bz2
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}
%define programs evtest inputattach

%Description
%{summary}

%Prep
%setup -n utils

%Build
make PROGRAMS="%{programs}"

%Install
rm -rf $RPM_BUILD_ROOT
install -m755 -d $RPM_BUILD_ROOT%{pfx}%{_bindir}
install -m755 %{programs} $RPM_BUILD_ROOT%{pfx}%{_bindir}
 
%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
