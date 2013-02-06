%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Linux hardware monitoring
Name            : lm_sensors
Version         : 3.0.3
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Olivia Yin
Group           : Applications/System
Source          : %{name}-%{version}.tar.bz2
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}
URL             : http://www.lm-sensors.org/

%Description
Build and provide some essential tools for monitoring the hardware health of Linux systems containing hardware health monitoring hardware such as the LM78 and LM75.

%Prep
%setup

%Build
case "$LINTARCH" in
    ppc|powerpc|ppc64)
        sed -i '/SRCDIRS += prog\/dump/d' Makefile
        ;;
    *)
        ;;
esac
make PREFIX=$RPM_BUILD_ROOT/%{pfx} CC="${TOOLCHAIN_PREFIX}gcc"

%Install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/%{pfx} ETCDIR=$RPM_BUILD_ROOT/%{pfx}/etc
mkdir -p $RPM_BUILD_ROOT/%{pfx}/lib/test/
cp -a lib/test/test-scanner $RPM_BUILD_ROOT/%{pfx}/lib/test/test-scanner

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
