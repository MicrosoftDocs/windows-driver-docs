---
title: Creating Resource Maps for a Multifunction Device
description: Resource maps identify the resources of a multifunction device that are used by a child function.
keywords:
- multifunction devices WDK , resource maps
- resource maps WDK multifunction devices
- child function resource maps WDK
ms.date: 03/17/2023
---

# Creating Resource Maps for a Multifunction Device

A *resource map* identifies the resources of a multifunction device that are used by a child function. Resource maps are specified using an [**INF AddReg directive**](../install/inf-addreg-directive.md). If a multifunction device requires resource maps, the INF for the device typically contains a resource map for each function of the device.

There are two types of resource maps − *standard* resource maps and *varying* resource maps. This section describes how to construct resource maps and includes the following topics:

[Creating Standard Resource Maps](creating-standard-resource-maps.md)

[Creating Varying Resource Maps](creating-varying-resource-maps.md)

Some multifunction devices can be described using only standard resource maps. Others require varying resource maps, or a combination of standard and varying maps. Still others require no resource maps at all. See [Supporting Multifunction PC Card Devices](supporting-multifunction-pc-card-devices.md) to determine which multifunction devices require resource maps.
