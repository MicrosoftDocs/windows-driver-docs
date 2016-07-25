---
title: Windows Driver Signing Tutorial
ms.assetid: B6F907DC-74DC-4BF3-A2F9-481AE706733C
description: 
---

# Windows Driver Signing Tutorial


This tutorial provides an overview and details the steps to sign driver binaries for Windows in one consolidated location. The following subtopics describe the process:

[Test Signing](test-signing.md)
[Release Signing](release-signing.md)
[Troubleshooting Driver Signing Installation](troubleshooting-driver-signing-installation.md)
[Related Topics and Appendices](related-topics-and-appendices.md)
## Overview


Starting with Windows Vista, x64-based versions of Windows required all software running in kernel mode, including drivers, to be digitally signed in order to be loaded.

Microsoft provides the following two ways to digitally sign drivers:

1.  [Certify your driver with Microsoft](http://msdn.microsoft.com/windows/hardware/gg463010.aspx) and Microsoft will provide a signature for it. When your driver package passes the certification tests, it can be signed by Windows Hardware Quality Labs (WHQL). If your driver package is signed by WHQL, it can be distributed through the Windows Update program or other Microsoft-supported distribution mechanisms.
2.  Vendors or driver developers can obtain a software publishing certificate (SPC) from a Microsoft authorized Certificate Authority (CA) and use it to sign kernel mode and user mode binaries by themselves.

In the case of boot-start drivers during system start, drivers that are loaded by the system loader (Windows Vista and later versions of Windows), vendors must use a Software Publishers Certificate (SPC) to embed-sign their driver binary image file.

**Note**  The mandatory kernel-mode code-signing policy applies to all kernel-mode software for x64-based systems that are running on Windows Vista and later versions of Windows. However, Microsoft encourages publishers to digitally sign all kernel-mode software, including device drivers (user-mode drivers included) for 32-bit systems as well. Windows Vista and later versions of Windows, verify kernel-mode signatures on 32-bit systems. Software to support protected media content must be digitally signed even if it is 32-bit.

 

User-mode drivers, like the Printer driver will install and work in an x64-based computer. A dialog will appear to the user during installation asking for approval to install the driver. Beginning in Windows 8 and later versions of Windows, installation will not proceed unless these driver packages are also signed.

The following resources describe Driver Signing in greater detail:

-   The main [Driver Signing](driver-signing.md) topic on MSDN
-   The subtopic "How to Release Sign a Kernel Module" in the [Kernel-Mode Code Signing Walkthrough](http://msdn.microsoft.com/library/windows/hardware/dn653569.aspx) describes what you should know about signing kernel-mode code. The information in the document also applies to signing user-mode drivers.
-   The selfsign\_readme.htm file in the Windows 7 WDK is located in the WDK install directory, \\WinDDK\\7600.16385.1\\src\\general\\build\\driversigning. This directory also has a command file, selfsign\_example.cmd, which can be edited to run the driver signing commands. The selfsign\_readme.htm file in the Windows 8.1 WDK is located at C:\\Program Files (x86)\\Windows Kits\\8.1\\bin\\selfsign, and provides links to additional driver signing information.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Windows%20Driver%20Signing%20Tutorial%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




