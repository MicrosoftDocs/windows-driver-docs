---
title: Threading and Synchronization Third Level
description: Threading and Synchronization Third Level
ms.assetid: 780d37d9-40c6-4737-9042-473810868227
keywords:
- threading WDK display , third level
- synchronization WDK display , third level
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Threading%20and%20Synchronization%20Third%20Level%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




