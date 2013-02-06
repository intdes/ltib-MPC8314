%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Universal Bootloader firmware
Name            : u-boot
Version         : 2009.03
Release         : 0
License         : GPL
Vendor          : Denx.de and Freescale
Packager        : Dipen  
Group           : Applications/System
Source          : u-boot-%{version}.tar.bz2
Patch1		: u-boot-2009.03-p2020rdb-GPIO-registers-to-mpc85xx-map.patch
Patch2		: u-boot-2009.03-p2020rdb-Second-UART-for-mpc85xx.patch
Patch3		: u-boot-2009.03-p2020rdb-Support-of-Vitesse-PHYs.patch
Patch4		: u-boot-2009.03-p2020rdb-Removed-CONFIG_NUM_CPUS-for-85xx.patch
Patch5		: u-boot-2009.03-p2020rdb-DDR-data-width-from-SVR.patch
Patch6		: u-boot-2009.03-p2020rdb-Support-of-P1-P2-processors-v2.patch
Patch7		: u-boot-2009.03-p2020rdb-Support-for-P1-P2-RDB-platforms-v2.patch
Patch8		: u-boot-2009.03-p2020rdb-eSPI-register-support-MPC8536DS.patch
Patch9		: u-boot-2009.03-p2020rdb-SPI-Flash-support-MPC8536DS.patch
Patch10		: u-boot-2009.03-p2020rdb-eSPI-controller-support-MPC8536DS.patch
Patch11		: u-boot-2009.03-p2020rdb-Boot-from-SDcard-MPC8536DS-v2.patch
Patch12		: u-boot-2009.03-p2020rdb-Save-env-to-SDcard-MPC8536DS.patch
Patch13		: u-boot-2009.03-p2020rdb-Fixup-SDHC-clock-in-dts-MPC8536DS.patch
Patch14		: u-boot-2009.03-p2020rdb-CONFIG_FSL_ESDHC-for-eSDHC-clk.patch
Patch15		: u-boot-2009.03-p2020rdb-PIO-mode-support-for-eSDHC-Driver.patch
Patch16		: u-boot-2009.03-p2020rdb-eSDHC-PIO-mode-last-3-bytes-corre.patch
Patch17		: u-boot-2009.03-p2020rdb-eSDHC-IRQ-Bypass-Workaround.patch
Patch18		: u-boot-2009.03-p2020rdb-eSDHC-IRQ-Bypass-auto-trigger.patch
Patch19		: u-boot-2009.03-p2020rdb-PIO-mode-for-P2020-eSDHC.patch
Patch20		: u-boot-2009.03-p2020rdb-SD-and-SPI-4-bit-data-mode.patch
Patch21		: u-boot-2009.03-p2020rdb-SDCARD-boot-support.patch
Patch22		: u-boot-2009.03-p2020rdb-Defines-for-CONFIG_ETH.patch
Patch23		: u-boot-2009.03-p2020rdb-SYSCLK-detected-from-GPIO10.patch
Patch24		: u-boot-2009.03-p2020rdb-RAMBOOT-support-over-SDCARD-boot.patch
Patch25		: u-boot-2009.03-p2020rdb-USB-mpc85xx-support.patch
Patch26		: u-boot-2009.03-p2020rdb-NAND-Boot-Support-v4.patch
Patch27		: u-boot-2009.03-p2020rdb-DDR-size-config-Board-Rev-and-SOC.patch
Patch28		: u-boot-2009.03-p2020rdb-RevB-DDR-changes.patch
Patch29		: u-boot-2009.03-p2020rdb-RevA-DDR-fixes.patch
Patch30		: u-boot-2009.03-p2020rdb-RevB-DDR-Changes-for-NAND-Boot-v3.patch
Patch31		: u-boot-2009.03-p2020rdb-Add-RTC-Support.patch
Patch32		: u-boot-2009.03-p2020rdb-Removed-NetLoop-Init-bug-v2.patch
Patch33         : 0003-adds-General-Freescale-CodeWarrior-debug-support.patch
Patch34         : 0004-Add-support-of-debug-kernel-with-attach-mode.patch
Patch35		: u-boot-2009.03-p2020rdb-Env-updated-with-diff-boot-options.patch
Patch36		: u-boot-2009.03-p2020rdb-added-revc-bugfix-3536-3577-3578.patch
Patch37		: u-boot-2009.03-p2020rdb-Added-nfsboot-command-in-fw_env.c-.patch
Patch38		: u-boot-2009.03-p2020rdb-retain-ESDHC-SCR-settings.patch
Patch39		: u-boot-2009.03-p2020rdb-Changed-the-nand-partition-number.patch

BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

Open source u-boot 2009.03 plus Freescale patches

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
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1

%Build
make distclean
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

if [ -f u-boot-nand.bin ]
then
    cp u-boot-nand.bin $RPM_BUILD_ROOT/%{pfx}/boot
fi

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
