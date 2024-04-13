---
title: Creating IRPs for Lower-Level Drivers
description: Creating IRPs for Lower-Level Drivers
keywords: ["IRPs WDK kernel , creating", "asynchronous requests WDK IRPs", "IRPs WDK kernel , asynchronous requests"]
ms.date: 06/16/2017
---

# Creating IRPs for Lower-Level Drivers





To allocate an IRP for an asynchronous request, which will be processed in an arbitrary thread context by lower drivers, a [*DispatchReadWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine can call one of the following support routines:

-   [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp), which allocates an IRP and a number of zero-initialized I/O stack locations

    The dispatch routine must set up the next-lower driver's I/O stack location for the newly allocated IRP, usually by copying (possibly modified) information from its own stack location in the original IRP. If a higher-level driver allocates an I/O stack location of its own for a newly-allocated IRP, the dispatch routine can set up per-request context information there for the [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine to use.

-   [**IoBuildAsynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildasynchronousfsdrequest), which sets up the next-lower driver's I/O stack location for the caller, according to caller-specified parameters

    Higher-level drivers can call this routine to allocate IRPs for [**IRP\_MJ\_READ**](./irp-mj-read.md), [**IRP\_MJ\_WRITE**](./irp-mj-write.md), [**IRP\_MJ\_FLUSH\_BUFFERS**](./irp-mj-flush-buffers.md), and [**IRP\_MJ\_SHUTDOWN**](./irp-mj-shutdown.md) requests.

    When an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine is called for such an IRP, it can check the I/O status block, and if necessary (or possible) set up the next-lower driver's I/O stack location in the IRP again and retry the request or reuse it. However, the *IoCompletion* routine has no local context storage for itself in the IRP, so the driver must maintain context about the original request elsewhere in resident memory.

-   [**IoMakeAssociatedIrp**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iomakeassociatedirp), which allocates an IRP and a number of zero-initialized I/O stack locations, and associates the IRP with a *master* IRP.

    Intermediate drivers cannot call [**IoMakeAssociatedIrp**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iomakeassociatedirp) to create IRPs for lower drivers.

    Any highest-level driver that calls **IoMakeAssociatedIrp** to create IRPs for lower drivers can return control to the I/O manager after sending its associated IRPs on and calling [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) for the original, master IRP. A highest-level driver can rely on the I/O manager to complete the master IRP when all associated IRPs have been completed by lower drivers.

    Drivers seldom set an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine for an associated IRP. If a highest-level driver calls [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) for an associated IRP it creates, the I/O manager does not complete the master IRP if the driver returns STATUS\_MORE\_PROCESSING\_REQUIRED from its *IoCompletion* routine. In these circumstances, the driver's *IoCompletion* routine must explicitly complete the master IRP with [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest).

If a driver allocates an I/O stack location of its own in a new IRP, the dispatch routine must call [**IoSetNextIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetnextirpstacklocation) before it calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) to set up context in its own I/O stack location for the [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine. For more information, see [Processing IRPs in an Intermediate-Level Driver](processing-irps-in-an-intermediate-level-driver.md).

The dispatch routine must call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) with the original IRP, but not with any driver-allocated IRPs because the [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine will free them.

If the dispatch routine is allocating IRPs for partial transfers and the underlying device driver might control a removable-media device, the dispatch routine must set up the thread context in its newly allocated IRPs from the value at **Tail.Overlay.Thread** in the original IRP.

An underlying driver for a removable-media device might call [**IoSetHardErrorOrVerifyDevice**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iosetharderrororverifydevice), which references the pointer at **Irp-&gt;Tail.Overlay.Thread**, for a driver-allocated IRP. If the driver calls this support routine, the file system driver can send a dialog box to the appropriate user thread that prompts the user to cancel, retry, or fail an operation that the driver could not satisfy. See [Supporting Removable Media](supporting-removable-media.md) for more information.

Dispatch routines must return STATUS\_PENDING after sending all driver-allocated IRPs on to lower drivers.

A driver's [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine should free all driver-allocated IRPs with [**IoFreeIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iofreeirp) before it calls [**IoCompleteRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocompleterequest) for the original IRP. When it completes the original IRP, the *IoCompletion* routine must free all driver-allocated IRPs before it returns control.

Each higher-level driver sets up any driver-allocated (and reused) IRPs for lower drivers in such a way that it is immaterial to the underlying device driver whether a given request comes from an intermediate driver or originates from any other source, such as a file system or user-mode application.

Highest-level drivers can call [**IoMakeAssociatedIrp**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iomakeassociatedirp) to allocate IRPs and set them up for a chain of lower drivers. The I/O manager automatically completes the original IRP when all its associated IRPs have been completed, as long as the driver does not call [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) with the original IRP or with any of the associated IRPs it allocates. Highest-level drivers must not, however, allocate associated IRPs for any IRP that requests a buffered I/O operation.

An intermediate-level driver cannot allocate IRPs for lower-level drivers by calling **IoMakeAssociatedIrp**. Any IRP an intermediate driver receives might already be an associated IRP, and a driver cannot associate another IRP with such an IRP.

Instead, if an intermediate driver creates IRPs for lower drivers, it should call [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp), [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest), [**IoBuildSynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildsynchronousfsdrequest), or [**IoBuildAsynchronousFsdRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuildasynchronousfsdrequest). However, **IoBuildSynchronousFsdRequest** can be called only in the following circumstances:

-   By a driver-created thread to build IRPs for read or write requests, because such a thread can wait in a nonarbitrary thread context (its own) on a dispatcher object, such as a driver-initialized *Event* passed to **IoBuildSynchronousFsdRequest**

-   In the system thread context during initialization or while unloading

-   To build IRPs for inherently synchronous operations, such as create, flush, shutdown, close, and device control requests

However, a driver is more likely to call **IoBuildDeviceIoControlRequest** to allocate device control IRPs than **IoBuildSynchronousFsdRequest**.

 

