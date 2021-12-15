---
title: Creating IOCTL Requests in Drivers
description: Creating IOCTL Requests in Drivers
keywords: ["I/O control codes WDK kernel , creating requests", "control codes WDK IOCTLs , creating requests", "IOCTLs WDK kernel , creating requests", "synchronization WDK IRPs", "embedded pointers WDK IOCTLs"]
ms.date: 06/16/2017
---

# Creating IOCTL Requests in Drivers





A class driver or other higher-level driver can allocate IRPs for I/O control requests and send them to the next-lower driver as follows:

1.  Allocate or reuse an I/O request packet ([**IRP**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_irp)) with the major function code [**IRP\_MJ\_DEVICE\_CONTROL**](./irp-mj-device-control.md) or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](./irp-mj-internal-device-control.md). You can use the [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest) routine to specifically allocate an IOCTL IRP. You can also use general-purpose IRP creation and initialization routines, such as [**IoAllocateIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocateirp), [**IoReuseIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreuseirp), or [**IoInitializeIrp**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializeirp). For more information about IRP allocation, see [Creating IRPs for Lower-Level Drivers](creating-irps-for-lower-level-drivers.md).

2.  Set up the lower driver's I/O stack location for the IRP with the IOCTL\_*XXX* code and appropriate parameters.

3.  If the IOCTL request is to be completed asynchronously, call the [**KeInitializeEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializeevent) routine to initialize an event object as a notification event. The driver uses this event to wait for an I/O operation to be completed.

4.  Call [**IoSetCompletionRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcompletionroutine) with the IRP so that the upper driver can supply an [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine, if necessary, to do the following:

    -   Determine how the lower driver handled a given request.

    -   Reuse the IRP to send another request or dispose of the driver-created IRP, after the lower driver completes a requested operation. The driver cannot reuse IRPs that [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest) created. For more information, see [Reusing IRPs](reusing-irps.md).

5.  Call [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to pass the request on to the lower driver.

6.  If [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) returns STATUS\_PENDING, call the [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject) routine to put the current thread into a wait state. The driver sets the routine's *Object* parameter to the address of the event object that was initialized in the call to [**KeInitializeEvent**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keinitializeevent).

    **Note**  If the driver calls [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject) with its *Timeout* parameter set either to **NULL** or to the address of a variable that contains a nonzero value, the driver must be running at IRQL &lt;= APC\_LEVEL in a nonarbitrary thread context. Otherwise, the driver must be running at IRQL &lt;= DISPATCH\_LEVEL.




The event is signaled by its [*IoCompletion*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_completion_routine) routine when the IOCTL request has completed. Once the event is signaled, the thread resumes execution.

**Important**  If the driver allocates the event object as a local variable on the stack, the driver must call [**KeWaitForSingleObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kewaitforsingleobject) with its *WaitMode* parameter set to **KernelMode**. This parameter value prevents the stack from being paged out.




To avoid synchronization problems and possible access violations, parameters for I/O control codes rarely include embedded pointers. Except for certain SCSI requests, the buffers at *Irp*-&gt;**AssociatedIrp**.**SystemBuffer**, at *Irp*-&gt;**MdlAddress**, and at **Parameters**.**DeviceIoControl**.**Type3InputBuffer** in a driver's I/O stack location do not contain pointers to other data buffers, nor do they contain structures that contain pointers for system-defined I/O control codes. For more information about how data buffers are used with IRPs that contain I/O control codes, see [Buffer Descriptions for I/O Control Codes](buffer-descriptions-for-i-o-control-codes.md).

Nevertheless, a pair of class/port drivers that define internal I/O control codes can pass an embedded pointer to driver-allocated memory from the higher-level driver to the lower-level driver. Such a pair of class/port drivers is responsible for ensuring that the following is true:

-   Only one driver at a time can access the data.

-   Private data buffers are accessible in an arbitrary thread context by the port driver.

Display drivers can call the GDI function [**EngDeviceIoControl**](/windows/win32/api/winddi/nf-winddi-engdeviceiocontrol) to send privately defined, device-specific I/O control requests, as well as system-defined public I/O control requests, through the system video port driver down to the corresponding adapter-specific [video miniport drivers](../display/video-miniport-drivers-in-the-windows-2000-display-driver-model.md).

Any user-mode component of a driver package can call [**DeviceIoControl**](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) to send I/O control requests to a driver stack. The I/O manager creates an [**IRP\_MJ\_DEVICE\_CONTROL**](./irp-mj-device-control.md) request and delivers it to the highest-level driver.
