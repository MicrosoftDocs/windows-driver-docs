---
title: Allocating the Bus-Master Adapter Object
description: Allocating the Bus-Master Adapter Object
ms.assetid: fc80d3f8-a12e-40bd-8b0e-c6bca2f9e7de
keywords: ["allocating bus-master adapter objects", "bus-master DMA WDK kernel", "DMA transfers WDK kernel , bus-master DMA", "adapter objects WDK kernel , bus-master DMA"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Allocating the Bus-Master Adapter Object





To prepare for packet-based, bus-master DMA, a driver calls [**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041) and [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573) after receiving an [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) or [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819). Before the driver calls these routines, its dispatch routine should check the validity of the IRP's parameters. It might also queue the IRP to another driver routine for further processing. The transfer request is the current IRP requiring a device I/O operation.

The driver routine that calls **AllocateAdapterChannel** must be executing at IRQL = DISPATCH\_LEVEL. Along with a pointer to the adapter object returned by [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220), a driver must supply the following when it calls **AllocateAdapterChannel**:

-   A pointer to the target device object for the current IRP

-   The entry point for its [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine

-   A pointer to any driver-determined context information the *AdapterControl* routine will use

**AllocateAdapterChannel** queues the driver's *AdapterControl* routine, which runs when the adapter object is free and a set of [map registers](map-registers.md) has been allocated for the driver's DMA operations to or from the target device.

On entry, an *AdapterControl* routine is given the *DeviceObject* and *Context* pointers passed in the call to **AllocateAdapterChannel**, as well as a handle (*MapRegisterBase*) for the allocated map registers.

The *AdapterControl* routine also is given a pointer to the **DeviceObject-&gt;CurrentIrp** if the driver has a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine. If the driver manages its own queuing of IRPs instead of having a *StartIo* routine, the driver should include a pointer to the current IRP as part of the context it passes when it calls **AllocateAdapterChannel**.

For the driver of a bus-master DMA device without scatter/gather capabilities, the *AdapterControl* routine usually does the following:

1.  Saves or initializes whatever context the driver maintains about DMA operations. The context might include the input *MapRegisterBase* handle the driver must pass to [**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402) and [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917), the **Length** in bytes of the requested transfer from its I/O stack location in the IRP, and so forth.

2.  Calls [**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539) followed by **MapTransfer** (described in [Setting Up a Transfer Operation](setting-up-a-transfer-operation.md), next) to get the logical address its device can use to start the transfer operation.

3.  Sets up the bus-master adapter to start the transfer operation.

4.  Returns the value **DeallocateObjectKeepRegisters**.

For the driver of a bus-master device with scatter/gather capabilities, the *AdapterControl* routine usually does the following:

1.  Saves or initializes whatever state the driver maintains about DMA operations, such as saving the *MapRegisterBase* handle the driver must pass to **MapTransfer** and **FlushAdapterBuffers**, the **Length** in bytes of the requested transfer from its I/O stack location in the IRP, and so forth.

2.  Calls **MmGetMdlVirtualAddress** followed by **MapTransfer** (described in the next subsection) to get the logical address its device can use to start the transfer operation.

    The *AdapterControl* routine calls MapTransfer repeatedly until it has used all the available map registers to build a scatter/gather list for the bus-master adapter.

3.  Sets up the bus-master adapter to start the transfer operation.

4.  Returns the value **DeallocateObjectKeepRegisters**.

For additional information, see [Writing AdapterControl Routines](writing-adaptercontrol-routines.md).

Note that drivers that perform bus-master DMA can use the [**GetScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff546531) and [**PutScatterGatherList**](https://msdn.microsoft.com/library/windows/hardware/ff559967) routines regardless of whether their devices support scatter/gather DMA. Using these routines changes the requirements for the driver's *AdapterControl* routine; see [Using Scatter/Gather DMA](using-scatter-gather-dma.md) for details.

An *AdapterControl* routine must return a system-defined value of type IO\_ALLOCATION\_ACTION. For drivers that use bus-master DMA, the *AdapterControl* routine should typically return the value **DeallocateObjectKeepRegisters**, which allows the driver to retain the allocated map registers for the target device object until it has transferred all the requested data for the current IRP. After the transfer is complete, the DPC routine should call [**FreeMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff546513) to free the allocated map registers. In cases where the device does not support command queuing, however, the *AdapterControl* routine can return **KeepObject** when the transfer for the current IRP is complete, and the DPC routine can call [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507) instead.

An *AdapterControl* routine cannot wait for the bus-master adapter to complete a DMA operation.

Regardless of whether the bus-master adapter supports scatter/gather, the *AdapterControl* routine must at least do the following:

1.  Save necessary context information—particularly the *MapRegisterBase* handle—in the driver's device extension, controller extension, or other driver-accessible resident storage area (nonpaged pool, allocated by the driver). The driver must pass this handle when it calls **MapTransfer** and **FlushAdapterBuffers**.

2.  Return **DeallocateObjectKeepRegisters**.

Another driver routine (probably the [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine) must call **FlushAdapterBuffers** when each DMA transfer operation is done. This routine also must set up any additional DMA operations necessary to satisfy the current IRP.

When the driver has satisfied the current IRP's transfer request or must fail the IRP due to a device or bus I/O error, it must call **FreeMapRegisters**. This call should occur immediately following the last call to **FlushAdapterBuffers** for the current IRP, so that the driver can service other DMA requests, possibly for other devices on the bus.

 

 




