---
title: WLAN Universal Windows driver model
description: The WLAN Universal Windows driver model was released in Windows 10 and is superseded by WiFiCx in Windows 11.
ms.date: 03/16/2022
---

# WLAN Universal Windows driver model

> [!IMPORTANT]
> [WiFiCx](../netcx/wifi-wdf-class-extension-wificx.md) is the new Wi-Fi driver model released in Windows 11. We recommend that you use WiFiCx to take advantage of the latest  features. The WDI driver model is now in maintenance mode and will only receive high priority fixes. 

WDI (WLAN Device Driver Interface) is a Universal Windows driver model released in Windows 10. WLAN device manufacturers can write a single WDI miniport driver that runs on all device platforms, and requires less code than the previous native WLAN driver model. All new WLAN features introduced in Windows 10 require WDI-based drivers.

Vendor-supplied native WLAN drivers continue to work in Windows 10, but functionality is limited to the version of Windows for which they were developed.

The WDI header files, wditypes.hpp and dot11wdi.h, are included in the WDK.

## How to write a universal WLAN driver


To write a universal WLAN driver, see [Getting Started with Universal Windows drivers](/windows-hardware/drivers), and follow the steps in the section titled *Building a Universal Windows driver* to build a universal driver using the Kernel Mode Driver (KMDF) template.

Then, see the WDI design and reference sections for implementation guidance.

-   [WDI Miniport Driver Design Guide](wdi-miniport-driver-design-guide.md)
-   [WDI Miniport Driver Reference](/windows-hardware/drivers/ddi/_netvista/#wireless-networking)

## Related topics


[Getting Started with Universal Windows drivers](/windows-hardware/drivers)

 

