---
title: Threading and Synchronization Level Three
description: Threading and Synchronization Level Three
keywords:
- threading WDK display , Level Three
- synchronization WDK display , Level Three
ms.date: 10/03/2023
---

# Threading and Synchronization Level Three

Level Three threading and synchronization ensures that:

* Only a single thread (the calling thread) is within the kernel-mode driver.
* The graphics hardware is idle.
* No direct memory access (DMA) buffers are currently being processed by the driver or passed through the GPU scheduler
* The video memory is completely evicted to host CPU memory.

WDDM guarantees that calls such as the following into the display miniport driver are made under the Level Three of threading and synchronization.

* [*DxgkDdiAddDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_add_device)

* [*DxgkDdiQueryChildRelations*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_relations)

* [*DxgkDdiRemoveDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_remove_device)

* [*DxgkDdiResetFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetfromtimeout)

* [*DxgkDdiRestartFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_restartfromtimeout)

* [*DxgkDdiSetPowerState*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_set_power_state)

* [*DxgkDdiStartDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device)

* [*DxgkDdiStopDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_stop_device)

* [*DxgkDdiUnload*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_unload)
