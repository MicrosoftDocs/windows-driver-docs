---
title: Threading and Synchronization Second Level
description: Threading and Synchronization Second Level
ms.assetid: 2b7c1eae-6527-469e-a2fa-74d2a1246bd3
keywords:
- threading WDK display , second level
- synchronization WDK display , second level
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Threading and Synchronization Second Level


The second level of threading and synchronization is the same as [the third level](threading-and-synchronization-third-level.md), except that video memory is not evicted to host CPU memory. In other words, the Windows Display Driver Model (WDDM) guarantees that only a single thread (that is, the calling thread) is within the display miniport driver, the graphics hardware is idle, and no direct memory access (DMA) buffers are currently being processed by the driver or passed through the GPU scheduler. The following calls into the display miniport driver are made under the second level:

**Note**   In order for some calls to be made under the second level, the **HardwareAccess** flag must be set within the **D3DDDI\_ESCAPEFLAGS** structure that is a member of **DXGKARG\_ESCAPE**. If this flag is not set, then the call will fail.

 

-   [*DxgkDdiCommitVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559597)

-   [*DxgkDdiControlInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559602)

-   [*DxgkDdiDispatchIoRequest*](https://msdn.microsoft.com/library/windows/hardware/ff559643)

-   [*DxgkDdiEscape*](https://msdn.microsoft.com/library/windows/hardware/ff559653)

-   [*DxgkDdiNotifyAcpiEvent*](https://msdn.microsoft.com/library/windows/hardware/ff559695)

-   [*DxgkDdiQueryInterface*](https://msdn.microsoft.com/library/windows/hardware/ff559764)

-   [*DxgkDdiRecommendFunctionalVidPn*](https://msdn.microsoft.com/library/windows/hardware/ff559775)

-   [*DxgkDdiRecommendMonitorModes*](https://msdn.microsoft.com/library/windows/hardware/ff559780)

-   [*DxgkDdiSetPalette*](https://msdn.microsoft.com/library/windows/hardware/ff560754)

-   [*DxgkDdiSetVidPnSourceAddress*](https://msdn.microsoft.com/library/windows/hardware/ff560767)

-   [*DxgkDdiSetVidPnSourceVisibility*](https://msdn.microsoft.com/library/windows/hardware/ff560771)

-   [*DxgkDdiUpdateActiveVidPnPresentPath*](https://msdn.microsoft.com/library/windows/hardware/ff560803)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Threading%20and%20Synchronization%20Second%20Level%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




