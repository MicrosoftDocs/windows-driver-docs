---
title: Unloading a Filter Driver
description: Unloading a Filter Driver
keywords:
- filter drivers WDK networking , unloading
- NDIS filter drivers WDK , unloading
- unloading filter drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Unloading a Filter Driver





The driver object that is associated with an NDIS filter driver specifies an [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine called *FilterDriverUnload*. The system can call the *FilterDriverUnload* routine when all the miniport adapters that the filter driver services have been removed.

[*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) should release any driver-specific resources. Any device objects that the filter driver created must be destroyed. The system can complete a driver unload operation after *FilterDriverUnload* returns.

The functionality of the unload function is driver-specific. As a general rule, [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) should undo the operations that were performed during driver initialization. For more information about driver initialization, see [Initializing a Filter Driver](initializing-a-filter-driver.md).

A filter driver must call the [**NdisFDeregisterFilterDriver**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisfderegisterfilterdriver) function from [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload). **NdisFDeregisterFilterDriver** calls [*FilterDetach*](/windows-hardware/drivers/ddi/ndis/nc-ndis-filter_detach) to detach all currently attached filter modules that are associated with this filter driver.

For more information about unloading filter drivers, see [Stopping a Driver Stack](stopping-a-driver-stack.md).
