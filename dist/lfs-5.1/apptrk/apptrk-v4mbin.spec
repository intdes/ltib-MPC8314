%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Userspace debug agent for Codewarrior
Name            : apptrk
Version         : 1.37
Release         : 1
License         : Freescale EULA
Vendor          : Freescale
Packager        : Kurt Mahan
Group           : Development/Debuggers
Source          : AppTRK-1.37-CFV4M.tgz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

Binary only package.

%Prep
%setup -n AppTRK-1.37-CFV4M

%Build

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}/usr/bin
cp AppTRK.elf $RPM_BUILD_ROOT/%{pfx}/usr/bin/apptrk

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
