%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : GStreamer Plugins Base
Name            : gst-plugins-base
Version         : 0.10.22
Release         : 1
License         : LGPL
Vendor          : Freescale
Packager        : Kurt Mahan
Group           : Applications/System
Source          : gst-plugins-base-%{version}.tar.bz2
Patch1          : gst-plugins-base-0.10.12-relink.patch
Patch2          : gst-plugins-base-0.10.22-optplaybin.patch
Patch3          : gst-plugins-base-0.10.22-mpeg2avsyncfix.patch 
Patch4          : gst-plugins-base-0.10.22-typefindaacplus2flac.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%Build
export NM=nm
if [ -z "$PKG_LIBX11" ]
then
    XTRA_OPTS="$XTRA_OPTS --without-x"
fi

if perl -e 'exit($ENV{TOOLCHAIN} =~ m,mtwk-lnx-powerpc-823-gcc-3.3.2-glibc-2.3.2, ? 0 : 1)'
then
    CFLAGS="-D__user="
fi
CFLAGS="$CFLAGS" \
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} \
	    --disable-vorbis --disable-vorbistest --disable-freetypetest \
	    --disable-theora --disable-ogg --disable-oggtest \
	    --disable-libvisual --disable-cdparanoia $XTRA_OPTS
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
