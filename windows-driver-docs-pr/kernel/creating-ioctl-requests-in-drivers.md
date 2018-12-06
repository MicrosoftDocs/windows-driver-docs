---
title: Creating IOCTL Requests in Drivers
description: Creating IOCTL Requests in Drivers
ms.assetid: 155e2577-0e9a-4c0b-a25a-8516ce3de631
keywords: ["I/O control codes WDK kernel , creating requests", "control codes WDK IOCTLs , creating requests", "IOCTLs WDK kernel , creating requests", "synchronization WDK IRPs", "embedded pointers WDK IOCTLs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Creating IOCTL Requests in Drivers





A class driver or other higher-level driver can allocate IRPs for I/O control requests and send them to the next-lower driver as follows:

1.  Allocate or reuse an I/O request packet ([**IRP**](https://msdn.microsoft.com/library/windows/hardware/ff550694)) with the major function code [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) or [**IRP\_MJ\_INTERNAL\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550766). You can use the [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) routine to specifically allocate an IOCTL IRP. You can also use general-purpose IRP creation and initialization routines, such as [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257), [**IoReuseIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549661), or [**IoInitializeIrp**](https://msdn.microsoft.com/library/windows/hardware/ff549315). For more information about IRP allocation, see [Creating IRPs for Lower-Level Drivers](creating-irps-for-lower-level-drivers.md).

2.  Set up the lower driver's I/O stack location for the IRP with the IOCTL\_*XXX* code and appropriate parameters.

3.  If the IOCTL request is to be completed asynchronously, call the [**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137) routine to initialize an event object as a notification event. The driver uses this event to wait for an I/O operation to be completed.

4.  Call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679) with the IRP so that the upper driver can supply an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine, if necessary, to do the following:

    -   Determine how the lower driver handled a given request.

    -   Reuse the IRP to send another request or dispose of the driver-created IRP, after the lower driver completes a requested operation. The driver cannot reuse IRPs that [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) created. For more information, see [Reusing IRPs](reusing-irps.md).

5.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) to pass the request on to the lower driver.

6.  If [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) returns STATUS\_PENDING, call the [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) routine to put the current thread into a wait state. The driver sets the routine's *Object* parameter to the address of the event object that was initialized in the call to [**KeInitializeEvent**](https://msdn.microsoft.com/library/windows/hardware/ff552137).

    **Note**  If the driver calls [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) with its *Timeout* parameter set either to **NULL** or to the address of a variable that contains a nonzero value, the driver must be running at IRQL &lt;= APC\_LEVEL in a nonarbitrary thread context. Otherwise, the driver must be running at IRQL &lt;= DISPATCH\_LEVEL.




The event is signaled by its [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine when the IOCTL request has completed. Once the event is signaled, the thread resumes execution.

**Important**  If the driver allocates the event object as a local variable on the stack, the driver must call [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) with its *WaitMode* parameter set to **KernelMode**. This parameter value prevents the stack from being paged out.




To avoid synchronization problems and possible access violations, parameters for I/O control codes rarely include embedded pointers. Except for certain SCSI requests, the buffers at *Irp*-&gt;**AssociatedIrp**.**SystemBuffer**, at *Irp*-&gt;**MdlAddress**, and at **Parameters**.**DeviceIoControl**.**Type3InputBuffer** in a driver's I/O stack location do not contain pointers to other data buffers, nor do they contain structures that contain pointers for system-defined I/O control codes. For more information about how data buffers are used with IRPs that contain I/O control codes, see [Buffer Descriptions for I/O Control Codes](buffer-descriptions-for-i-o-control-codes.md).

Nevertheless, a pair of class/port drivers that define internal I/O control codes can pass an embedded pointer to driver-allocated memory from the higher-level driver to the lower-level driver. Such a pair of class/port drivers is responsible for ensuring that the following is true:

-   Only one driver at a time can access the data.

-   Private data buffers are accessible in an arbitrary thread context by the port driver.

Display drivers can call the GDI function [**EngDeviceIoControl**](https://msdn.microsoft.com/library/windows/hardware/ff564838) to send privately defined, device-specific I/O control requests, as well as system-defined public I/O control requests, through the system video port driver down to the corresponding adapter-specific [video miniport drivers](https://msdn.microsoft.com/library/windows/hardware/ff570509).

Any user-mode component of a driver package can call [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) to send I/O control requests to a driver stack. The I/O manager creates an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request and delivers it to the highest-level driver.








