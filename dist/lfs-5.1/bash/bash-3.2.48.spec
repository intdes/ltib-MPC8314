%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : bash - GNU Bourne-Again SHell
Name            : bash
Version         : 3.2.48
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Olivia Yin
Group           : System Environment/Shells
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup 

%Build
config_opts='ac_cv_func_setvbuf_reversed=no bash_cv_have_mbstate_t=yes ac_cv_lib_intl_bindtextdomain=no CC_FOR_BUILD="$BUILDCC"'

if [ -z "$UCLIBC" ]
then
    config_opts="bash_cv_job_control_missing=no $config_opts"
fi

if [ "$GNUTARCH" = m68k ]
then
    config_opts="with_bash_malloc=no $config_opts"
fi

eval $config_opts \
./configure --prefix=%{_prefix} --bindir=/bin --host=$CFGHOST --build=%{_build} --mandir=%{_mandir}
make -j1


%Install
rm -rf $RPM_BUILD_ROOT
make -j1 install DESTDIR=$RPM_BUILD_ROOT/%{pfx}
ln -s bash $RPM_BUILD_ROOT/%{pfx}/bin/sh
#
# Sometimes we want bash present but not installed as the default shell
#
if [ "$PKG_BASH_WANT_NO_SH_SYMLINK" = "y" ]
then
    rm -f $RPM_BUILD_ROOT/%{pfx}/bin/sh
fi

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*


