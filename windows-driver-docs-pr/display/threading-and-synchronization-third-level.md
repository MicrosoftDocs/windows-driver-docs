---
title: Threading and Synchronization Third Level
description: Threading and Synchronization Third Level
ms.assetid: 780d37d9-40c6-4737-9042-473810868227
keywords:
- threading WDK display , third level
- synchronization WDK display , third level
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Threading and Synchronization Third Level


The Windows Display Driver Model (WDDM) guarantees that the following calls into the display miniport driver are made under the third level of threading and synchronization. This ensures that only a single thread (that is, the calling thread) is within the driver. In addition, the graphics hardware is idle, no direct memory access (DMA) buffers are currently being processed by the driver or passed through the GPU scheduler, and the video memory is completely evicted to host CPU memory.

-   [*DxgkDdiAddDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_add_device)

-   [*DxgkDdiQueryChildRelations*](https://docs.microsoft.com/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_query_child_relations)

-   [*DxgkDdiRemoveDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_remove_device)

-   [*DxgkDdiResetFromTimeout*](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_resetfromtimeout)

-   [*DxgkDdiRestartFromTimeout*](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_restartfromtimeout)

-   [*DxgkDdiSetPowerState*](https://docs.microsoft.com/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_set_power_state)

-   [*DxgkDdiStartDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_start_device)

-   [*DxgkDdiStopDevice*](https://docs.microsoft.com/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_stop_device)

-   [*DxgkDdiUnload*](https://docs.microsoft.com/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_unload)

 

 





