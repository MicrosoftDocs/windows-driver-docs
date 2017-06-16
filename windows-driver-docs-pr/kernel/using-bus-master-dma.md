---
title: Using Bus-Master DMA
author: windows-driver-content
description: Using Bus-Master DMA
ms.assetid: 08357a55-aec2-4454-923f-6daaf1583a25
keywords: ["AdapterControl routines, bus-master DMA", "bus-master DMA WDK kernel", "DMA transfers WDK kernel , bus-master DMA", "adapter objects WDK kernel , bus-master DMA"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Bus-Master DMA


## <a href="" id="ddk-using-bus-master-dma-kg"></a>


Drivers of bus-master DMA devices can use the following kinds of system-supplied DMA support:

-   Packet-based DMA if the bus-master adapter allows the driver to determine when a DMA transfer operation is done and/or when to begin another transfer operation for a given IRP. See [Using Packet-Based Bus-Master DMA](using-packet-based-bus-master-dma.md) for details.

-   Common-buffer DMA (also called *continuous DMA*) if the bus-master adapter does not provide a way for the driver to determine readily when a transfer operation will begin or when a transfer is complete, or if a single buffer area is used continuously or repeatedly for DMA transfers. See [Using Common-Buffer Bus-Master DMA](using-common-buffer-bus-master-dma.md) for details.

Depending on the nature of the bus-master adapter, some drivers use packet-based DMA exclusively, some use common-buffer DMA exclusively, and some use both. For example, the driver of a bus-master adapter that uses a mailbox scheme to communicate status information and commands might use a common buffer for the mailboxes shared between the driver and its adapter, together with packet-based DMA for data transfers.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Bus-Master%20DMA%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


