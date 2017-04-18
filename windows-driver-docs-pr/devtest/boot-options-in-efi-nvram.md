---
title: Boot Options in EFI NVRAM
description: Computers with Extensible Firmware Interface (EFI) firmware, such as Intel Itanium 2 processors, store boot options in NVRAM, a storage medium that can be edited, but retains its state even when you turn off the computer.
ms.assetid: 99247d03-1723-4a2b-8ef4-c1f39687642f
keywords: ["NVRAM boot options WDK", "EFI NVRAM boot options WDK", "boot options WDK , EFI NVRAM", "Extensible Firmware Interface WDK boot options", "Itanium processor boot options WDK"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Boot%20Options%20in%20EFI%20NVRAM%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




