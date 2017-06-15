---
title: Introduction to Adapter Objects
author: windows-driver-content
description: Introduction to Adapter Objects
MS-HAID:
- 'ioprogdma\_1a9532bd-cec6-48ef-9c33-b732c8cd2135.xml'
- 'kernel.introduction\_to\_adapter\_objects'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a1a0d516-dee0-484a-b971-c7a595fef155
keywords: ["AdapterControl routines, about AdapterControl routines", "DMA transfers WDK kernel , adapter objects", "adapter objects WDK kernel , about adapter objects"]
---

# Introduction to Adapter Objects


## <a href="" id="ddk-introduction-to-adapter-objects-kg"></a>


Any driver that uses direct I/O and DMA must create an adapter object. The adapter object represents either a DMA controller channel or port, or a bus-master device.

Two kinds of lowest-level drivers must use adapter objects:

-   Drivers for devices that use the system DMA controller. Such devices are called *subordinate devices* and are said to "use system (or *subordinate*) DMA."

-   Drivers for devices that are bus-master adapters. Such devices arbitrate with the system for use of the I/O bus, and thus use bus-master DMA.

Drivers provide storage, usually in a device extension, for a pointer to the adapter object.

To carry out DMA transfers, drivers of devices that use either of these DMA methods usually have an [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine and call system-supplied support routines that manipulate adapter objects. (Drivers that do not require *AdapterControl* routines include those that [use scatter/gather DMA](using-scatter-gather-dma.md) and those that [use common-buffer, bus-master DMA](using-common-buffer-bus-master-dma.md).)

As part of device start-up operations, drivers that handle DMA operations call the I/O manager, which in turn calls the platform-specific HAL to create a set of adapter objects. On any Windows platform, the set of adapter objects usually includes an adapter object for:

-   Each system DMA controller channel or port to which a subordinate device is attached.

-   Each bus-master DMA device in the machine.

(For SCSI devices capable of bus-master DMA, the SCSI port driver sets up adapter objects for HBA-specific SCSI miniport drivers. The miniport driver's [*HwScsiFindAdapter*](https://msdn.microsoft.com/library/windows/hardware/ff557300) routine supplies the port driver with adapter-specific data.)

See [Using System DMA](using-system-dma.md) and [Using Bus-Master DMA](using-bus-master-dma.md) for more information about when and how drivers use adapter objects and *AdapterControl* routines.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20Adapter%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


