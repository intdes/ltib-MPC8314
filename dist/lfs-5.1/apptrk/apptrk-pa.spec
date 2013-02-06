%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Userspace debug agent for PA CodeWarrior
Name            : AppTRK-Base
Version         : 1.37
Release         : 1
License         : Freescale EULA
Vendor          : Freescale
Packager        : Bogdan Irimia
Group           : Development/Debuggers
Source          : %{name}-%{version}.tar.gz
Patch1		: apptrk-1.37-pa.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup 
%patch1 -p1

%Build
make all

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}/usr/bin
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
