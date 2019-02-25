---
title: Bus-Master DMA in Video Miniport Drivers
description: Bus-Master DMA in Video Miniport Drivers
ms.assetid: fe6c2e16-d222-4948-b1df-34ed8d57d9d8
keywords:
- video miniport drivers WDK Windows 2000 , bus-master DMA
- bus-master DMA WDK video miniport
- DMA bus-master WDK video miniport
- common-buffer DMA WDK video miniport
- common-buffer DMA WDK video miniport , overview
- packet-based DMA WDK video miniport
- packet-based DMA WDK video miniport , overview
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bus-Master DMA in Video Miniport Drivers


## <span id="ddk_bus_master_dma_in_video_miniport_drivers_gg"></span><span id="DDK_BUS_MASTER_DMA_IN_VIDEO_MINIPORT_DRIVERS_GG"></span>


Beginning with Windows XP, the operating system graphics interface supports DMA on PCI bus-master devices. Video miniport drivers of PCI bus-master devices can implement the following types of DMA support using helper functions supplied by the video port driver:

-   **Packet-based DMA**

    In packet-based DMA, data is transferred directly between the requester's space and the device. Since the requester's space might not be contiguous, packet-based DMA is more efficient on those devices with hardware scatter/gather support. Packet-based DMA is an ideal choice for moving large amounts of arbitrary data between user space and the device.

-   **Common-buffer DMA**

    In common-buffer DMA, a buffer is shared between (hence, common to), and used by both the host and the device for repeated DMA operations. Some drivers use common-buffer DMA to upload driver-manipulated data, such as a series of commands, to the graphics engine. The common buffer is contiguous and is always accessible to both the device and the host CPU.

    The common buffer is a precious system resource. For better overall driver and system performance, drivers should use common-buffer DMA as economically as possible.

Depending on the nature of the bus-master adapter, some miniport drivers use packet-based DMA exclusively, others use common-buffer DMA exclusively, and some use both.

Regardless of which type of DMA is used, the miniport driver should call [**VideoPortGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff570312) to get a pointer to the [**VP\_DMA\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff570570) structure and use it for subsequent DMA functions calls. When there is no longer any need for continued DMA operations, the miniport driver should call [**VideoPortPutDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff570335) to discard the adapter object.

The following subsections describe how to use the packet-based and common-buffer DMA support supplied by the video port driver.

[Packet-Based Bus-Master DMA](packet-based-bus-master-dma.md)

[Common-Buffer Bus-Master DMA](common-buffer-bus-master-dma.md)

[Points to Consider When Using DMA](points-to-consider-when-using-dma.md)

 

 





