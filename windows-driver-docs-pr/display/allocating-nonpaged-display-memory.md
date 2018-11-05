---
title: Allocating Nonpaged Display Memory
description: Allocating Nonpaged Display Memory
ms.assetid: 6a8523e7-3955-4289-b131-52556ba3e631
keywords:
- nonpaged display memory WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Allocating Nonpaged Display Memory


## <span id="ddk_allocating_nonpaged_display_memory_gg"></span><span id="DDK_ALLOCATING_NONPAGED_DISPLAY_MEMORY_GG"></span>


**This topic applies only to Microsoft Windows XP and later.**

A DirectX 9.0 version display driver can call the [**EngAllocMem**](https://msdn.microsoft.com/library/windows/hardware/ff564176) graphics device interface (GDI) function to not only allocate memory from the system's paged pool but also from nonpaged pool. To allocate nonpaged memory, the driver must specify the FL\_NONPAGED\_MEMORY flag in the *Flags* parameter of the **EngAllocMem** call. If this flag is not specified, the memory is allocated from the system's paged pool.

Windows 2000 and earlier only permitted allocations from the system's paged pool.

Although this feature of allocating from nonpaged pool was available in WindowsXP and later, it was not documented in the Windows XP and Windows XP with Service Pack 1 (SP1) DDKs.

 

 





