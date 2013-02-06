%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : The GNU utility for retrieving files across the internet
Name            : wget
Version         : 1.11.1
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Olivia Yin
Group           : Applications/Internet
Source          : %{name}-%{version}.tar.bz2
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup 

%Build
./configure --prefix=%{_prefix} --sysconfdir=%{_sysconfdir} --host=$CFGHOST --mandir=%{_mandir}
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*


