%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : X.Org X11 libXtst runtime library
Name            : libXtst
Version         : 1.0.3
Release         : 3
License         : MIT
Vendor          : X.Org Foundation
Packager        : Rogerio Pimentel
Group           : System Environment/Libraries
URL             : http://www.x.org
Source0: ftp://ftp.x.org/pub/individual/lib/libXtst-1.0.3.tar.bz2

BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --disable-static
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*.la" | xargs rm -f

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*

