---
title: Interlocked Operations in Storport Miniport Drivers
description: Many of the interlocked functions available to Windows applications are appropriate for use in Storport miniport drivers.
ms.assetid: F3868AF4-545F-4B8E-8655-5AAD888C4B40
ms.date: 06/13/2019
ms.localizationpriority: medium
---

# Interlocked Operations in Storport Miniport Drivers

Applications must synchronize access to variables that are shared by multiple threads, using the Platform Software Development Kit (SDK) interlocked functions to do so. Many of the interlocked functions available to Windows applications are appropriate for use in Storport miniport drivers. Most of these functions are implemented as [compiler intrinsic functions](https://docs.microsoft.com/cpp/intrinsics/compiler-intrinsics?view=vs-2019) and are suitable for synchronizing changes to protected values.
Functions are defined for logical, assignment, comparison, and arthimetic operations.

For more information about interlocked operations, see [Interlocked Variable Access](https://docs.microsoft.com/windows/desktop/Sync/interlocked-variable-access).

**Note**  The **Interlocked*Xxx*** functions are declared in *miniport.h* or, for 32-bit (x86) drivers, in *storport.h*.
