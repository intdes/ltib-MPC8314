%define base %(echo %{_prefix} | sed -e s,/usr.*$,,)
%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : A tool for automatically generating simple manual pages from program output.
Name            : help2man
Version         : 1.36.4
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Olivia Yin
Group           : System Environment/Base
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build
# fu_cv_sys_stat_statfs2_bsize is needed to turn on df
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --mandir=%{_mandir}
make

%Install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/%{pfx}/usr mandir=$RPM_BUILD_ROOT/%{pfx}/usr/share/man install_base

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*


