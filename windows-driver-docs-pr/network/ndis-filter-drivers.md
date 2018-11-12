---
title: Filter drivers
description: Filter drivers
ms.assetid: 626547ba-4c26-4be7-b209-c5e26daf56ab
keywords:
- filter drivers WDK networking , architecture
- NDIS filter drivers WDK , architecture
- filter modules WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter drivers





NDIS 6.0 introduced NDIS filter drivers. Filter drivers can monitor and modify the interaction between protocol drivers and miniport drivers. Filter drivers are easier to implement and have less processing overhead than NDIS intermediate drivers.

A *filter module* is an instance of a filter driver. As the following figure illustrates, filter modules are typically layered between miniport adapters and protocol bindings.

![diagram illustrating an ndis driver stack with filter modules](images/filterstack.png)

A filter driver communicates with NDIS and other NDIS drivers through the NDIS library. The NDIS library exports a full set of functions (**NdisF*Xxx*** and other **Ndis*Xxx*** functions) that encapsulate all of the operating system functions that a filter driver must call. The filter driver, in turn, must export a set of entry points (*FilterXxx* functions) that NDIS calls for its own purposes, or on behalf of other drivers, to access the filter driver.

## Related topics


[NDIS Filter Drivers](ndis-filter-drivers2.md)

[NDIS Filter Driver Reference](https://msdn.microsoft.com/library/windows/hardware/ff565527)

 

 






