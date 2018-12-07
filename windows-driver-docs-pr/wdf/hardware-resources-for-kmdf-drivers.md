---
title: Handling Hardware Resources
description: A system's hardware resources are the I/O ports, interrupt vectors, direct memory access (DMA) channels, and other communication paths that must be assigned to each device that is connected to the system.
ms.assetid: 30ceb7db-f11e-498c-a0c0-a63218627c6e
keywords:
- PnP WDK KMDF , hardware resources
- Plug and Play WDK KMDF , hardware resources
- hardware resources WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Hardware Resources


A system's hardware resources are the I/O ports, interrupt vectors, direct memory access (DMA) channels, and other communication paths that must be assigned to each device that is connected to the system. The topics in this section describe how Kernel-Mode Driver Framework (KMDF) drivers negotiate hardware resource requirements for a device, review the proposed resource list, and then receive the assigned resources. This section also discusses how both KMDF and User-Mode Driver Framework (UMDF) drivers access and map assigned resources.




## In this section


-   [Introduction to Hardware Resources](introduction-to-hardware-resources.md)
-   [Framework Objects for Hardware Resources](framework-objects-for-hardware-resources.md)
-   [Creating a Resource Requirements List](creating-a-resource-requirements-list.md)
-   [Modifying a Resource Requirements List](modifying-a-resource-requirements-list.md)
-   [Creating a Resource List for a Boot Configuration](creating-a-resource-list-for-a-boot-configuration.md)
-   [Modifying a Resource List](modifying-a-resource-list.md)
-   [Raw and Translated Resources](raw-and-translated-resources.md)
-   [Finding and Mapping Hardware Resources](finding-and-mapping-hardware-resources.md)
-   [Reading and Writing to Device Registers](reading-and-writing-to-device-registers.md)

 

 





