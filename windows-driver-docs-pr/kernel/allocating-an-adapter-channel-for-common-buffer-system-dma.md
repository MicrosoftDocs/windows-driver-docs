---
title: Allocating an Adapter Channel for Common-Buffer System DMA
description: Allocating an Adapter Channel for Common-Buffer System DMA
ms.assetid: 3b426b5e-e555-458c-8e16-0d59a7cb9bd6
keywords: ["allocating adapter channels", "adapter channel allocations WDK kernel", "AllocateAdapterChannel", "system DMA WDK kernel , common buffer", "common buffer DMA WDK kernel", "DMA transfers WDK kernel , common buffer"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Allocating an Adapter Channel for Common-Buffer System DMA





A driver calls [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573) after its [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376) or [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034) routine (or any other dispatch routine that handles a DMA transfer) has checked the validity of the IRP's parameters, possibly queued one or more IRPs to another driver routine for further processing, and possibly loaded its common buffer with data to be transferred, if appropriate.

The driver routine that calls **AllocateAdapterChannel** must be executing at IRQL = DISPATCH\_LEVEL. The **AllocateAdapterChannel** routine queues the driver's [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine, which runs after the system DMA controller has been assigned to this driver and a set of [map registers](map-registers.md) has been allocated for the driver's DMA operation.

On entry, the *AdapterControl* routine is given pointers to the device object and context passed in the call to **AllocateAdapterChannel**, as well as a handle for the allocated map registers. The *AdapterControl* routine also is given a pointer to the **DeviceObject-&gt;CurrentIrp** if the driver has a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine. If the driver manages its own queuing of IRPs instead of having a *StartIo* routine, the driver should include a pointer to the current IRP as part of the context data it passes when it calls **AllocateAdapterChannel**.

The *AdapterControl* routine typically does the following:

1.  Saves or initializes whatever context the driver maintains about DMA operations. The context might include the input *MapRegisterBase* handle the driver must pass to [**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402) and [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917) and, possibly, the **Length** of the requested transfer from its I/O stack location in the IRP.

2.  Sets up the subordinate device to start the transfer operation.

3.  Returns the value **KeepObject**.

For additional information, see [Writing AdapterControl Routines](writing-adaptercontrol-routines.md).

For drivers that use a system DMA controller's auto-initialize mode, the *AdapterControl* routine must return the value **KeepObject**. This allows the driver to retain "ownership" of the system DMA controller and allocated map register(s) until it has transferred all the data.

Because an *AdapterControl* routine cannot wait for the subordinate device to carry out the DMA operation, the *AdapterControl* routine must at least do the following:

1.  Save context information, particularly the *MapRegisterBase* handle, in the driver's device extension, controller extension, or other driver-accessible resident storage area (nonpaged pool allocated by the driver).

2.  Return **KeepObject**.

Another driver routine (probably the [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) routine) must call [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917) and [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507) when the DMA transfer operation is complete.

 

 




