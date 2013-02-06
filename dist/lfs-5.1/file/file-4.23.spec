%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : A utility for determining file types.
Name            : file
Version         : 4.23
Release         : 1
License         : BSD
Vendor          : Freescale
Packager        : Stuart Hughes
Group           : Applications/File
Source          : %{name}-%{version}.tar.gz
Patch1          : file-4.23-magic-bugfix.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch1 -p1 

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --target=$CFGHOST
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*


