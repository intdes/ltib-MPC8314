%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Universal Bootloader firmware
Name            : u-boot
Version         : 2009.03
Release         : rc1
License         : GPL
Vendor          : Freescale
Packager        : Vivienne Li
Group           : Applications/System
Source          : u-boot-%{version}-%{release}.tar.bz2
Patch1          : 0001-eSPI-add-the-eSPI-register-support.patch
Patch2          : 0002-mtd-SPI-Flash-Support-the-Spansion-Flash.patch
Patch3          : 0003-eSPI-add-eSPI-controller-support.patch
Patch4          : 0004-Make-a-special-uboot-used-for-booting-from-SDcard-or.patch
Patch5          : 0005-Add-support-for-save-the-env-to-SDcard-2.patch
Patch6          : 0006-Save-the-env-variables-to-SDcard-and-SPI-flash-for-M.patch
Patch7          : 0007-Add-the-PCI-EP-support-for-8536DS-board.patch
Patch8          : 0008-8536-fixup-SDHC-clock-frequency-in-dts.patch
Patch9          : 0010-Fix-mpc85xx-ddr-gen3-ddr_sdram_cfg.patch
Patch10         : 0001-Invert-SDHC_WP-pin-polarity-on-MPC8536-rev1.1-silico.patch
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

Open source u-boot 2009.03-rc1 plus Freescale patches
ftp://ftp.denx.de/pub/u-boot/u-boot-2009.03-rc1.tar.bz2

%Prep
%setup -n %{name}-%{version}-%{release}
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

%Build
PKG_U_BOOT_CONFIG_TYPE=${PKG_U_BOOT_CONFIG_TYPE:-MPC8536DS_config}
make HOSTCC="$BUILDCC" CROSS_COMPILE=$TOOLCHAIN_PREFIX $PKG_U_BOOT_CONFIG_TYPE
make HOSTCC="$BUILDCC" HOSTSTRIP="$BUILDSTRIP" \
     CROSS_COMPILE=$TOOLCHAIN_PREFIX $PKG_U_BOOT_BUILD_ARGS all

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
