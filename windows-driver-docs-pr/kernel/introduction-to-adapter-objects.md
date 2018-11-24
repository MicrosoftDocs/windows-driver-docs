---
title: Introduction to Adapter Objects
description: Introduction to Adapter Objects
ms.assetid: a1a0d516-dee0-484a-b971-c7a595fef155
keywords: ["AdapterControl routines, about AdapterControl routines", "DMA transfers WDK kernel , adapter objects", "adapter objects WDK kernel , about adapter objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to Adapter Objects





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

 

 




