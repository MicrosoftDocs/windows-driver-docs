---
title: Allocating Nonpaged Display Memory
description: Allocating Nonpaged Display Memory
ms.assetid: 6a8523e7-3955-4289-b131-52556ba3e631
keywords:
- nonpaged display memory WDK DirectX 9.0
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Allocating Nonpaged Display Memory


## <span id="ddk_allocating_nonpaged_display_memory_gg"></span><span id="DDK_ALLOCATING_NONPAGED_DISPLAY_MEMORY_GG"></span>


**This topic applies only to Microsoft Windows XP and later.**

A DirectX 9.0 version display driver can call the [**EngAllocMem**](https://msdn.microsoft.com/library/windows/hardware/ff564176) graphics device interface (GDI) function to not only allocate memory from the system's paged pool but also from nonpaged pool. To allocate nonpaged memory, the driver must specify the FL\_NONPAGED\_MEMORY flag in the *Flags* parameter of the **EngAllocMem** call. If this flag is not specified, the memory is allocated from the system's paged pool.

Windows 2000 and earlier only permitted allocations from the system's paged pool.

Although this feature of allocating from nonpaged pool was available in WindowsXP and later, it was not documented in the Windows XP and Windows XP with Service Pack 1 (SP1) DDKs.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Allocating%20Nonpaged%20Display%20Memory%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




