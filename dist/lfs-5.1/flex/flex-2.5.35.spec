%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : fast lexical analyzer generator
Name            : flex
Version         : 2.5.35
Release         : 1
License         : BSD
Vendor          : Freescale
Packager        : Stuart Hughes, Daiane Angolini
Group           : Development/Tools
Source          : flex-%{version}.tar.bz2
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build
./configure --prefix=%{_prefix}
make

%Install
rm -rf $RPM_BUILD_ROOT
make -j1 install prefix=$RPM_BUILD_ROOT/%{pfx}/%{_prefix}
ln -s flex $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/lex

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*


