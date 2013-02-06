%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : gzip, gunzip, zcat - compress or expand files using LZ77
Name            : gzip
Version         : 1.3.12
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Stuart Hughes
Group           : Applications/File
Source          : %{name}-%{version}.tar.gz
Patch0          : gnulib-futimens.patch
Patch1          : gzip-1.3.12-gnulib-futimens.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch0 -p1
%patch1 -p1

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build}
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*


