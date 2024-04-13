---
title: Decorations in Printer INF Files
description: Decorations in Printer INF Files
keywords:
- INF files WDK print , decorations
- additional drivers WDK printer
- decorated INF WDK
- INF Models Section
ms.date: 01/27/2023
---

# Decorations in Printer INF Files

[!include[Print Support Apps](../includes/print-support-apps.md)]

The Printer device setup class is unique among device classes in its ability to accommodate drivers written for different processor architectures. For example, an x86 printer driver (one consisting of x86 binaries) can be added to an x64 machine. The x86 driver in this example is never executed on the x64 machine - it provides Point and Print support for x86 clients. Printer drivers that are added to support Point and Print for clients of a different architecture are called *additional drivers*. For information about Point and Print, see [Introduction to Point and Print](introduction-to-point-and-print.md).

Because of the need to load additional drivers for different processor architectures (that is, for the x86, x64, and Itanium architectures), the printer class installer in Microsoft Windows Server 2003 with SP1 and later, and the 64-bit version of Windows XP and later, uses decorations in the [**INF Models section**](../install/inf-models-section.md) to identify the architecture of the machine that the driver targets.

## INF File Decorations and Windows Versions

Decorations in printer INF files were introduced in Windows XP. In Windows XP and in Windows Server 2003, the decorations are optional. When decorations in the INF Models section are specified, they should match the current processor architecture.

Beginning with Windows Server 2003 with SP1 and the 64-bit version of Windows XP, decorations in the INF Models section are no longer optional for x64 drivers; these drivers must use decorated INF Models sections to indicate their target machine.

[How to Use Decorations in INF Files for Printer Drivers](how-to-use-decorations-in-inf-files-for-printer-drivers.md)
