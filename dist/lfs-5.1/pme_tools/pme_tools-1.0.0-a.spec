%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary		: Pattern matcher tools
Name		: pme_tools
Version		: 1.0.0
Release		: a6
License		: Freescale EULA
Vendor		: Freescale
Packager	: Paul Barrette
Group		: Development/Tools
URL		: http://git.am.freescale.net/r01325/pme_tools.git
Source		: %{name}-%{version}-%{release}.tar.gz
BuildRoot	: %{_tmppath}/%{name}
Prefix		: %{pfx}

%Description
%{summary}

%Prep
%setup

%Build
make -j 1 ARCH=powerpc USE_LTIB=1 LTIB_LIB_PATH=$TOP/rootfs/usr/lib

%Install
rm -rf $RPM_BUILD_ROOT
DIR=$RPM_BUILD_ROOT/%{pfx}/usr
mkdir -p $DIR/bin
mkdir -p $DIR/lib
make INSTALL_DIR=$DIR install ARCH=powerpc
mkdir -p $RPM_BUILD_ROOT/%{pfx}/sample_rules
cp ltib_supp/sample* $RPM_BUILD_ROOT/%{pfx}/sample_rules

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-, root, root)
%{pfx}/*
