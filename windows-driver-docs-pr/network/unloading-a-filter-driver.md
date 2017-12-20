---
title: Unloading a Filter Driver
description: Unloading a Filter Driver
ms.assetid: e7ef209f-ab61-4644-a641-2fef09023a24
keywords:
- filter drivers WDK networking , unloading
- NDIS filter drivers WDK , unloading
- unloading filter drivers
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Unloading a Filter Driver


## <a href="" id="ddk-unloading-a-filter-driver-ng"></a>


The driver object that is associated with an NDIS filter driver specifies an [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine called *FilterDriverUnload*. The system can call the *FilterDriverUnload* routine when all the miniport adapters that the filter driver services have been removed.

[*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) should release any driver-specific resources. Any device objects that the filter driver created must be destroyed. The system can complete a driver unload operation after *FilterDriverUnload* returns.

The functionality of the unload function is driver-specific. As a general rule, [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) should undo the operations that were performed during driver initialization. For more information about driver initialization, see [Initializing a Filter Driver](initializing-a-filter-driver.md).

A filter driver must call the [**NdisFDeregisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561800) function from [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886). **NdisFDeregisterFilterDriver** calls [*FilterDetach*](https://msdn.microsoft.com/en-us/library/windows/hardware/ff549918) to detach all currently attached filter modules that are associated with this filter driver.

For more information about unloading filter drivers, see [Stopping a Driver Stack](stopping-a-driver-stack.md).