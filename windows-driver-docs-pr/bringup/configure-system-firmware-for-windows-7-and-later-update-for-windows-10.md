---
title: Configure system firmware for Windows 7 and enable for Windows 10
description: Configure system firmware for Windows 7 and enable for Windows 10
author: windows-driver-content
ms.author: windowsdriverdev
ms.date: 05/15/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


# Configure system firmware for Windows 7 and enable for Windows 10


To setup a modern system for installation of a downlevel operating system (such as Windows 7), this checklist can be used to meet both Windows 7 and Windows 10 requirements.

- UEFI 2.3.1 Errata C; This is based on a requirement for Windows 8.1, in anticipation of future upgrade to Windows 10.

- Secure Boot components for Windows 10 should be installed (certificates, etc.) See [Secure Boot](secure-boot.md) for more information.

- TPM 2.0 used for TPM support in Windows 7. See [KB2920188](https://support.microsoft.com/en-us/kb/2920188) for more information.

- EFI System Resource Table(ESRT) should be populated with a model specific Unique ID for System and Devices that can update firmware.

- **UpdateCapsule()** and **QueryCapsuleCapabilitiesenabled()** in UEFI.

- SMBIOS configured and populated per [SMBIOS](smbios.md) guidance (even if using downlevel SMBIOS, within reason).

- CSM is enabled. This is needed for Windows 7 and will disable Secure Boot.

- Configure hard drive as GPT disk.

- Device configured for UEFI Boot.

**Note** These requirements are based on both Windows 7 requirements, such as CSM enabled for UEFI boot, and Windows 10 requirements, such as ESRT and **UpdateCapsule()** being enabled.





--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


