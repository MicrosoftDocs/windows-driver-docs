---
title: Boot Options in EFI NVRAM
description: Computers with Extensible Firmware Interface (EFI) firmware store boot options in NVRAM, but retains its state even when you turn off the computer.
keywords:
- NVRAM boot options WDK
- EFI NVRAM boot options WDK
- boot options WDK , EFI NVRAM
- Extensible Firmware Interface WDK boot options
- Itanium processor boot options WDK
ms.date: 07/03/2018
---

# Boot Options in EFI NVRAM


> [!IMPORTANT] 
> This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for modern versions of Windows, see [Boot Options in Windows](boot-options-in-windows.md).

Computers with Extensible Firmware Interface (EFI) firmware, such as Intel Itanium 2 processors, store boot options in NVRAM, a storage medium that can be edited, but retains its state even when you turn off the computer. EFI firmware serves the same purpose as BIOS firmware, but it overcomes many limitations of the traditional BIOS. The startup functions that are implemented in the BIOS and boot manager (NTLDR) on x86-based systems are handled by EFI components, namely the EFI BIOS and EFI Boot Manager.

To configure features related to driver debugging and testing on EFI-based systems running Windows XP, Windows Server 2003 and their predecessors, you must edit the boot options in NVRAM. The following sections briefly describe the boot options in EFI NVRAM and explain the aspects of boot options that are specific to systems that use this technology.

On Windows Vista and later versions of Windows, boot options on BIOS-based and EFI-based computers are stored in *Boot Configuration Data* (BCD), a firmware-independent configuration and storage system for boot options. For more information, see [Boot Options in Windows Vista and Later](./boot-options-in-windows.md).

For a detailed description of boot options on Itanium-based systems, see the Extensible Firmware Interface Specification. You can download a copy of the updated specification from the [Intel Extensible Firmware Interface](https://www.intel.com/content/www/us/en/architecture-and-technology/unified-extensible-firmware-interface/efi-homepage-general-technology.html) website.

This section includes:

- [Overview of Boot Options in EFI](overview-of-boot-options-in-efi.md)
- [Editing Boot Options in EFI](editing-boot-options-in-efi.md)
- [Backing up Boot Options in EFI](backing-up-boot-options-in-efi.md)
