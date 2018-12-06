---
title: Raw and Translated Resources
description: Raw and Translated Resources
ms.assetid: dfc1376d-7a1a-421c-82ae-e183cac77ec8
keywords:
- hardware resources WDK KMDF , raw resources
- resource lists WDK KMDF
- hardware resources WDK KMDF , translated resources
- translated resources WDK KMDF
- raw resources WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Raw and Translated Resources


When a driver's [*EvtDeviceRemoveAddedResources*](https://msdn.microsoft.com/library/windows/hardware/ff540892) or [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function receives a resource list, it receives two versions of the list. One version represents the device's *raw resources*, and the other represents the device's *translated resources*. Both versions represent the same set of hardware resources, in the same order.

-   Raw resources are resources that are identified by addresses that are relative to the bus to which the device is connected. Typically, the driver that programs the device provides these addresses to the device.

-   Translated resources are resources that are identified by system physical addresses that drivers use to access the resources.

A driver for a PCI bus device receives resources that are listed in the order in which they appear in the device’s *Base Address Registers* (BARs). However, additional resource descriptors may be interleaved in the list, such that the resource at index *X* in the BAR might not match the resource at the same index position in the resource list.

For more information about raw and translated resources, see the member descriptions for the [**CM\_PARTIAL\_RESOURCE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff541977) structure.

If a device's translated resource list contains a resource with the **Type** member of the CM\_PARTIAL\_RESOURCE\_DESCRIPTOR structure set to **CmResourceTypeMemory**, every driver that accesses that resource must do the following:

-   The driver's [*EvtDevicePrepareHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540880) callback function must call [**MmMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff554618) to map system physical addresses to system virtual addresses.
-   The driver's [*EvtDeviceReleaseHardware*](https://msdn.microsoft.com/library/windows/hardware/ff540890) callback function must call [**MmUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff556387) to unmap the addresses.

For more information about mapping bus-relative addresses, see [Mapping Bus-Relative Addresses to Virtual Addresses](https://msdn.microsoft.com/library/windows/hardware/ff554399).

 

 





