---
title: Decorations in Printer INF Files
description: Decorations in Printer INF Files
ms.assetid: 86ddca11-e2a9-44b8-8c42-313116fc580e
keywords: ["INF files WDK print , decorations", "additional drivers WDK printer", "decorated INF WDK", "INF Models Section"]
---

# Decorations in Printer INF Files


The Printer device setup class is unique among device classes in its ability to accommodate drivers written for different processor architectures. For example, an x86 printer driver (one consisting of x86 binaries) can be added to an x64 machine. The x86 driver in this example is never executed on the x64 machine - it provides Point and Print support for x86 clients. Printer drivers that are added to support Point and Print for clients of a different architecture are called *additional drivers*. For information about Point and Print, see [Introduction to Point and Print](introduction-to-point-and-print.md).

Because of the need to load additional drivers for different processor architectures (that is, for the x86, x64, and Itanium architectures), the printer class installer in Microsoft Windows Server 2003 with SP1 and later, and the 64-bit version of Windows XP and later, uses decorations in the [**INF Models section**](https://msdn.microsoft.com/library/windows/hardware/ff547456) to identify the architecture of the machine that the driver targets.

### INF File Decorations and Windows Versions

Decorations in printer INF files were introduced in Windows XP. In Windows XP and in Windows Server 2003, the decorations are optional. When decorations in the INF Models section are specified, they should match the current processor architecture.

Beginning with Windows Server 2003 with SP1 and the 64-bit version of Windows XP, decorations in the INF Models section are no longer optional for x64 drivers; these drivers must use decorated INF Models sections to indicate their target machine.

[How to Use Decorations in INF Files for Printer Drivers](how-to-use-decorations-in-inf-files-for-printer-drivers.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Decorations%20in%20Printer%20INF%20Files%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




