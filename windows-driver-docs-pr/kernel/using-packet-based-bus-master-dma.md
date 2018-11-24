---
title: Using Packet-Based Bus-Master DMA
description: Using Packet-Based Bus-Master DMA
ms.assetid: 57b37103-8ae0-4c54-b613-55b1a629d9ae
keywords: ["bus-master DMA WDK kernel", "DMA transfers WDK kernel , bus-master DMA", "adapter objects WDK kernel , bus-master DMA"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using Packet-Based Bus-Master DMA





To use packet-based DMA, drivers of bus-master DMA devices call the following general sequence of support routines as they process an IRP requesting a DMA transfer:

-   [**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041) just before attempting to allocate map registers for a transfer request (for more information, see [Maintaining Cache Coherency](maintaining-cache-coherency.md))

-   [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573) when the driver is ready to program the bus-master adapter for DMA

-   [**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539) to get an index into the MDL, required as an initial parameter to [**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402), and **MapTransfer** to make the system physical memory that backs the IRP's buffer device-accessible

    Note that any driver might need to carry out more than one transfer operation in order to satisfy the current IRP, as explained in [Splitting Transfer Requests](splitting-dma-transfer-requests.md). Drivers of devices that do not have scatter/gather capabilities can call **MapTransfer** once per transfer operation. Drivers of devices that have scatter/gather capabilities can call **MapTransfer** more than once to set up each transfer operation. Alternatively, these drivers can use the system's built-in scatter/gather support, described in [Using Scatter/Gather DMA](using-scatter-gather-dma.md).

-   [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917) at the end of each DMA transfer operation to/from the target device, in order to determine whether all the requested data has been completely transferred

-   [**FreeMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff546513) as soon as all DMA operations for the current IRP are done, because all the requested data has been completely transferred or because the driver must fail the IRP due to a device or bus I/O error

The adapter object pointer returned by [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220) is a required parameter to **AllocateAdapterChannel**, **MapTransfer**, **FlushAdapterBuffers**, and **FreeMapRegisters**. Note that in versions of Windows NT prior to Windows 2000, bus-master devices could pass a **NULL** adapter object pointer to **MapTransfer** and **FlushAdapterBuffers**. In Windows 2000 and later, drivers can no longer do so.

**KeFlushIoBuffers** and **MmGetMdlVirtualAddress** require a pointer to the MDL at **Irp-&gt;MdlAddress**.

Individual drivers call this sequence of support routines at different points, depending on how each driver is implemented to service its device. For example, one driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine might make the call to **AllocateAdapterChannel**, while another driver might make this call from a routine that removes IRPs from a driver-created interlocked queue or device queue.

Instead of using the routines described in this section, any driver that uses packet-based DMA can use support routines intended to streamline scatter/gather DMA, regardless of whether its device has built-in scatter/gather support. See [Using Scatter/Gather DMA](using-scatter-gather-dma.md) for details.

 

 




