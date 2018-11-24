---
title: Configure system firmware for Windows 7 and enable for Windows 10
description: Configure system firmware for Windows 7 and enable for Windows 10
ms.date: 05/07/2018
ms.localizationpriority: medium
---


# Configure system firmware for Windows 7 and enable for Windows 10


To setup a modern system for installation of a downlevel operating system (such as Windows 7), this checklist can be used to meet both Windows 7 and Windows 10 requirements.

- UEFI 2.3.1 Errata C; This is based on a requirement for Windows 8.1, in anticipation of future upgrade to Windows 10.

- Secure Boot components for Windows 10 should be installed (certificates, etc.) See [Secure Boot](secure-boot.md) for more information.

- TPM 2.0 used for TPM support in Windows 7. See [KB2920188](https://support.microsoft.com/kb/2920188) for more information.

- EFI System Resource Table(ESRT) should be populated with a model specific Unique ID for System and Devices that can update firmware.

- **UpdateCapsule()** and **QueryCapsuleCapabilitiesenabled()** in UEFI.

- SMBIOS configured and populated per [SMBIOS](smbios.md) guidance (even if using downlevel SMBIOS, within reason).

- CSM is enabled. This is needed for Windows 7 and will disable Secure Boot.

- Configure hard drive as GPT disk.

- Device configured for UEFI Boot.

**Note** These requirements are based on both Windows 7 requirements, such as CSM enabled for UEFI boot, and Windows 10 requirements, such as ESRT and **UpdateCapsule()** being enabled.


