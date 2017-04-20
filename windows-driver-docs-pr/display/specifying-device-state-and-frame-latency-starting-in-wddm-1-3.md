---
title: Specifying device state and frame latency starting in WDDM 1.3
ms.assetid: 97FC54BD-0D20-4235-B914-5F44690274AE
description: Implementing escape flags to pass info to the miniport driver
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Specifying device state and frame latency starting in WDDM 1.3


Windows Display Driver Model (WDDM) 1.3 and later user-mode display drivers can use escape flags to pass device status and frame latency info to the display miniport driver when the [*pfnEscapeCb*](https://msdn.microsoft.com/library/windows/hardware/ff568908) function is called. These flags are available in the [**D3DDDI\_ESCAPEFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544541) structure starting in Windows 8.1.

These reference topics describe how to implement this capability in your user-mode display driver:

-   [**D3DDDI\_DEVICEEXECUTION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/dn482416)
-   [**D3DDDI\_EXECUTIONSTATEESCAPE**](https://msdn.microsoft.com/library/windows/hardware/dn482417)
-   [**D3DDDI\_FRAMELATENCYESCAPE**](https://msdn.microsoft.com/library/windows/hardware/dn482418)
-   [**D3DDDI\_ESCAPEFLAGS**](https://msdn.microsoft.com/library/windows/hardware/ff544541) (new **DeviceStatusQuery** and **ChangeFrameLatency** members)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Specifying%20device%20state%20and%20frame%20latency%20starting%20in%20WDDM%201.3%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




