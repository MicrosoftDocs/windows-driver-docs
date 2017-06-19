---
title: Using Scatter/Gather DMA
author: windows-driver-content
description: Using Scatter/Gather DMA
ms.assetid: dacc618f-d4d4-4c3c-a18c-baeef779e931
keywords: ["AdapterListControl routine", "scatter/gather DMA WDK I/O", "PutScatterGatherList", "GetScatterGatherList", "DMA transfers WDK kernel , scatter/gather DMA"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using Scatter/Gather DMA


## <a href="" id="ddk-using-scatter-gather-dma-kg"></a>


Drivers that perform system or bus-master, packet-based DMA can use support routines designed especially for scatter/gather DMA. Instead of calling the sequence of routines outlined in [Using Packet-Based System DMA](using-packet-based-system-dma.md) and [Packet-Based Bus-Master DMA](using-packet-based-bus-master-dma.md), a driver can use [**GetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff546531) and [**PutScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff559967).

A device does not need to have built-in scatter/gather support for its driver to use these routines.

Drivers that use packet-based DMA call the following general sequence of support routines for scatter/gather operations:

1.  [**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539) to get an index into the MDL, required as a parameter in the call to **GetScatterGatherList**

2.  [**GetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff546531) when the driver is ready to program its device for DMA and needs the system DMA controller or bus-master adapter

    **GetScatterGatherList** allocates the system DMA controller or bus-master adapter, determines how many map registers are required and allocates them, fills in the scatter/gather list, and calls the driver's [*AdapterListControl*](https://msdn.microsoft.com/library/windows/hardware/ff540513) routine when the DMA controller or adapter and map registers are available.

3.  [**PutScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff559967) as soon as all the requested data has been transferred or the driver fails the IRP because of a device I/O error

    **PutScatterGatherList** flushes the adapter buffers, frees the map registers, and frees the scatter/gather list. The driver must call **PutScatterGatherList** before it can access the data in the buffer.

The adapter object pointer returned by **IoGetDmaAdapter** is a required parameter to each of these routines except **MmGetMdlVirtualAddress**, which requires a pointer to the MDL at *Irp*-&gt;**MdlAddress**.

The **GetScatterGatherList** routine includes calls to **AllocateAdapterChannel** and **MapTransfer**, so the driver does not have to make these calls. The routine takes the following as parameters:

-   A pointer to the [**DMA\_ADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff544062) structure returned by [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220)

-   A pointer to the target device object for the DMA operation

-   A pointer to the MDL that describes the buffer at *Irp*-&gt;**MdlAddress**

-   A pointer to the current virtual address in the buffer described by the Mdl

-   The number of bytes to be mapped

-   A pointer to an [*AdapterListControl*](https://msdn.microsoft.com/library/windows/hardware/ff540513) routine that performs the transfer

-   A pointer to a driver-defined context area to be passed to the *AdapterListControl* routine

-   A Boolean value: **TRUE** for a transfer to the device; **FALSE** otherwise

After determining the number of map registers required, allocating the adapter channel and map registers, filling in the scatter/gather list and preparing for the transfer, **GetScatterGatherList** calls the driver-supplied *AdapterListControl* routine. The *AdapterListControl* routine is run in an arbitrary thread context at IRQL = DISPATCH\_LEVEL.

The *AdapterListControl* routine a driver supplies in calls to **GetScatterGatherList** differs from the [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine passed to **AllocateAdapterChannel** in the following important respects:

-   The *AdapterListControl* routine has no return value, whereas the *AdapterControl* routine returns an [**IO\_ALLOCATION\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff550534).

-   Rather than a pointer to the *MapRegisterBase* for the system-allocated map registers, the third parameter to an *AdapterListControl* routine instead points to a [**SCATTER\_GATHER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff563664) structure through which the driver can perform DMA.

-   The *AdapterListControl* routine performs a subset of the tasks required in an *AdapterControl* routine.

    The *AdapterListControl* routine does not call **AllocateAdapterChannel** or **MapTransfer**. Its only responsibilities are to save the input scatter/gather list pointer, set up its device, and use the scatter/gather list to perform DMA.

The scatter/gather list structure includes a **SCATTER\_GATHER\_ELEMENT** array and the number of elements in the array. Each element of the array provides the length and starting physical address of a physically contiguous scatter/gather region. A driver uses the length and address in data transfers.

A driver can use **GetScatterGatherList** regardless of whether its device supports scatter/gather DMA. For a device that does not support scatter/gather DMA, the scatter/gather list will contain only one element.

Using the scatter/gather routines can improve performance over calling **AllocateAdapterChannel** (as previously described in [Using Packet-Based System DMA](using-packet-based-system-dma.md) and [Using Packet-Based Bus-Master DMA](using-packet-based-bus-master-dma.md)). Unlike calls to **AllocateAdapterChannel**, more than one call to **GetScatterGatherList** can be queued for a device object at any one time. A driver can call **GetScatterGatherList** again for another DMA operation on the same driver object before its *AdapterListControl* routine has completed execution.

On return from the driver-supplied *AdapterListControl* routine, **GetScatterGatherList** keeps the map registers but frees the DMA adapter structure.

When the driver has satisfied the current IRP's transfer request or must fail the IRP due to a device or bus I/O error, it must call **PutScatterGatherList** before it can access the transferred data in the buffer. **PutScatterGatherList** flushes the adapter buffers and frees the map registers and scatter/gather list.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20Scatter/Gather%20DMA%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


