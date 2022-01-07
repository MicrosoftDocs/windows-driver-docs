---
title: Windows Kernel-Mode Run-Time Library
description: Windows Kernel-Mode Run-Time Library
ms.date: 10/17/2018
---

# Windows Kernel-Mode Run-Time Library


Windows provides a set of common utility routines needed by various kernel-mode components. For example, [**RtlCheckRegistryKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-rtlcheckregistrykey) is used to see if a given key is in the registry.

Most of the run-time library (RTL) routines are prefixed with the letters "**Rtl**"; for a list of the run-time library routines for the kernel, see [Run-Time Library (RTL) Routines](/windows-hardware/drivers/ddi/index).

There is also a different kernel-mode library specifically designed for safe string handling. For more information about the safe string library, see [Windows Kernel-Mode Safe String Library](windows-kernel-mode-safe-string-library.md). Note that safe string library routines are also usually prefixed by "**Rtl**" but are not part of the run-time library (RTL).

 

