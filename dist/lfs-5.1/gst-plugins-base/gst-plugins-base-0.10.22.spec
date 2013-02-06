%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : GStreamer Plugins Base
Name            : gst-plugins-base
Version         : 0.10.22
Release         : 1
License         : LGPL
Vendor          : Freescale
Packager        : Kurt Mahan, Daiane Angolini
Group           : Applications/System
Source          : gst-plugins-base-%{version}.tar.bz2
Patch1          : gst-plugins-base-0.10.22-relink.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch1 -p1

%Build
./configure --prefix=%{_prefix} --build=%{_build} --host=$CFGHOST NM=nm \
	    --disable-vorbis --disable-vorbistest --disable-freetypetest \
	    --disable-theora --disable-pango --disable-ogg \
	    --disable-oggtest --disable-libvisual \
	    --disable-gnome_vfs --disable-cdparanoia \
	    --disable-x --disable-xvideo
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
