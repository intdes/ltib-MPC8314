%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : GStreamer Core
Name            : gstreamer-core
Version         : 0.10.22
Release         : 1
License         : LGPL
Vendor          : Freescale
Packager        : Kurt Mahan, Daiane Angolini
Group           : Applications/System
Source          : gstreamer-%{version}.tar.bz2
Patch1          : gstreamer-core-0.10.22-relink.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup -n gstreamer-%{version}
%patch1 -p1

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST NM=nm --build=%{_build} \
            --disable-valgrind --without-check 

make CFLAGS=-O0

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*.la" | xargs rm -f

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
