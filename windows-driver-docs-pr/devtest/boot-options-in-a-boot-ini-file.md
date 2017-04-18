---
title: Boot Options in a Boot.ini File
description: Boot.ini is a text file located at the root of the system partition, typically c \\Boot.ini. Boot.ini stores boot options for computers with BIOS firmware, traditionally, computers with x86 and x64-based processors.
ms.assetid: a2593b6d-03df-49d1-ae77-efec4c2ac8be
keywords: ["Boot.ini files WDK", "boot options WDK , Boot.ini files"]
---

# Boot Options in a Boot.ini File


\[This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for Windows 8, Windows Server 2012, Windows 7, Windows Server 2008, or Windows Vista, see [Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md).\]

Boot.ini is a text file located at the root of the system partition, typically c:\\Boot.ini. Boot.ini stores boot options for computers with BIOS firmware, traditionally, computers with x86 and x64-based processors.

## <span id="ddk_boot_options_in_a_boot_ini_file_tools"></span><span id="DDK_BOOT_OPTIONS_IN_A_BOOT_INI_FILE_TOOLS"></span>


On Windows Server 2003 and earlier versions of NT-based Windows operating systems, when the computer starts, the Windows boot loader, Ntldr, reads the Boot.ini file and displays the entries for each operating system in the boot menu. Then, Ntldr loads the selected operating system in accordance with settings in the Boot.ini file.

By default, on NTFS drives, the **system**, **hidden**, **archived**, and **read-only** attributes are set to protect the Boot.ini file; however, members of the Administrators group can change these attributes. The file attributes do not affect the operation of boot loader.

The following sections briefly describe the Boot.ini file and explain the aspects of boot options that are specific to computers with Personal Computer Advanced Technology (PC/AT)-type BIOS firmware.

This section includes:

[Overview of the Boot.ini File](overview-of-the-boot-ini-file.md)

[Editing the Boot.ini File](editing-the-boot-ini-file.md)

[Backing Up the Boot.ini File](backing-up-the-boot-ini-file.md)

This document describes aspects of the Boot.ini file that are of special interest to driver developers and testers. For a complete list of the Boot.ini file parameters, see [Available Switch Options for the Windows XP and the Windows Server 2003 Boot.ini Files](http://go.microsoft.com/fwlink/p/?linkid=137742) topic in the Microsoft Knowledge Base.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Boot%20Options%20in%20a%20Boot.ini%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




