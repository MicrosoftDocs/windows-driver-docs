---
title: Firmware WEG FAQ
description:  Firmware WEG - Frequently asked questions (FAQ)
ms.date: 05/07/2018
ms.localizationpriority: medium
---


# Firmware WEG: Frequently asked questions (FAQ)


The following FAQ came about due to the number of machines still using Windows 7.

Please send aditional questions or comments to <SAUEFI@Microsoft.com>.

**Q:** If I am installing Windows 7 on Skylake, which configuration should be chosen? Should the firmware CSM be enabled with UEFI boot (Config \#2) or legacy boot MBR (Config \#3)? If Legacy boot mode, why?

> **A:** Specifically, for Windows 7 it is recommended to use Config \#2. You will need to enable the CSM and set default to UEFI boot, falling back to legacy boot only if needed. Secure Boot will need to be disabled.
>
> Windows 7 is not able to support Config \# 1. Windows 7 has a dependency on Int10 support for basic display when the high-res graphics driver is not available (for example, Bugcheck, Sleep transitions, etc.), a dependency satisfied by the CSM. You can boot Win7 in UEFI mode if a partial CSM is in place (enabled) providing Int10 support. If firmware defaults to UEFI boot mode leaving Int10 CSM enabled, then Win7 will install successfully in UEFI mode. Microsoft has also backported TPM 2.0 support to Windows 7 for when it is installed in UEFI mode. For more information, see this KB article: [KB2920188](https://support.microsoft.com/kb/2920188).
>
> Microsoft recommends you should use Config \# 2; Legacy MBR Boot mode should not be used.

**Q:** If I installed Windows 7 with CSM enabled, what will the partition table/disk configuration look like?

> **A:** It depends on the boot devices priority defaults in firmware. If CSM is enabled and loaded into memory, this can sometimes cause install media to default to Legacy MBR boot.
>
> If you boot to legacy boot mode and go through installation you will typically have 2 partitions (as listed with diskpart.exe "list partition"). The first partition being active and listed as ‘system partition’, file system type being NTFS with a hidden \\boot folder. The second partition is where \\Windows is installed on another NTFS partition.
>
> If Windows is installing in UEFI mode, installation will create the EFI System Partition (ESP) as file system type Fat32, the Microsoft Reserve Partition (MSR) as RAW, and an OS / data partition using NTFS. If you mount and look at the ESP, you should see a folder \\EFI boot folder (folder may be hidden). Also see [Method to verify system is booted in UEFI mode](#_Toc451181866).
>
> Since you will need to leave CSM enabled in the system firmware for Windows 7, you may need to specifically select UEFI boot mode when booting to installation media (CD/DVD/USB) in order to install Windows 7 in UEFI boot mode.
> Consult with PC manufacture for more information concerning boot options and BIOS configuration.

**Q:** If I am installed Windows 7 with the CSM enabled in Legacy boot mode (config\#3), what is the upgrade path?

> **A:** Upgrade path for this configuration (\#3) is still supported through Windows 10. Though you will not be able to use Secure Boot as it is only available in UEFI Config \# 1. If you desire to switch the system to UEFI boot, you will need to format and re-install the original operating system with disk partitioned for GPT disk using UEFI boot mode. You will not need to keep the CSM enabled during this transition unless you need to boot to Windows 7 for the upgrade (config\#2) if you are upgrading from Windows store or an online installation.
> It is recommended to go straight to config\#1 (with the CSM disabled) for a pure UEFI environment, this is to make use of Secure Boot if firmware supports it.

**Q:** Is there any user impact when switching the Firmware from CSM enabled with Legacy BIOS boot (config\#3) to CSM enabled UEFI boot (config\#2) and back?

> **A:** This depends on how you go about switching. If you change from config\#3 to Config\#3, then attempt to boot, system may not boot. If you change back to config\#3 at this point, WITHOUT ANY FURHTER CHANGES TO SYSTEM, DISK or OS. Than you should be able to boot back into original OS, using the original config\#n. The recommendation is to *not* change the BIOS setting and instead upgrade "as-is".

**Q:** Change from config\#2 to config\#1 to enable Secure Boot:

> **A:** For newer systems; post 2015 (Skylake), and if system has CSM enabled, with Secure Boot disabled (they should be mutually exclusive) and OS is installed using UEFI boot method to GPT disk. After upgrading to Win10+, it should be a straightforward process of turning off the CSM and enabling Secure Boot in Firmware (if Secure Boot was setup in the factory and is an option in firmware).
>
> If after making the changes, the system is not able to boot, then system is more than likely configured to boot using CSM’s legacy BIOS for boot. If this is the case, this will require either Win10+ installation media, or a clean install of the original operating system (Windows 7). Ensuring that the CSM is enabled and installation/disk partition is set for UEFI boot mode which would later allow upgrade to Win10 in UEFI boot mode.
>
> Be sure to select UEFI boot to install media, firmware configuration may require further BIOS setting changes in order to boot to UEFI installation.
>
> Consult with PC manufacture for more information concerning boot options and BIOS configuration.

**Q:** User is running Windows 7, before upgrade to Win 10, BIOS/Firmware is switched to UEFI.

> **A:** \[Assuming that operating system was previously installed in Legacy BIOS boot mode.\]
>
> If the person who is installing Windows 10 goes through installation/setup. Windows setup will detect disk in Legacy MBR BIOS boot mode and attempt to install accordingly. Results may vary depending on system, boot method, installation media (if customized). However, you may get a message that the disk format is unsupported with this boot method. If you get this message it will be easy to format the disk and install fresh. WARNING, if you do format the disk you will **lose** any data that was on the disk.
>
> Recommendations are to change settings back to what they were prior to switching. This is so you can boot to the already installed operating system. Backup any data that you wish to save to an external storage location. Then go about re-provisioning the disk (clean the hard disk of existing partitions, boot to media in UEFI mode and perform fresh install to GPT disk).
>
> Caution; if you leave the CSM enabled, as in config\#2, there is a possibility that installation media may default to MBR boot. If operating system is installed in Legacy MBR boot mode. You will not be able to enable Secure Boot without again reprovisioning the disk and installing the operating system in UEFI Boot mode to GPT disk. You may wish to consult with PC manufacture for more information concerning boot options, BIOS configuration options as well as firmware updates and Secure Boot options.

**Q:** Does UEFI support booting from a MBR partitioned disk?

> **A:** No, booting from a MBR partitioned disk is only supported when booting in BIOS mode. If CSM is present and enabled, then legacy boot should be supported leveraging CSM’s legacy BIOS boot method.

**Q:** What is the dependency on 32-bit vs. 64-bit UEFI?

> **A:** Microsoft does support both 32 and 64 bit UEFI. The bitness of the OS and the UEFI firmware must match. (for example, if you have a 64-bit UEFI firmware then you must install 64-bit Windows OS).

**Q:** Can you programmatically switch firmware settings?

> **A:** No, most firmware settings are not standardized, and Microsoft does not offer a tool to allow a means to programmatically modify firmware settings. Consult with PC manufacture for details as there may be tools available for management and configuration.

**Q:** How does switching from CSM enabled Legacy BIOS boot (config\#3) to CSM enabled UEFI boot (config\#2) impact Secure Boot behavior?

> **A:** Secure Boot is only supported in UEFI mode with the CSM disabled. If Secure Boot was not pre-configured on the factory floor prior to system shipping out to customers, then you will probably not have the option available to you. If the system did previously have Secure Boot enabled, but disabled for current Windows 7 OS (using downgrade rights) then it may be as simple as disabling the CSM and enabling Secure Boot. However, if partition was cleaned and you are not setup for UEFI boot to GPT disk. Then you will need to clean the disk and re-install the operating system for UEFI boot prior to turning on Secure Boot.
>
> Consult with the original equipment manufacturer (OEM) prior to making any changes to ensure your system supports secure boot.
>
> **Note** Cleaning the disk will destroy any data that is on that disk even if in other partitions.

**Q:** Any dependency on BitLocker and Non-Microsoft disk encryption tools?

> **A:** Yes, switching UEFI/Legacy BIOS boot will likely cause boot to fail, and switching Firmware settings back to defaults should allow recovery. Suspending bitlocker, and in some cases, disabling Bitlocker or non-MS encryption tools would be recommended depending on if switching requires wiping the drive or just changing firmware settings (such as CSM/Secure boot)
>
> Consult with PC or software Manufacture for more information about configuration and defaults.

**Q:** How is Secure Boot configured once the BIOS is switched to UEFI?

> **A:** By default, for Win7 devices, Secure Boot is not implemented. If a system came with Windows 8 or higher, it's very likely that system would have Secure Boot configured as this was a Logo requirement. Secure Boot is only implemented on factory floor by the PC manufacturer. Please contact the PC manufacturer to see if they would be able to install Secure Boot on your system. You may need to send system back to PC manufacture to get this installed.

**Q:** What is impact on a rollback/restore to Windows 7?

> **A:** As long as there were no changes to firmware settings, rollback to original operating system should work. If firmware settings were changed, change them back to factory default (what they were prior to rollback). Consult with PC manufacture to find out what type of rollback method or recovery method is included with system.

**Q:** What is the impact to WinRE?

> **A:** WinRE is going to have the same boot process as the installed operating system. If you changed the firmware boot option (Legacy BIOS to UEFI) than attempting to boot to operating system or WinRE on disk will now fail. If you are booting to WinRE or WinPE on USB/CD/DVD, this will use a separate boot method.

**Q:** What is dependency/impact on 32-bit vs. 64-bit OS going from Legacy boot to UEFI and vice versa if the firmware is 64-bit UEFI or 32-bit UEFI?

> **A:** One limitation of Windows UEFI boot is that you can only boot an OS "bitness" that matches the UEFI that is installed (see Question 7).� If you have a 32-bit UEFI, you can only install a 32-bit Windows on it.� 64-bit Windows requires 64-bit UEFI or a CSM.� However, if�a system is missing a CSM, you cannot boot Win7 64-bit Windows OS.

**Q:** Can you convert a system booting using Legacy MBR boot to GPT boot on the fly without impacting data?

> **A:** No. Using Microsoft tools such as diskpart.exe will result in data loss. MBR boot and GPT boot are two different booting mechanisms that require a change to the disk that will remove all data from the disk in order to implement this change. Backup any data prior to attempting to make this change.

## Related resources

[UEFI Firmware](https://technet.microsoft.com/library/hh824898)

[Windows 10 Specifications - Microsoft](https://www.microsoft.com/windows/windows-10-specifications)

[Update to add support for TPM 2.0 in Windows 7 and Windows Server 2008 R2](https://support.microsoft.com/kb/2920188)



