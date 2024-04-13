---
title: Interlocked Operations in Storport Miniport Drivers
description: Many of the interlocked functions available to Windows applications are appropriate for use in Storport miniport drivers.
ms.date: 06/13/2019
---

# Interlocked Operations in Storport Miniport Drivers

Applications must synchronize access to variables that are shared by multiple threads, using the Platform Software Development Kit (SDK) interlocked functions to do so. Many of the interlocked functions available to Windows applications are appropriate for use in Storport miniport drivers. Most of these functions are implemented as [compiler intrinsic functions](/cpp/intrinsics/compiler-intrinsics) and are suitable for synchronizing changes to protected values.
Functions are defined for logical, assignment, comparison, and arthimetic operations.

For more information about interlocked operations, see [Interlocked Variable Access](/windows/desktop/Sync/interlocked-variable-access).

**Note**  The **Interlocked*Xxx*** functions are declared in *miniport.h* or, for 32-bit (x86) drivers, in *storport.h*.
