---
title: Installing a New Bus Driver
description: Installing a New Bus Driver
ms.assetid: 449c0c08-c995-4e23-a770-a567bd48966c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a New Bus Driver


New vendor bus drivers should comply with the following guidelines for reporting the bus type and device IDs, and, possibly, for creating a new [device setup class](device-setup-classes.md) for the child devices on the bus. These guidelines apply to a new vendor bus if the configuration or operation of the bus and its child devices differ significantly from other buses. In those cases, new vendor bus drivers should do the following to ensure that the bus and its child devices are not unintentionally and inappropriately grouped with other buses and child devices:

1.  Use a unique GUID to identify the bus type. A bus driver reports the bus type of a child device (represented as a physical device object ([*PDO*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdo)) in response to an [**IRP_MN_QUERY_BUS_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff551654) request for the child device. In response to such a request, the bus driver returns a pointer to a [**PNP_BUS_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff559608) structure that returns the GUID in the **PNP_BUS_INFORMATION.BusTypeGuid** member. In addition, the bus driver should set **PNP_BUS_INFORMATION.LegacyBusType** to **PNPBus**, and **PNP_BUS_INFORMATION.BusNumber** to an appropriate custom value.

2.  [Use custom hardware IDs](using-custom-hardware-ids-and-compatible-ids.md) to uniquely identify the bus [*enumerator*](https://msdn.microsoft.com/library/windows/hardware/ff556279#wdkgloss-enumerator) and the child devices of the bus.

3.  If the child devices of the bus do not belong to an existing [device setup class](device-setup-classes.md), [install a new device setup class for the child devices of the bus](installing-a-new-device-setup-class-for-a-bus.md).

 

 





