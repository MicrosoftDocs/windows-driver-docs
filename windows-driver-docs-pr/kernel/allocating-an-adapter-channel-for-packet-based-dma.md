---
title: Allocating an Adapter Channel for Packet-Based DMA
description: Allocating an Adapter Channel for Packet-Based DMA
ms.assetid: c95e4b2d-ce19-453a-bcc5-4bb37fc5d9ed
keywords: ["system DMA WDK kernel , packet-based", "packet-based DMA WDK kernel", "DMA transfers WDK kernel , packet-based", "allocating adapter channels", "adapter channel allocations WDK kernel", "AllocateAdapterChannel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Allocating an Adapter Channel for Packet-Based DMA





To prepare for packet-based system DMA, a driver calls [**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041) and [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573) after receiving an [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) or [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) request.

Before the driver calls these routines, its [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376) or [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034) routine (or any other dispatch routine that handles a DMA transfer) should already have checked the validity of the IRP's parameters. The dispatch routine might also have queued the IRP to another driver routine for further processing.

The driver routine that calls **AllocateAdapterChannel** must be executing at IRQL = DISPATCH\_LEVEL. Along with a pointer to the adapter object returned by [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220), a driver must supply the following when it calls **AllocateAdapterChannel**:

-   A pointer to the target device object

-   The entry point for its [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine

-   A pointer to any driver-determined context information the *AdapterControl* routine will use

**AllocateAdapterChannel** queues the driver's *AdapterControl* routine, which runs when the system DMA controller is assigned to this driver and a set of [map registers](map-registers.md) has been allocated for the driver's DMA operation(s).

On entry, the *AdapterControl* routine receives the *DeviceObject* and *Context* pointers passed in the call to **AllocateAdapterChannel**, as well as a handle (*MapRegisterBase*) for the allocated map registers.

The *AdapterControl* routine also receives a pointer to the **DeviceObject-&gt;CurrentIrp** if the driver has a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine. If the driver manages its own queuing of IRPs (instead of having a *StartIo* routine), the driver should include a pointer to the current IRP as part of the context it passes when it calls **AllocateAdapterChannel**.

The *AdapterControl* routine typically does the following:

1.  Saves or initializes whatever context the driver maintains about DMA operations. The context might include the input *MapRegisterBase* handle the driver must pass to [**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402) and [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917) and, possibly, the **Length** of the requested transfer from its I/O stack location in the IRP.

2.  Calls [**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539) followed by **MapTransfer**. See [Setting Up the System DMA Controller for Packet-Based DMA](setting-up-the-system-dma-controller-for-packet-based-dma.md).

3.  Sets up the subordinate device to start the transfer operation.

4.  Returns the value **KeepObject**.

Every *AdapterControl* routine must return a system-defined value of type [**IO\_ALLOCATION\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff550534). For drivers that use system DMA, the *AdapterControl* routine must return the value **KeepObject**. This allows the driver to retain "ownership" of the system DMA controller and allocated map registers until it has transferred all the requested data.

Because an *AdapterControl* routine cannot wait for the subordinate device to carry out the DMA operation, each *AdapterControl* routine must, at a minimum, do the following:

1.  Save context information, particularly the *MapRegisterBase* handle, in the driver's device extension, controller extension, or other driver-accessible resident storage area (nonpaged pool allocated by the driver).

2.  Return **KeepObject**.

For additional information, see [Writing AdapterControl Routines](writing-adaptercontrol-routines.md).

Another driver routine (probably the [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine) must call [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917) when each DMA transfer operation is complete. This routine also must call **MapTransfer** and **FlushAdapterBuffers** again if it is necessary to set up the DMA controller more than once to satisfy the current IRP's transfer request.

When a driver has satisfied the current IRP's request, it must call [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507). This support routine should be called immediately following the last call to **FlushAdapterBuffers** for the current IRP so that the system DMA controller can be made available for use (by any driver) to satisfy other transfer requests expeditiously.

The driver of a subordinate device with scatter/gather capabilities should also return **KeepObject** from its *AdapterControl* routine. The device must be capable of waiting while the system DMA controller is reprogrammed between DMA operations when the driver must split up a given DMA request. On some Windows platforms, such devices can transfer at most a page of data per DMA operation because the HAL can assign only a single map register to the driver of that device.

 

 




