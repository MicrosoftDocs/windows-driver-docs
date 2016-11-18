---
title: Overview of the Boot.ini File
description: The Boot.ini file is a text file that contains the boot options for computers with BIOS firmware running NT-based operating system prior to Windows Vista. It is located at the root of the system partition, typically c \\Boot.ini.
ms.assetid: bc9bb063-4caa-42fe-bb3d-dc588fbbb8d9
keywords: ["Boot.ini files WDK , about Boot.ini files", "boot loader section WDK boot options", "operating systems section WDK boot options", "boot entries WDK", "names WDK boot options", "friendly names WDK boot options", "boot entry parameters WDK", "boot parameters WDK"]
---

# Overview of the Boot.ini File


\[This topic describes the boot options supported in Windows XP and Windows Server 2003. If you are changing boot options for Windows 8, Windows Server 2012, Windows 7, Windows Server 2008, or Windows Vista, see [Boot Options in Windows Vista and Later](boot-options-in-windows-vista-and-later.md).\]

The Boot.ini file is a text file that contains the boot options for computers with BIOS firmware running NT-based operating system prior to Windows Vista. It is located at the root of the system partition, typically c:\\Boot.ini.

## <span id="ddk_overview_of_the_boot_ini_file_tools"></span><span id="DDK_OVERVIEW_OF_THE_BOOT_INI_FILE_TOOLS"></span>


The following sample shows the content of a typical Boot.ini file.

```
[boot loader]
timeout=30
default=multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
[operating systems]
multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect
C:\CMDCONS\BOOTSECT.DAT="Microsoft Windows Recovery Console" /cmdcons
```

The Boot.ini file has two main sections:

-   The **\[boot loader\]** section contains option settings that apply to all boot entries on the system. The options include **timeout**, the boot menu time-out value, and **default**, the location of the default operating system.

    The following sample shows the \[boot loader\] section of a Boot.ini file.

    ```
    [boot loader]
    timeout=30
    default=multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
    ```

-   The **\[operating systems\]** section is comprised of one or more *boot entries* for each operating system or bootable program installed on the computer.

    A *boot entry* is a set of options that defines a load configuration for an operating system or bootable program. The boot entry specifies an operating system or bootable program and the location of its files. It can also include parameters that configure the operating system or program.

    The following sample shows the \[operating systems\] section of a Boot.ini file on a computer with two operating systems, Microsoft Windows XP and Microsoft Windows 2000. It has two boot entries, one for each operating system.

    ```
    [operating systems]
    multi(0)disk(0)rdisk(0)partition(1)\WINDOWS="Microsoft Windows XP Professional" /fastdetect
    multi(0)disk(0)rdisk(0)partition(2)\WINNT="Microsoft Windows 2000 Professional" /fastdetect
    ```

Each boot entry includes the following elements:

-   The location of the operating system. The Boot.ini file uses the Advanced RISC Computing (ARC) naming convention to display the path to the disk partition and directory where the operating system resides. For example:
    ```
    multi(0)disk(0)rdisk(0)partition(1)\WINDOWS
    ```

-   A friendly name for the boot entry. The friendly name represents the boot entry in the boot menu. The friendly name is surrounded by quotation marks and represents the boot entry in the boot menu. For example:
    ```
    "Microsoft Windows XP Professional"
    ```

-   *Boot entry parameters*, also known as *boot parameters* or *load options* enable, disable, and configure operating system features. Boot parameters resemble command-line parameters, each beginning with a forward slash (/), such as [**/debug**](https://msdn.microsoft.com/library/windows/hardware/ff556253). You can have zero or more boot parameters on each boot entry.

    For a list of boot parameters that are relevant to driver testing and debugging, see [Boot.ini Boot Parameter Reference](https://msdn.microsoft.com/library/windows/hardware/ff542248).

You can have multiple boot entries for the same operating system, each with a different set of boot parameters. Windows creates a standard boot entry when you install the operating system, and you can create additional, customized entries for an operating system by editing the Boot.ini file.

Comment

This document describes aspects of the Boot.ini file that are of special interest to driver developers and testers. For a more general description of the Boot.ini file, including a list of commonly used Boot.ini file parameters, see "Reviewing and Correcting Boot.ini Settings on x86-based Systems" in the [Microsoft Windows XP Professional Resource Kit Documentation](http://go.microsoft.com/fwlink/p/?linkid=10004).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Overview%20of%20the%20Boot.ini%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




