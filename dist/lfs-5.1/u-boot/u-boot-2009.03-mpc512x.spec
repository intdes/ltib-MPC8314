%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Universal Bootloader firmware
Name            : u-boot
Version         : 2009.03
Release         : 0
License         : GPL
Vendor          : Freescale
Packager        : John Rigby
Group           : Applications/System
Source          : u-boot-%{version}.tar.bz2
Patch1          : u-boot-2009.03-ADS5121-01-Resume-from-suspend-to-ram.patch
Patch2          : u-boot-2009.03-ADS5121-02-Add-NAND-driver.patch
Patch3          : u-boot-2009.03-ADS5121-03-Add-CW-debug-support.patch
Patch4          : u-boot-2009.03-ADS5121-04-Update-default-env.patch
Patch5          : u-boot-2009.03-ADS5121-05-Change-CONFIG_SYS_MONITOR_LEN.patch
Patch6          : u-boot-2009.03-ADS5121-06-only-read-dvi-xvr-regs-on-DEBUG.patch
Patch7          : u-boot-2009.03-ADS5121-07-delay-ide-pci-and-net-init.patch
Patch8          : u-boot-2009.03-ADS5121-08-enable-icache-from-the-beginning.patch
Patch9          : u-boot-2009.03-ADS5121-09-reset-fix.patch
Patch10         : u-boot-2009.03-ADS5121-10-update-enabled-features.patch
Patch11         : u-boot-2009.03-ADS5121-11-Change-naming-on-DRAM-constants.patch
Patch12         : u-boot-2009.03-ADS5121-12-add-new-elpida-memory-config.patch
Patch13         : u-boot-2009.03-ADS5121-13-add-ADS5125-support.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

Open source u-boot v2008.10 plus Freescale patches

%Prep
%setup -n u-boot-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

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

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
