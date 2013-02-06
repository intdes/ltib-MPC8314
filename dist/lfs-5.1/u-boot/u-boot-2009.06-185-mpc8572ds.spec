%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Universal Bootloader firmware
Name            : u-boot
Version         : 2009.06
Release         : 0
License         : GPL
Vendor          : Freescale
Packager        : Zhenhua Luo
Group           : Applications/System
Source          : %{name}-%{version}-185-g57fe301-2.tar.bz2
Patch1		: 0001-8xxx-Fix-PCI-bus-address-setup-for-36-bit-configs.patch
Patch2		: 0002-MPC8572-Delete-default-interleaving-setting.patch


BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

Open source u-boot v2009.06-185--g57fe301 plus Freescale patches

%Prep
%setup -n %{name}-%{version}-185-g57fe301
%patch1 -p1
%patch2 -p1


%Build
if [ -z "$PKG_U_BOOT_CONFIG_TYPE" ]; then
    echo PKG_U_BOOT_CONFIG_TYPE is not set
    exit 1
fi
make distclean
make HOSTCC="$BUILDCC" CROSS_COMPILE=$TOOLCHAIN_PREFIX $PKG_U_BOOT_CONFIG_TYPE
make HOSTCC="$BUILDCC" HOSTSTRIP="$BUILDSTRIP" \
    CROSS_COMPILE=$TOOLCHAIN_PREFIX $PKG_U_BOOT_BUILD_ARGS

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}/boot
for i in u-boot.bin u-boot
do
    cp $i $RPM_BUILD_ROOT/%{pfx}/boot
done
if [ -f u-boot-nand.bin ] 
then
    cp u-boot-nand.bin $RPM_BUILD_ROOT/%{pfx}/boot
fi

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
