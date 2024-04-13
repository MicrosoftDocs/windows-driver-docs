---
title: Using Packet-Based System DMA
description: Using Packet-Based System DMA
keywords: ["system DMA WDK kernel , packet-based", "packet-based DMA WDK kernel", "DMA transfers WDK kernel , packet-based"]
ms.date: 06/16/2017
---

# Using Packet-Based System DMA





Drivers of subordinate devices that use packet-based DMA call the following general sequence of support routines as they process an IRP requesting a DMA transfer:

-   [**KeFlushIoBuffers**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keflushiobuffers) just before attempting to allocate the system DMA controller (for more information, see [Maintaining Cache Coherency](maintaining-cache-coherency.md))

-   [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel) when the driver is ready to program its device for DMA and needs the system DMA controller

    **AllocateAdapterChannel**, in turn, calls the driver's [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine.

-   [**MmGetMdlVirtualAddress**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetmdlvirtualaddress) to get an index into the MDL, required as an parameter in the initial call to **MapTransfer**

-   [**MapTransfer**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pmap_transfer) to program the system DMA controller for the transfer operation

    A driver might need to call **MapTransfer** more than once to transfer all the requested data, as explained in [Splitting Transfer Requests](splitting-dma-transfer-requests.md).

-   [**FlushAdapterBuffers**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pflush_adapter_buffers) just after each DMA transfer operation to/from the subordinate device

    If a driver must call **MapTransfer** more than once to transfer all the requested data, it must call **FlushAdapterBuffers** as many times as it calls **MapTransfer**.

-   [**FreeAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel) either as soon as all the requested data has been transferred or if the driver fails the IRP because of a device I/O error

The adapter object pointer returned by [**IoGetDmaAdapter**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdmaadapter) is a required parameter to each of these routines except **KeFlushIoBuffers** and **MmGetMdlVirtualAddress**, which require the pointer to the MDL passed at **Irp-&gt;MdlAddress**.

Individual drivers call this sequence of support routines at different points, depending on how each driver is implemented to service its device. For example, one driver's [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine might make the call to **AllocateAdapterChannel**, another driver might make this call from a routine that removes IRPs from a driver-created interlocked queue, and still another driver might make this call when its subordinate DMA device indicates it is ready to transfer data.

 

