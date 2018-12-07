---
title: Using Bus-Master DMA
description: Using Bus-Master DMA
ms.assetid: 08357a55-aec2-4454-923f-6daaf1583a25
keywords: ["AdapterControl routines, bus-master DMA", "bus-master DMA WDK kernel", "DMA transfers WDK kernel , bus-master DMA", "adapter objects WDK kernel , bus-master DMA"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Bus-Master DMA





Drivers of bus-master DMA devices can use the following kinds of system-supplied DMA support:

-   Packet-based DMA if the bus-master adapter allows the driver to determine when a DMA transfer operation is done and/or when to begin another transfer operation for a given IRP. See [Using Packet-Based Bus-Master DMA](using-packet-based-bus-master-dma.md) for details.

-   Common-buffer DMA (also called *continuous DMA*) if the bus-master adapter does not provide a way for the driver to determine readily when a transfer operation will begin or when a transfer is complete, or if a single buffer area is used continuously or repeatedly for DMA transfers. See [Using Common-Buffer Bus-Master DMA](using-common-buffer-bus-master-dma.md) for details.

Depending on the nature of the bus-master adapter, some drivers use packet-based DMA exclusively, some use common-buffer DMA exclusively, and some use both. For example, the driver of a bus-master adapter that uses a mailbox scheme to communicate status information and commands might use a common buffer for the mailboxes shared between the driver and its adapter, together with packet-based DMA for data transfers.

 

 




