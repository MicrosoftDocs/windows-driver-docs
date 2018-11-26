---
title: Windows Kernel-Mode Run-Time Library
description: Windows Kernel-Mode Run-Time Library
ms.assetid: 9c968014-c529-43e1-a8a6-a307c90e4162
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Windows Kernel-Mode Run-Time Library


Windows provides a set of common utility routines needed by various kernel-mode components. For example, [**RtlCheckRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff561754) is used to see if a given key is in the registry.

Most of the run-time library (RTL) routines are prefixed with the letters "**Rtl**"; for a list of the run-time library routines for the kernel, see [Run-Time Library (RTL) Routines](https://msdn.microsoft.com/library/windows/hardware/ff563638).

There is also a different kernel-mode library specifically designed for safe string handling. For more information about the safe string library, see [Windows Kernel-Mode Safe String Library](windows-kernel-mode-safe-string-library.md). Note that safe string library routines are also usually prefixed by "**Rtl**" but are not part of the run-time library (RTL).

 

 




