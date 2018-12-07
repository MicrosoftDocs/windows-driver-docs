---
title: Specifying device state and frame latency in WDDM 1.3
ms.assetid: 97FC54BD-0D20-4235-B914-5F44690274AE
description: Starting in Windows Display Driver Model (WDDM) 1.3, user-mode display drivers can use escape flags to pass device status and frame latency info to the display miniport driver.
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Specifying device state and frame latency in WDDM 1.3


Starting in Windows Display Driver Model (WDDM) 1.3, user-mode display drivers can use escape flags to pass device status and frame latency info to the display miniport driver when the [*pfnEscapeCb*](https://msdn.microsoft.com/library/windows/hardware/ff568908) function is called. These flags are available in the [**D3DDDI\_ESCAPEFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544541) structure starting in Windows 8.1.

These reference topics describe how to implement this capability in your user-mode display driver:

-   [**D3DDDI\_DEVICEEXECUTION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/dn482416)
-   [**D3DDDI\_EXECUTIONSTATEESCAPE**](https://msdn.microsoft.com/library/windows/hardware/dn482417)
-   [**D3DDDI\_FRAMELATENCYESCAPE**](https://msdn.microsoft.com/library/windows/hardware/dn482418)
-   [**D3DDDI\_ESCAPEFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544541) (new **DeviceStatusQuery** and **ChangeFrameLatency** members)

 

 





