---
title: Writing DPC Routines
description: Writing DPC Routines
keywords: ["deferred procedure calls WDK kernel", "DPCs WDK kernel", "DpcForIsr", "CustomDpc"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Writing DPC Routines





The primary responsibilities of [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) and [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routines are ensuring that the next device I/O operation is started promptly and completing the current IRP.

Additional work done by any *DpcForIsr* or *CustomDpc* routine depends on the driver's design and the nature of the device. For example, a *DpcForIsr* or *CustomDpc* routine also can do any of the following:

-   Retry an operation that has timed out or failed.

-   Call [**IoAllocateErrorLogEntry**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateerrorlogentry), set up an error log packet to report a device I/O error, and call [**IoWriteErrorLogEntry**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iowriteerrorlogentry).

    For more information about handling I/O errors, see [Logging Errors](logging-errors.md).

-   If the driver uses [buffered I/O](methods-for-accessing-data-buffers.md), or if the IRP specifies a device control operation, transfer data read in from the device to the system buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** before completing the IRP.

-   If the driver uses [direct I/O](methods-for-accessing-data-buffers.md) and must break large transfers into smaller pieces, save state about each just-completed partial-transfer operation, calculate the next partial-transfer range, and use a driver-supplied [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine to program the device for the next partial-transfer operation.

    Even a driver that uses buffered I/O might have to split up a transfer request if its device has limited transfer capabilities.

-   If the driver uses packet-based DMA, call [**FlushAdapterBuffers**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pflush_adapter_buffers) after each device transfer operation, and call [**FreeAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel) or [**FreeMapRegisters**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_map_registers) when a sequence of partial transfers is done and the full transfer request is satisfied.

    If a requested transfer is only partly satisfied by a single DMA operation, the *DpcForIsr* or *CustomDpc* routine is usually responsible for setting up one or more DMA operations until the IRP's specified number of bytes have been fully transferred.

    For more information about using DMA, see [Adapter Objects and DMA](./introduction-to-adapter-objects.md).

-   If the driver uses programmed I/O (PIO), call [**KeFlushIoBuffers**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keflushiobuffers) at the end of each transfer operation if the current IRP requests a read.

    If a requested transfer is only partly satisfied by a single PIO operation, the *DpcForIsr* or *CustomDpc* routine is usually responsible for setting up one or more transfer operations until the IRP's specified number of bytes have been fully transferred.

    For more information about using PIO, see [Using Direct I/O](using-direct-i-o.md).

-   If a non-WDM driver has a [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049) routine, call [**IoFreeController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iofreecontroller) when a requested operation is complete.

Note that a *DpcForIsr* or *CustomDpc* routine usually does most of the driver's device I/O processing to satisfy IRPs. These routines also share some of the responsibility for queuing IRPs to the device with the driver's dispatch routines.

Consider the following a general design guidelines.

-   Any *DpcForIsr* or *CustomDpc* routine should call [**IoStartNextPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartnextpacket) as soon as it can safely make this call: that is, without possibly causing a resource conflict or race condition with the driver's [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine or with any other routine the *StartIo* routine causes to run.

-   If a driver manages its own queuing of IRPs, its *DpcForIsr* or *CustomDpc* routine should notify the driver as soon as it is safe to dequeue the next IRP and to set up the device for the next request.

A *DpcForIsr* or *CustomDpc* routine must call **IoStartNextPacket**, or otherwise notify the appropriate driver routine when device I/O processing for the next request can be started. Depending on the driver and its device, this can occur well before the *DpcForIsr* or *CustomDpc* routine completes the current IRP with [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest), or it can occur immediately before this routine completes the current IRP and returns control.

 

