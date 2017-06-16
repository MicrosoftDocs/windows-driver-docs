---
title: Using Packet-Based Bus-Master DMA
author: windows-driver-content
description: Using Packet-Based Bus-Master DMA
ms.assetid: 57b37103-8ae0-4c54-b613-55b1a629d9ae
keywords: ["bus-master DMA WDK kernel", "DMA transfers WDK kernel , bus-master DMA", "adapter objects WDK kernel , bus-master DMA"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Packet-Based Bus-Master DMA


## <a href="" id="ddk-using-packet-based-bus-master-dma-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Packet-Based%20Bus-Master%20DMA%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


