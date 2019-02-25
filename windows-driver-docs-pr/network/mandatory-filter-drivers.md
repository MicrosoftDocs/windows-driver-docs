---
title: Mandatory Filter Drivers
description: Mandatory Filter Drivers
ms.assetid: 7be7cb9d-d0a6-4d4b-9dc1-2fef73b1f10e
keywords:
- filter drivers WDK networking , mandatory
- NDIS filter drivers WDK , mandatory
- mandatory filter drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mandatory Filter Drivers





Mandatory filter drivers are filter drivers that must be present for a driver stack to function properly. If the mandatory filter module does not attach, the rest of the driver stack will be torn down. [Modifying or monitoring filter drivers](types-of-filter-drivers.md) can be mandatory. All filter intermediate drivers are optional.

To attach a mandatory filter module to a driver stack, NDIS unbinds all the protocol bindings, attaches the filter module, and then reestablishes all the protocol bindings. If the driver does not attach, NDIS tears down the underlying driver stack.

To detach a mandatory filter module from a driver stack, NDIS unbinds all the protocol bindings detaches the filter module, and then reestablishes the protocol bindings. To detach an optional filter module, NDIS pauses the stack and restarts it without unbinding the protocol drivers.

When a computer restarts, NDIS will not bind any protocol drivers to a miniport adapter if any mandatory filter module that is associated with the adapter does not attach to the miniport adapter.

To install a mandatory filter driver, you must specify a value of 0x00000001 for **FilterRunType** in the INF file. To install an optional filter driver, you must specify a value of 0x00000002 for **FilterRunType** in the INF file.

 

 





