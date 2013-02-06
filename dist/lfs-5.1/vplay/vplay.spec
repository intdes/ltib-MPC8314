%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : vplay - vrec - mixer
Name            : vplay
Version         : 1.0
Release         : 1
License         : Distributable
Vendor          : Freescale
Packager        : Matt Waddel
Group           : Application/System
Source          : vplay-1.0.tar.gz
Patch0          : vplay-add-soundcard-h.patch
Patch1          : vplay-add-amp-dev-options.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup -n vplay
%patch0 -p1
%patch1 -p1

%Build
make

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}/bin
cp vplay vrec $RPM_BUILD_ROOT/%{pfx}/bin

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*


