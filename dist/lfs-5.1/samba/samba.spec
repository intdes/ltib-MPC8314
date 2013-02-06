%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Samba is useful for creating and connecting to Windows shares using the SMB protocol
Name            : samba
Version         : 3.4.0
Release         : 3
License         : GPL
Vendor          : Freescale Semiconductor
URL             : http://www.samba.org
Packager        : Olivia Yin
Group           : System Environment/Daemons
Source          : http://samba.org/samba/ftp/stable/samba-3.4.0.tar.gz
Patch1          : %{name}-%{version}-configure-workaround.patch
Patch2          : pre-reply-write.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup
%patch1 -p1
%patch2 -p1

%Build
cd source3
CPPFLAGS="-D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE" \
samba_cv_CC_NEGATIVE_ENUM_VALUES=yes \
samba_cv_HAVE_EXPLICIT_LARGEFILE_SUPPORT=yes \
samba_cv_have_longlong=yes \
samba_cv_SIZEOF_OFF_T=yes \
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build} --disable-cups --without-ldap
make

%Install
rm -rf $RPM_BUILD_ROOT
cd source3
make installservers installbin installlibs DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
