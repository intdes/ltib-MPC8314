%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Proprietary pme libraries
Name            : pme_priv
Version         : 1.0.0
Release         : a5
License         : Freescale EULA
Vendor          : Freescale
Packager        : Paul Barrette
Group           : Development/Debuggers
Source          : %{name}-%{version}-%{release}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build

%Install
rm -rf $RPM_BUILD_ROOT
pwd
echo  "$RPM_BUILD_ROOT/%{pfx}/pme_priv"
mkdir -p $RPM_BUILD_ROOT/%{pfx}/usr/lib
cp lib_powerpc/* $RPM_BUILD_ROOT/%{pfx}/usr/lib

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
