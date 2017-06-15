---
title: Writing DPC Routines
author: windows-driver-content
description: Writing DPC Routines
MS-HAID:
- 'Intrupts\_f8b8f4c3-71f1-41d5-8f03-dfde1c3aa336.xml'
- 'kernel.writing\_dpc\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: a0b93b71-7ee3-4626-b0b8-5dd6e19fba0d
keywords: ["deferred procedure calls WDK kernel", "DPCs WDK kernel", "DpcForIsr", "CustomDpc"]
---

# Writing DPC Routines


## <a href="" id="ddk-writing-dpc-routines-kg"></a>


The primary responsibilities of [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) and [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routines are ensuring that the next device I/O operation is started promptly and completing the current IRP.

Additional work done by any *DpcForIsr* or *CustomDpc* routine depends on the driver's design and the nature of the device. For example, a *DpcForIsr* or *CustomDpc* routine also can do any of the following:

-   Retry an operation that has timed out or failed.

-   Call [**IoAllocateErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff548245), set up an error log packet to report a device I/O error, and call [**IoWriteErrorLogEntry**](https://msdn.microsoft.com/library/windows/hardware/ff550527).

    For more information about handling I/O errors, see [Logging Errors](logging-errors.md).

-   If the driver uses [buffered I/O](methods-for-accessing-data-buffers.md), or if the IRP specifies a device control operation, transfer data read in from the device to the system buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** before completing the IRP.

-   If the driver uses [direct I/O](methods-for-accessing-data-buffers.md) and must break large transfers into smaller pieces, save state about each just-completed partial-transfer operation, calculate the next partial-transfer range, and use a driver-supplied [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine to program the device for the next partial-transfer operation.

    Even a driver that uses buffered I/O might have to split up a transfer request if its device has limited transfer capabilities.

-   If the driver uses packet-based DMA, call [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917) after each device transfer operation, and call [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507) or [**FreeMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff546513) when a sequence of partial transfers is done and the full transfer request is satisfied.

    If a requested transfer is only partly satisfied by a single DMA operation, the *DpcForIsr* or *CustomDpc* routine is usually responsible for setting up one or more DMA operations until the IRP's specified number of bytes have been fully transferred.

    For more information about using DMA, see [Adapter Objects and DMA](adapter-objects-and-dma.md).

-   If the driver uses programmed I/O (PIO), call [**KeFlushIoBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff552041) at the end of each transfer operation if the current IRP requests a read.

    If a requested transfer is only partly satisfied by a single PIO operation, the *DpcForIsr* or *CustomDpc* routine is usually responsible for setting up one or more transfer operations until the IRP's specified number of bytes have been fully transferred.

    For more information about using PIO, see [Using Direct I/O](using-direct-i-o.md).

-   If a non-WDM driver has a [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049) routine, call [**IoFreeController**](https://msdn.microsoft.com/library/windows/hardware/ff549104) when a requested operation is complete.

Note that a *DpcForIsr* or *CustomDpc* routine usually does most of the driver's device I/O processing to satisfy IRPs. These routines also share some of the responsibility for queuing IRPs to the device with the driver's dispatch routines.

Consider the following a general design guidelines.

-   Any *DpcForIsr* or *CustomDpc* routine should call [**IoStartNextPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550358) as soon as it can safely make this call: that is, without possibly causing a resource conflict or race condition with the driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine or with any other routine the *StartIo* routine causes to run.

-   If a driver manages its own queuing of IRPs, its *DpcForIsr* or *CustomDpc* routine should notify the driver as soon as it is safe to dequeue the next IRP and to set up the device for the next request.

A *DpcForIsr* or *CustomDpc* routine must call **IoStartNextPacket**, or otherwise notify the appropriate driver routine when device I/O processing for the next request can be started. Depending on the driver and its device, this can occur well before the *DpcForIsr* or *CustomDpc* routine completes the current IRP with [**IoCompleteRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548343), or it can occur immediately before this routine completes the current IRP and returns control.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20DPC%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


