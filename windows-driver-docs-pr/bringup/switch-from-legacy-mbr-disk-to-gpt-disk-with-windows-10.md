---
title: Switch from Legacy MBR disk to GPT disk with Windows 10
description: Provides guidance to enable a seamless upgrade and enable the user to leverage new and improved security features of Windows 10.
ms.date: 05/07/2018
ms.localizationpriority: medium
---


# Switch from Legacy MBR disk to GPT disk with Windows 10


To facilitate upgrading from downlevel operating systems, such as Windows 7, or transitioning from BIOS Boot to UEFI Boot for the enhanced security features. Microsoft has provided the following information. The steps in the following sections will enable a more seamless upgrade to Windows 10 and enable the user the ability to leverage the new and improved security features of Windows 10. For purposes of the below steps, we will refer to the GUID Partition Table as GPT, and Legacy Master Boot Record as Legacy MBR boot disks.

These four configurations will be used:

- Config \# 1 - UEFI boot without a Compatibility Support Module (CSM) or the CSM is disabled in firmware. Requires a GPT Hard Disk Drive (HDD).
- Config \# 2 - UEFI boot with CSM enabled, booting from GPT HDD
- Config \# 3 - Legacy BIOS boot with CSM enabled, booting from Legacy MBR HDD
- Config \# 4 - UEFI boot with CSM enabled, booting from Legacy MBR HDD

## Upgrade paths

| Existing OS+Config | Target OS+Config | Results | Security options | Coverage |
|---|---|---|---|---|
| Windows 7 **x64** installed to system with UEFI firmware, CSM enabled on GPT HDD (Config \# 2) | Windows 10 **x64** installed to UEFI firmware CSM enabled on GPT HDD (Config \# 2)        | Will bootup and run Windows 10 OS               | OS is able to make use of MS security features supported in firmware once CSM is disabled | Not covered in this document                                                                  |
| Windows 7 **x64** installed to BIOS with active partition NTFS HDD (Config \# 3)               | Windows 10 **x64** installed to BIOS with active partition NTFS HDD (Config \# 3)         | Will bootup and run Windows 10 OS               | Only able to leverage Bitlocker                                                           | Not covered in this document                                                                  |
| Windows 7 **x86** installed to BIOS with active partition NTFS HDD (Config \# 3)               | Windows 10 **x86** installed to BIOS with active partition NTFS HDD = works (Config \# 3) | Will bootup and run Windows 10 OS               | Only able to leverage Bitlocker                                                           | Not covered in this document                                                                  |
| Windows 7 **x86** installed to BIOS with active partition NTFS (Config \# 3)                   | Windows 10 **x64** installed to BIOS with active partition NTFS HDD (Config \# 3)         | Will need installation media and clean install. | Only able to leverage Bitlocker (other security features require UEFI boot)               | Not covered in this document                                                                  |
| Windows 7 **x64** installed to BIOS with active partition NTFS (Config \# 3)                   | Windows 10 **x64** installed to UEFI firmware CSM disabled on GPT HDD (Config \# 1)        | Special instructions below                      | OS is able to make use of MS security features supported in firmware                      | See [General overview for switching Legacy BIOS boot+CSM to UEFI+GPT](#_General_overview_for) |

## Definition of terms

**Compatibility support module (CSM)** can typically be enabled or disabled in firmware. This module facilitates, but does not dictate booting to an active partition with legacy master boot record (MBR). Depending on BIOS/Firmware boot options, you may be able to enable the CSM and still select to boot to UEFI boot mode using GPT disk or Legacy MBR boot mode. Having the CSM enabled and loaded into memory is required for Windows 7 to boot UEFI.
*UEFI boot* does not need CSM to be enabled. With CSM disabled, bootup does not use an active partition on the Hard Disk Drive(HDD), it does make use of an EFI System Partition (ESP) where it looks for a recognized file system such as FAT-FAT32 with boot files. Boot files can be defined in either a) NVRAM (boot000n) or b) Using UEFI specification defined fallback boot method looking for \\EFI\\Boot\\Boot(arch).efi (for example: bootx64.efi) This boot method does not work on a Legacy MBR configured NTFS boot disk.

**Legacy MBR boot** is not able to recognize GUID Partition Table (GPT) disks. It requires an active partition and supporting BIOS to facilitate access to disk. OLD and limited on HDD size and number of partitions. On UEFI firmware systems, it requires CSM enabled and loaded into memory to facilitate active partition booting.


## In this section


[New method - Windows 10, version 1703 and later](new-method--windows-10--version-1703-and-later.md)

[MBR2GPT tool test guidance](mbr2gpt-tool-test-guidance.md)

[Old method - Windows 10, version 1607 and earlier](old-method--windows-10--version-1607-and-earlier.md)

[How to convert an installed x64 Windows 7 system](how-to-convert-an-installed-x64-windows-7.md)



## Related resources


[Windows 10 Specification](https://www.microsoft.com/windows/Windows-10-specifications)



