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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Bus-Master%20DMA%20in%20Video%20Miniport%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




