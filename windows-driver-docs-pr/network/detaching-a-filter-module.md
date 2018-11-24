---
title: Detaching a Filter Module
description: Detaching a Filter Module
ms.assetid: ef987f2f-a681-4ddb-959a-1becdf633678
keywords:
- filter modules WDK networking , detaching
- detaching filter modules
- filter drivers WDK networking , detaching filter modules
- NDIS filter drivers WDK , detaching filter modules
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Detaching a Filter Module





To initiate the process of detaching a filter module from a driver stack, NDIS calls a filter driver's [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function. At the start of execution in the *FilterDetach* function, the filter module enters the *Detached* state. Before detaching a filter module, NDIS must pause the driver stack. For more information about pausing the driver stack, see [Pausing a Driver Stack](pausing-a-driver-stack.md).

In its *FilterDetach* function, the driver frees its context areas and other resources (such as buffer pools) for the affected filter module. A filter driver cannot fail the call to *FilterDetach*. Therefore, filter drivers should preallocate, during the attach operation, all the resources required to perform the detach operation successfully. For more information about attaching a filter module, see [Attaching a Filter Module](attaching-a-filter-module.md).

After the filter module returns from *FilterDetach*, NDIS can start the paused driver stack. For more information about starting a driver stack, see [Starting a Driver Stack](starting-a-driver-stack.md).

 

 





