---
title: Windows Kernel-Mode Safe String Library
author: windows-driver-content
description: Windows Kernel-Mode Safe String Library
MS-HAID:
- 'safelib\_1f11be85-3233-4807-b0c1-4429b8b461d8.xml'
- 'kernel.windows\_kernel\_mode\_safe\_string\_library'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a54cd20c-2c2d-462d-b9fc-112e99562e52
---

# Windows Kernel-Mode Safe String Library


One of the major problems in software security is related to the vulnerability of working with strings. To provide greater security, Windows provides a safe string library.

Safe string library routines are prefixed with the letters "**Rtl**"; for a list of all safe string library routines for the kernel, see [Safe String Library Routines](https://msdn.microsoft.com/library/windows/hardware/ff563648).

For more information about using safe strings, see [Using Safe String Functions](using-safe-string-functions.md).

Note that there is also a separate run-time library for general C programming in the kernel that has string functionality as well. For more information about the run-time library (RTL), see [Windows Kernel-Mode Run-Time Library](windows-kernel-mode-run-time-library.md). Note that even though both libraries are prefixed with "**Rtl**" they are not the same library.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Kernel-Mode%20Safe%20String%20Library%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


