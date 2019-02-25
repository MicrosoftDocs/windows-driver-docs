---
title: WLAN Universal Windows driver model
description: WDI (WLAN Device Driver Interface) is the new Universal Windows driver model for Windows 10.
ms.assetid: 6EF92E34-7BC9-465E-B05D-2BCB29165A18
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WLAN Universal Windows driver model


WDI (WLAN Device Driver Interface) is the new Universal Windows driver model for Windows 10. WLAN device manufacturers can write a single WDI miniport driver that runs on all device platforms, and requires less code than the previous native WLAN driver model. All new WLAN features introduced in Windows 10 require WDI-based drivers.

Vendor-supplied native WLAN drivers continue to work in Windows 10, but functionality is limited to the version of Windows for which they were developed.

The WDI header files, wditypes.hpp and dot11wdi.h, are included in the WDK.

## How to write a universal WLAN driver


To write a universal WLAN driver, see [Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers), and follow the steps in the section titled *Building a Universal Windows driver* to build a universal driver using the Kernel Mode Driver (KMDF) template.

Then, see the WDI design and reference sections for implementation guidance.

-   [WDI Miniport Driver Design Guide](wdi-miniport-driver-design-guide.md)
-   [WDI Miniport Driver Reference](https://msdn.microsoft.com/library/windows/hardware/dn926075)

## Related topics


[Getting Started with Universal Windows drivers](https://msdn.microsoft.com/windows-drivers/develop/getting_started_with_universal_drivers)

 

 






