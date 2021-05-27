---
title: Passing IRPs down the Driver Stack
description: Passing IRPs down the Driver Stack
keywords: ["IRPs WDK kernel , passing down stack", "passing IRPs down driver stack WDK", "transferring IRPs down driver stack", "I/O stack locations WDK kernel", "stack locations WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Passing IRPs down the Driver Stack





When a driver's dispatch routine receives an IRP, it must call [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) so that it can check its own I/O stack location and determine that any parameters are valid. If the driver cannot satisfy and complete the request itself, it can do one of the following:

-   Pass the IRP on for further processing by lower-level drivers.

-   Create one or more new IRPs and pass them down to lower-level drivers.

### A higher-level driver should pass an I/O request on to a next-lower driver as follows:

1.  If the driver will pass the input IRP on to the next lower-level driver, the dispatch routine should call [**IoSkipCurrentIrpStackLocation**](./mm-bad-pointer.md) or [**IoCopyCurrentIrpStackLocationToNext**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocopycurrentirpstacklocationtonext) to set up the I/O stack location of the next-lower driver.

    If the driver calls [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp) to allocate one or more additional IRPs for lower drivers, the dispatch routine must initialize the next-lower driver's I/O stack location by following the steps that are described in [Processing IRPs in an Intermediate-Level Driver](processing-irps-in-an-intermediate-level-driver.md).

    The dispatch routine can modify some of the parameters in the next-lower driver's I/O stack location for certain requests. For example, a higher-level driver might modify the parameters for a large transfer request when the underlying device has a known limit in transfer capacity, and reuse the IRP to send partial-transfer requests to the underlying device driver.

2.  Call [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine).

    If the dispatch routine is passing a received IRP to the next-lower driver, setting an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine is optional but useful, because the routine can perform such tasks as determining how lower drivers completed the request, reusing the IRP for partial transfers, updating whatever state the driver maintains if it tracks IRPs, and retrying a request that was returned with an error.

    If the dispatch routine has allocated new IRPs, setting an *IoCompletion* routine is required because the routine must release each IRP after lower drivers have completed it.

    For more information about *IoCompletion* routines, see [Completing IRPs](completing-irps.md).

3.  Call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) with each IRP to be processed by lower drivers.

4.  Return an appropriate NTSTATUS value, such as:
    -   STATUS\_PENDING

        The driver usually returns STATUS\_PENDING if the input IRP is an asynchronous request, such as [**IRP\_MJ\_READ**](./irp-mj-read.md) or [**IRP\_MJ\_WRITE**](./irp-mj-write.md).

    -   The result of the call to **IoCallDriver**

        The driver frequently returns the result of the call to **IoCallDriver** if the input IRP is a synchronous request, such as [**IRP\_MJ\_CREATE**](./irp-mj-create.md).

### A lowest-level device driver passes any IRP that it cannot complete in its dispatch routine on to other driver routines as follows:

1.  Call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) with the input IRP.

2.  Call [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket) to pass on or queue the IRP to the driver's [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine, unless the driver manages its own internal IRP queuing, as described in [Driver-Managed IRP Queues](driver-managed-irp-queues.md).

    If the driver does not have a *StartIo* routine but handles cancelable IRPs, it must either register a [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine or implement a [cancel-safe IRP queue](cancel-safe-irp-queues.md). For more information about *Cancel* routines, see [Canceling IRPs](canceling-irps.md).

3.  Return STATUS\_PENDING.

 

