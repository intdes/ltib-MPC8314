%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Wireless Ethernet configuration tools
Name            : wireless_tools
Version         : 29
Release         : 2
License         : GPL
Vendor          : Freescale
Packager        : Stuart Hughes
Group           : System Environment/Base
Source          : %{name}.%{version}.tar.gz
Patch1          : wireless-tools-29-tc-segv.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup -n %{name}.%{version}
%patch1 -p1

%Build
make

%Install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/%{pfx}/%{_prefix}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
