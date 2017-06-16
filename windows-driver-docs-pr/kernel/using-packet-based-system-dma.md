---
title: Using Packet-Based System DMA
author: windows-driver-content
description: Using Packet-Based System DMA
ms.assetid: 5d175193-4a28-49fd-80b5-18f116232c6e
keywords: ["system DMA WDK kernel , packet-based", "packet-based DMA WDK kernel", "DMA transfers WDK kernel , packet-based"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Packet-Based System DMA


## <a href="" id="ddk-using-packet-based-system-dma-kg"></a>


Drivers of subordinate devices that use packet-based DMA call the following general sequence of support routines as they process an IRP requesting a DMA transfer:

-   [**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041) just before attempting to allocate the system DMA controller (for more information, see [Maintaining Cache Coherency](maintaining-cache-coherency.md))

-   [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573) when the driver is ready to program its device for DMA and needs the system DMA controller

    **AllocateAdapterChannel**, in turn, calls the driver's [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine.

-   [**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539) to get an index into the MDL, required as an parameter in the initial call to **MapTransfer**

-   [**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402) to program the system DMA controller for the transfer operation

    A driver might need to call **MapTransfer** more than once to transfer all the requested data, as explained in [Splitting Transfer Requests](splitting-dma-transfer-requests.md).

-   [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917) just after each DMA transfer operation to/from the subordinate device

    If a driver must call **MapTransfer** more than once to transfer all the requested data, it must call **FlushAdapterBuffers** as many times as it calls **MapTransfer**.

-   [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507) either as soon as all the requested data has been transferred or if the driver fails the IRP because of a device I/O error

The adapter object pointer returned by [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220) is a required parameter to each of these routines except **KeFlushIoBuffers** and **MmGetMdlVirtualAddress**, which require the pointer to the MDL passed at **Irp-&gt;MdlAddress**.

Individual drivers call this sequence of support routines at different points, depending on how each driver is implemented to service its device. For example, one driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine might make the call to **AllocateAdapterChannel**, another driver might make this call from a routine that removes IRPs from a driver-created interlocked queue, and still another driver might make this call when its subordinate DMA device indicates it is ready to transfer data.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Packet-Based%20System%20DMA%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


