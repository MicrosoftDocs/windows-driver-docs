---
title: Windows Kernel-Mode Run-Time Library
author: windows-driver-content
description: Windows Kernel-Mode Run-Time Library
ms.assetid: 9c968014-c529-43e1-a8a6-a307c90e4162
---

# Windows Kernel-Mode Run-Time Library


Windows provides a set of common utility routines needed by various kernel-mode components. For example, [**RtlCheckRegistryKey**](https://msdn.microsoft.com/library/windows/hardware/ff561754) is used to see if a given key is in the registry.

Most of the run-time library (RTL) routines are prefixed with the letters "**Rtl**"; for a list of the run-time library routines for the kernel, see [Run-Time Library (RTL) Routines](https://msdn.microsoft.com/library/windows/hardware/ff563638).

There is also a different kernel-mode library specifically designed for safe string handling. For more information about the safe string library, see [Windows Kernel-Mode Safe String Library](windows-kernel-mode-safe-string-library.md). Note that safe string library routines are also usually prefixed by "**Rtl**" but are not part of the run-time library (RTL).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20Kernel-Mode%20Run-Time%20Library%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


