---
title: Allocating an Adapter Channel for Packet-Based DMA
description: Allocating an Adapter Channel for Packet-Based DMA
keywords: ["system DMA WDK kernel , packet-based", "packet-based DMA WDK kernel", "DMA transfers WDK kernel , packet-based", "allocating adapter channels", "adapter channel allocations WDK kernel", "AllocateAdapterChannel"]
ms.date: 07/18/2025
ms.topic: how-to
---

# Allocating an Adapter Channel for Packet-Based DMA

To prepare for packet-based system DMA, a driver calls [**KeFlushIoBuffers**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keflushiobuffers) and [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel) after receiving an [**IRP_MJ_READ**](./irp-mj-read.md) or [**IRP_MJ_WRITE**](./irp-mj-write.md) request.

Before the driver calls these routines, its [*DispatchRead*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) or [*DispatchWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine (or any other dispatch routine that handles a DMA transfer) should already check the validity of the IRP's parameters. The dispatch routine might also queue the IRP to another driver routine for further processing.

The driver routine that calls **AllocateAdapterChannel** must run at IRQL = DISPATCH_LEVEL. Along with a pointer to the adapter object returned by [**IoGetDmaAdapter**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdmaadapter), a driver supplies the following information when it calls **AllocateAdapterChannel**:

- A pointer to the target device object

- The entry point for its [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine

- A pointer to any driver-determined context information the *AdapterControl* routine uses

**AllocateAdapterChannel** queues the driver's *AdapterControl* routine. The system runs this routine when it assigns the system DMA controller to this driver and allocates a set of [map registers](map-registers.md) for the driver's DMA operations.

On entry, the *AdapterControl* routine receives the *DeviceObject* and *Context* pointers passed in the call to **AllocateAdapterChannel**, as well as a handle (*MapRegisterBase*) for the allocated map registers.

The *AdapterControl* routine also receives a pointer to the **DeviceObject-&gt;CurrentIrp** if the driver has a [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine. If the driver manages its own queuing of IRPs (instead of having a *StartIo* routine), the driver should include a pointer to the current IRP as part of the context it passes when it calls **AllocateAdapterChannel**.

The *AdapterControl* routine typically does the following steps:

1. Saves or initializes whatever context the driver maintains about DMA operations. The context might include the input *MapRegisterBase* handle the driver must pass to [**MapTransfer**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pmap_transfer) and [**FlushAdapterBuffers**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pflush_adapter_buffers) and, possibly, the **Length** of the requested transfer from its I/O stack location in the IRP.

1. Calls [**MmGetMdlVirtualAddress**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetmdlvirtualaddress) followed by **MapTransfer**. For more information, see [Setting Up the System DMA Controller for Packet-Based DMA](setting-up-the-system-dma-controller-for-packet-based-dma.md).

1. Sets up the subordinate device to start the transfer operation.

1. Returns the value **KeepObject**.

Every *AdapterControl* routine must return a system-defined value of type [**IO_ALLOCATION_ACTION**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_io_allocation_action). For drivers that use system DMA, the *AdapterControl* routine must return the value **KeepObject**. This value lets the driver keep "ownership" of the system DMA controller and allocated map registers until it transfers all the requested data.

Because an *AdapterControl* routine can't wait for the subordinate device to carry out the DMA operation, each *AdapterControl* routine must, at a minimum, do the following steps:

1. Save context information, particularly the *MapRegisterBase* handle, in the driver's device extension, controller extension, or other driver-accessible resident storage area (nonpaged pool allocated by the driver).

1. Return **KeepObject**.

For additional information, see [Writing AdapterControl Routines](writing-adaptercontrol-routines.md).

Another driver routine (probably the [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) routine) must call [**FlushAdapterBuffers**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pflush_adapter_buffers) when each DMA transfer operation completes. This routine also must call **MapTransfer** and **FlushAdapterBuffers** again if it's necessary to set up the DMA controller more than once to satisfy the current IRP's transfer request.

When a driver satisfies the current IRP's request, it must call [**FreeAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel). The driver should call this support routine immediately following the last call to **FlushAdapterBuffers** for the current IRP. This call makes the system DMA controller available for use by any driver to satisfy other transfer requests as quickly as possible.

The driver of a subordinate device with scatter/gather capabilities should also return **KeepObject** from its *AdapterControl* routine. The device must be capable of waiting while the system DMA controller is reprogrammed between DMA operations when the driver splits up a given DMA request. On some Windows platforms, such devices can transfer at most a page of data per DMA operation because the HAL can assign only a single map register to the driver of that device.
