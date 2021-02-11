---
title: Specifying device state and frame latency in WDDM 1.3
description: Starting in Windows Display Driver Model (WDDM) 1.3, user-mode display drivers can use escape flags to pass device status and frame latency info to the display miniport driver.
ms.date: 12/06/2018
ms.localizationpriority: medium
ms.custom: seodec18
---

# Specifying device state and frame latency in WDDM 1.3


Starting in Windows Display Driver Model (WDDM) 1.3, user-mode display drivers can use escape flags to pass device status and frame latency info to the display miniport driver when the [*pfnEscapeCb*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_escapecb) function is called. These flags are available in the [**D3DDDI\_ESCAPEFLAGS**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_escapeflags) structure starting in Windows 8.1.

These reference topics describe how to implement this capability in your user-mode display driver:

-   [**D3DDDI\_DEVICEEXECUTION\_STATE**](/windows-hardware/drivers/ddi/d3dumddi/ne-d3dumddi-_d3dddi_deviceexecution_state)
-   [**D3DDDI\_EXECUTIONSTATEESCAPE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_executionstateescape)
-   [**D3DDDI\_FRAMELATENCYESCAPE**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_framelatencyescape)
-   [**D3DDDI\_ESCAPEFLAGS**](/windows-hardware/drivers/ddi/d3dukmdt/ns-d3dukmdt-_d3dddi_escapeflags) (new **DeviceStatusQuery** and **ChangeFrameLatency** members)

 

