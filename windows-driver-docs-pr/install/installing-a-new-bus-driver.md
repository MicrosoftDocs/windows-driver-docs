---
title: Installing a New Bus Driver
description: Installing a New Bus Driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a New Bus Driver


New vendor bus drivers should comply with the following guidelines for reporting the bus type and device IDs for the child devices on the bus. These guidelines apply to a new vendor bus if the configuration or operation of the bus and its child devices differ significantly from other buses. In those cases, new vendor bus drivers should do the following to ensure that the bus and its child devices are not unintentionally and inappropriately grouped with other buses and child devices:

1.  Use a unique GUID to identify the bus type. A bus driver reports the bus type of a child device (represented as a physical device object (*PDO*) in response to an [**IRP_MN_QUERY_BUS_INFORMATION**](../kernel/irp-mn-query-bus-information.md) request for the child device. In response to such a request, the bus driver returns a pointer to a [**PNP_BUS_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_pnp_bus_information) structure that returns the GUID in the **PNP_BUS_INFORMATION.BusTypeGuid** member. In addition, the bus driver should set **PNP_BUS_INFORMATION.LegacyBusType** to **PNPBus**, and **PNP_BUS_INFORMATION.BusNumber** to an appropriate custom value.

2.  [Use custom hardware IDs](using-custom-hardware-ids-and-compatible-ids.md) to uniquely identify the bus *enumerator* and the child devices of the bus.

 

