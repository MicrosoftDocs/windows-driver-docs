---
title: Summary of Read/Write Dispatch Routines
description: Summary of Read/Write Dispatch Routines
keywords: ["DispatchRead routine", "DispatchWrite routine", "DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchWrite routine", "dispatch routines WDK kernel , DispatchRead routine", "read/write dispatch routines WDK kernel", "IRP_MJ_WRITE I/O function codes", "IRP_MJ_READ I/O function codes", "data transfers WDK kernel , read/write dispatch routines", "transferring data WDK kernel , read/write dispatch routines"]
ms.date: 06/16/2017
---

# Summary of Read/Write Dispatch Routines





Keep the following points in mind when implementing a [*DispatchRead*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch), [*DispatchWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch), or [*DispatchReadWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine:

-   It is the responsibility of the highest-level driver in a chain of layered drivers to check the parameters of incoming read/write IRPs for validity before setting up the next-lower-level driver's I/O stack location in an IRP.

-   Intermediate and lowest-level drivers generally can rely on the highest-level driver in their chain to pass down transfer requests with valid parameters. However, any driver can perform sanity checks on the parameters in its I/O stack location of an IRP, and each device driver should check the parameters for conditions that might violate any restrictions imposed by its device.

-   If a *DispatchReadWrite* routine completes an IRP with an error, it should set the I/O stack location **Status** member with an appropriate NTSTATUS-type value, set the **Information** member to zero, and call [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) with the IRP and a *PriorityBoost* of IO\_NO\_INCREMENT.

-   If a driver uses buffered I/O, it might need to define a structure to contain data to be transferred and might need to buffer some number of these structures internally.

-   If a driver uses direct I/O, it might need to check whether the MDL at **Irp-&gt;MdlAddress** describes a buffer containing too much data (or too many page breaks) for the underlying device to handle in a single transfer operation. If so, the driver must split up the original transfer request into a sequence of smaller transfer operations.

    A closely coupled class driver might split up such a request in its *DispatchReadWrite* routine for its underlying port driver. SCSI class drivers, particularly for mass-storage devices, are required to do this. For more information about requirements for SCSI drivers, see [Storage Drivers](../storage/storage-drivers.md).

-   A lower-level device driver's *DispatchReadWrite* routine should postpone splitting a large transfer request into partial transfers until another driver routine dequeues the IRP to set up the device for the transfer.

-   If a lower-level device driver queues a read/write IRP for further processing by its own routines, it must call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) before it queues the IRP. The *DispatchReadWrite* routine also must return control with STATUS\_PENDING in these circumstances.

-   If the *DispatchReadWrite* routine passes an IRP on to lower drivers, it must set up the I/O stack location for the next-lower driver in the IRP. Whether the higher-level driver also sets an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine in the IRP before passing it on with [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) depends on the design of the driver and of those layered under it.

    However, a higher-level driver must call [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) before it calls [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) if it allocates any resources, such as IRPs or memory. Its *IoCompletion* routine must free any driver-allocated resources when lower drivers have completed the request but before the *IoCompletion* routine calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) with the original IRP.

-   If a higher-level driver allocates IRPs for lower drivers that might include an underlying removable-media device driver, the allocating driver must establish the thread context in each IRP it allocates.

 

