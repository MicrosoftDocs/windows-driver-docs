---
title: Portable
description: Portable
ms.assetid: 3ce16503-e375-44c1-82a7-796286c1a253
keywords: ["portable drivers WDK kernel", "platform-dependent definitions WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Portable





All drivers must be portable across all Windows-supported hardware platforms. To achieve cross-platform portability, driver writers should:

-   Code in C (no assembly language).

-   Interact with Windows by only using the programming interfaces and headers that are supplied in the WDK.

### Coding Drivers in C

All kernel-mode drivers should be written in C so that they can be recompiled with a system-compatible C compiler, relinked, and run on different Microsoft Windows platforms without rewriting or replacing any code. Most operating system components are coded entirely in C, with only small pieces of the HAL and kernel components written in assembly language, so that the operating system is readily portable across hardware platforms. You cannot use many C++ language constructs in kernel-mode drivers, so you should carefully evaluate using such constructs. For more information about issues that arise when drivers include C++ features, see the [C++ for Kernel Mode Drivers: Pros and Cons](http://go.microsoft.com/fwlink/p/?linkid=56294) white paper.

Drivers should not rely on the features of any particular system-compatible C compiler or C support library if those features are not guaranteed to be supported by other system-compatible compilers. In general, driver code should conform to the ANSI C standard and not depend on anything that this standard describes as "implementation-defined."

To write portable drivers, it is best to avoid:

-   Dependencies on data types that can vary in size or layout from one platform to another.

-   Calling any standard C runtime library function that maintains state.

-   Calling any standard C runtime library function for which the operating system provides an alternative support routine.

### Using WDK-Supplied Interfaces

Each Windows NT executive component exports a set of kernel-mode [driver support routines](https://msdn.microsoft.com/library/windows/hardware/ff544200) that drivers and all other kernel-mode components call. If the underlying implementation of a support routine changes over time, its callers remain portable because the interface to the defining component does not change.

The WDK supplies a set of header files that define system-specific data types and constants that drivers (and all other kernel-mode components) use to help maintain portability from one platform to another. All kernel-mode drivers include one of the master WDK kernel-mode header files, Wdm.h or Ntddk.h. The master header files pull in not only system-supplied headers that define the basic kernel-mode types, but also appropriate selections from any processor-architecture-specific headers when a driver is compiled with the corresponding compiler directive.

Some drivers, such as [SCSI miniport drivers](https://msdn.microsoft.com/library/windows/hardware/ff565309), [NDIS drivers](https://msdn.microsoft.com/library/windows/hardware/ff556938), and [video miniport drivers](https://msdn.microsoft.com/library/windows/hardware/ff570509), include other system-supplied header files.

If a driver requires platform-dependent definitions, it is best to isolate those definitions within **\#ifdef** statements, so that each driver can be compiled and linked for the appropriate hardware platform. However, you can almost always avoid implementing any platform-specific, conditionally compiled code in a driver by using the support routines, macros, constants, and types that the WDK master header files provide.

Kernel-mode drivers can use kernel-mode **Rtl*Xxx*** routines that are documented in the WDK. Kernel-mode drivers cannot call user-mode **Rtl*Xxx*** routines.

 

 




