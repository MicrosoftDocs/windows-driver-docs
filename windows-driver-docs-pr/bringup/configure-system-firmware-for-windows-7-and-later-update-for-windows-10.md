---
title: Configure system firmware for Windows 7 and enable for Windows 10
description: Provides information about how to configure system firmware for Windows 7 and enable for Windows 10.
ms.date: 03/22/2023
---

# Configure system firmware for Windows 7 and enable for Windows 10

To set up a modern system for installation of a downlevel operating system (such as Windows 7), this checklist can be used to meet both Windows 7 and Windows 10 requirements.

- UEFI 2.3.1 Errata C; This is based on a requirement for Windows 8.1, in anticipation of future upgrade to Windows 10.

- Secure Boot components for Windows 10 should be installed (for example, certificates). For more information, see [Secure Boot](secure-boot.md).

- TPM 2.0 used for TPM support in Windows 7. For more information, see [KB2920188](https://support.microsoft.com/help/2920188/update-to-add-support-for-tpm-2-0-in-windows-7-and-windows-server-2008).

- EFI System Resource Table(ESRT) should be populated with a model specific Unique ID for System and Devices that can update firmware.

- **UpdateCapsule()** and **QueryCapsuleCapabilitiesenabled()** in UEFI.

- SMBIOS configured and populated per [SMBIOS](smbios.md) guidance (even if using downlevel SMBIOS, within reason).

- CSM is enabled. This is needed for Windows 7 and disables Secure Boot.

- Configure hard drive as GPT disk.

- Device configured for UEFI Boot.

These requirements are based on both Windows 7 requirements, such as CSM enabled for UEFI boot, and Windows 10 requirements, such as ESRT and **UpdateCapsule()** being enabled.
