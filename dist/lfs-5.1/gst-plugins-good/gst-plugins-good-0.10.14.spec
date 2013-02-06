%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : GStreamer Plugins Good
Name            : gst-plugins-good
Version         : 0.10.14
Release         : 1
License         : LGPL
Vendor          : Freescale
Packager        : Kurt Mahan, Daiane Angolini
Group           : Applications/System
Source          : gst-plugins-good-%{version}.tar.bz2
Patch1          : gst-plugins-good-0.10.14-relink.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch1 -p1

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST NM=nm \
	    --build=%{_build} --without-check \
	    --disable-speex \
	    --disable-shout2test --disable-shout2 \
	    --disable-dv1394 --disable-libpng \
	    --disable-libdv --disable-libcaca \
	    --disable-ladspa --disable-jpeg \
	    --disable-gconf --disable-flac \
	    --disable-esd --disable-esdtest \
	    --disable-cairo --disable-aalib \
	    --disable-aalibtest --disable-x \
	    --disable-xvideo --disable-hal
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
