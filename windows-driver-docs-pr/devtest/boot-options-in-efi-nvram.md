---
title: Boot Options in EFI NVRAM
description: Computers with Extensible Firmware Interface (EFI) firmware store boot options in NVRAM, but retains its state even when you turn off the computer.
ms.assetid: 99247d03-1723-4a2b-8ef4-c1f39687642f
keywords:
- NVRAM boot options WDK
- EFI NVRAM boot options WDK
- boot options WDK , EFI NVRAM
- Extensible Firmware Interface WDK boot options
- Itanium processor boot options WDK
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Boot Options in EFI NVRAM


\[This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for Windows 8, Windows Server 2012, Windows 7, Windows Server 2008, or Windows Vista, see [Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md).\]

Computers with Extensible Firmware Interface (EFI) firmware, such as Intel Itanium 2 processors, store boot options in NVRAM, a storage medium that can be edited, but retains its state even when you turn off the computer.

## <span id="ddk_boot_options_in_efi_nvram_tools"></span><span id="DDK_BOOT_OPTIONS_IN_EFI_NVRAM_TOOLS"></span>


EFI firmware serves the same purpose as BIOS firmware, but it overcomes many limitations of the traditional BIOS. The startup functions that are implemented in the BIOS and boot manager (NTLDR) on x86-based systems are handled by EFI components, namely the EFI BIOS and EFI Boot Manager.

To configure features related to driver debugging and testing on EFI-based systems running Windows Server 2003 and earlier versions of NT-based Windows operating systems, you must edit the boot options in NVRAM. The following sections briefly describe the boot options in EFI NVRAM and explain the aspects of boot options that are specific to systems that use this technology.

On Windows Vista and later versions of Windows, boot options on BIOS-based and EFI-based computers are stored in *Boot Configuration Data* (BCD), a firmware-independent configuration and storage system for boot options. For more information, see [Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md).

For a detailed description of boot options on Itanium-based systems, see the Extensible Firmware Interface Specification. You can download a copy of the updated specification from the [Intel Extensible Firmware Interface](http://go.microsoft.com/fwlink/p/?linkid=10596) website.

This section includes:

[Overview of Boot Options in EFI](overview-of-boot-options-in-efi.md)

[Editing Boot Options in EFI](editing-boot-options-in-efi.md)

[Backing up Boot Options in EFI](backing-up-boot-options-in-efi.md)

 

 





