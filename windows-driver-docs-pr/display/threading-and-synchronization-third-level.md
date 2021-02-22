---
title: Threading and Synchronization Third Level
description: Threading and Synchronization Third Level
keywords:
- threading WDK display , third level
- synchronization WDK display , third level
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Threading and Synchronization Third Level


The Windows Display Driver Model (WDDM) guarantees that the following calls into the display miniport driver are made under the third level of threading and synchronization. This ensures that only a single thread (that is, the calling thread) is within the driver. In addition, the graphics hardware is idle, no direct memory access (DMA) buffers are currently being processed by the driver or passed through the GPU scheduler, and the video memory is completely evicted to host CPU memory.

-   [*DxgkDdiAddDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_add_device)

-   [*DxgkDdiQueryChildRelations*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_relations)

-   [*DxgkDdiRemoveDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_remove_device)

-   [*DxgkDdiResetFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetfromtimeout)

-   [*DxgkDdiRestartFromTimeout*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_restartfromtimeout)

-   [*DxgkDdiSetPowerState*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_set_power_state)

-   [*DxgkDdiStartDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device)

-   [*DxgkDdiStopDevice*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_stop_device)

-   [*DxgkDdiUnload*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_unload)

 

