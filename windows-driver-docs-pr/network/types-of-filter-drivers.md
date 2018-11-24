---
title: Types of Filter Drivers
description: Types of Filter Drivers
ms.assetid: d3a92f10-5f5c-4640-ae03-1bf4e17c45ac
keywords:
- filter drivers WDK networking , types
- NDIS filter drivers WDK , types
- modifying filter drivers WDK networking
- monitoring filter drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Types of Filter Drivers





There are two primary types of filter drivers:

<a href="" id="monitoring"></a>Monitoring  
These filter drivers monitor the behavior in a driver stack. However, they only pass on information and do not modify the behavior of the driver stack. Monitoring filter drivers cannot modify or originate data.

<a href="" id="modifying"></a>Modifying  
These filter drivers modify the behavior of the driver stack. The type of modification is driver-specific.

The **FilterType** entry in the INF file is 0x00000001 for monitoring filter drivers and 0x00000002 for modifying filter drivers.

You can specify that a filter driver is mandatory. This feature is generally used with modifying filter drivers. If a mandatory filter driver does not load, the associated driver stack will be torn down. For more information about mandatory filter drivers, see [Mandatory Filter Drivers](mandatory-filter-drivers.md).

 

 





