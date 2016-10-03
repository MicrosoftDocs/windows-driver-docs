---
title: Unloading a Filter Driver
description: Unloading a Filter Driver
ms.assetid: e7ef209f-ab61-4644-a641-2fef09023a24
keywords: ["filter drivers WDK networking , unloading", "NDIS filter drivers WDK , unloading", "unloading filter drivers"]
---

# Unloading a Filter Driver


## <a href="" id="ddk-unloading-a-filter-driver-ng"></a>


The driver object that is associated with an NDIS filter driver specifies an [*FilterDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff549936) routine. The system can call the *FilterDriverUnload* routine when all the miniport adapters that the filter driver services have been removed.

[*FilterDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff549936) should release any driver-specific resources. Any device objects that the filter driver created must be destroyed. The system can complete a driver unload operation after *FilterDriverUnload* returns.

The functionality of the unload function is driver-specific. As a general rule, [*FilterDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff549936) should undo the operations that were performed during driver initialization. For more information about driver initialization, see [Initializing a Filter Driver](initializing-a-filter-driver.md).

A filter driver must call the [**NdisFDeregisterFilterDriver**](https://msdn.microsoft.com/library/windows/hardware/ff561800) function from [*FilterDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff549936).

**Note**  The system does not call [*FilterDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff549936) until after NDIS calls the [*FilterDetach*](https://msdn.microsoft.com/library/windows/hardware/ff549918) function to detach all the filter modules that are associated with the driver.

 

For more information about unloading filter drivers, see [Stopping a Driver Stack](stopping-a-driver-stack.md).

 

 





