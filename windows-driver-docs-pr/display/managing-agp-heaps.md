---
title: Managing AGP Heaps
description: Managing AGP Heaps
ms.assetid: edeed3bc-c107-4286-9d5a-7fdef89cc4e1
keywords:
- heaps WDK DirectDraw
- display memory WDK DirectDraw , heaps
- nonlocal display memory WDK DirectDraw , heaps
- AGP WDK DirectDraw , heaps
- drawing AGP support WDK DirectDraw , heaps
- DirectDraw AGP support WDK Windows 2000 display , heaps
- memory WDK DirectDraw AGP , heaps
- GetDriverInfo2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing AGP Heaps


## <span id="ddk_managing_agp_heaps_gg"></span><span id="DDK_MANAGING_AGP_HEAPS_GG"></span>


**This topic applies only to Windows NT-based operating systems.**

A driver can manage AGP heaps using notifications that it receives from the DirectX runtime. The driver receives the notifications from the runtime as **GetDriverInfo2** requests that use the following values:

-   D3DGDI2\_TYPE\_DEFERRED\_AGP\_AWARE

-   D3DGDI2\_TYPE\_FREE\_DEFERRED\_AGP

-   D3DGDI2\_TYPE\_DEFER\_AGP\_FREES

For more information about the **GetDriverInfo2** request, see [Supporting GetDriverInfo2](supporting-getdriverinfo2.md).

When the display device is created, the display driver receives a **GetDriverInfo2** request with the D3DGDI2\_TYPE\_DEFERRED\_AGP\_AWARE notification, which the driver uses to determine if it should disable its other mechanisms that handle AGP heaps and instead use the D3DGDI2\_TYPE\_FREE\_DEFERRED\_AGP and D3DGDI2\_TYPE\_DEFER\_AGP\_FREES notifications that the runtime subsequently sends. In the D3DGDI2\_TYPE\_DEFERRED\_AGP\_AWARE notification, the DirectX runtime provides a pointer to a [**DD\_DEFERRED\_AGP\_AWARE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff550562) structure in the **lpvData** member of the [**DD\_GETDRIVERINFODATA**](https://msdn.microsoft.com/library/windows/hardware/ff551550) data structure.

The driver sometimes receives a **GetDriverInfo2** request with the D3DGDI2\_TYPE\_DEFER\_AGP\_FREES notification before a display mode change occurs. The DirectX runtime only sends this notification if the runtime performs the display mode change. The driver should check the process identifier (PID) of the process destroying the surface against the process that created the surface. If the PIDs are different, the driver should not destroy the user-mode mappings of the AGP memory because an application might still be using the memory.

The driver receives a **GetDriverInfo2** request with the D3DGDI2\_TYPE\_FREE\_DEFERRED\_AGP notification when all display devices within the process stop using surfaces, textures, vertex buffers, and index buffers that were locked at the time of the display mode change. The notification informs the driver that it can safely destroy all of the user-mode mappings of the AGP memory.

In the D3DGDI2\_TYPE\_DEFER\_AGP\_FREES and D3DGDI2\_TYPE\_FREE\_DEFERRED\_AGP notifications, the runtime provides a pointer to a [**DD\_FREE\_DEFERRED\_AGP\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff551528) structure in the **lpvData** member of the DD\_GETDRIVERINFODATA data structure. The **dwProcessId** member of DD\_FREE\_DEFERRED\_AGP\_DATA specifies the PID of the process that destroys the AGP memory.

Note that an application can terminate without the runtime sending the D3DGDI2\_TYPE\_FREE\_DEFERRED\_AGP notification to the driver. Therefore, the driver should free all of the user-mode mappings of the AGP memory when it receives a call to its [**D3dDestroyDDLocal**](https://msdn.microsoft.com/library/windows/hardware/ff544685) function.

 

 





