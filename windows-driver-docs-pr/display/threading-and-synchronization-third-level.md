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

-   [*DxgkDdiAddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559586)

-   [*DxgkDdiQueryChildRelations*](https://msdn.microsoft.com/library/windows/hardware/ff559750)

-   [*DxgkDdiRemoveDevice*](https://msdn.microsoft.com/library/windows/hardware/ff559789)

-   [*DxgkDdiResetFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559815)

-   [*DxgkDdiRestartFromTimeout*](https://msdn.microsoft.com/library/windows/hardware/ff559820)

-   [*DxgkDdiSetPowerState*](https://msdn.microsoft.com/library/windows/hardware/ff560764)

-   [*DxgkDdiStartDevice*](https://msdn.microsoft.com/library/windows/hardware/ff560775)

-   [*DxgkDdiStopDevice*](https://msdn.microsoft.com/library/windows/hardware/ff560781)

-   [*DxgkDdiUnload*](https://msdn.microsoft.com/library/windows/hardware/ff560801)

 

 





