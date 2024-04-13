---
title: Portability in Network Drivers
description: Portability in Network Drivers
keywords:
- network drivers WDK , porting drivers
- portability WDK networking
- porting drivers WDK networking
- NDIS porting drivers WDK
ms.date: 04/20/2017
---

# Portability in Network Drivers





NDIS drivers should be written so that they are easily portable across all platforms that support Microsoft Windows operating systems. In general, porting from one hardware platform to another should only require recompilation with a system-compatible compiler.

Follow these guidelines when you write NDIS drivers:

-   Avoid calling operating system-specific functions. Instead, use the NDIS equivalent functions. NDIS exports a rich set of support functions for writing drivers, and if you call these support functions, you can port the code between Microsoft operating systems that support NDIS.

-   Write drivers in C (specifically, the ANSI C Standard). Avoid using any language features that other system-compatible compilers do not support. Do not use any features that the ANSI C standard designates as "implementation defined."

-   Avoid dependencies on data types whose size and layout vary across platforms. For example, do not write driver code that calls any C Run-Time Library functions instead of NDIS-provided functions.

-   Do not use floating-point operations in kernel mode. If you attempt such operations, a fatal error will occur.

-   Use **\#ifdef** and **\#endif** statements to encapsulate code that is used to support platform-specific features.

 

 





