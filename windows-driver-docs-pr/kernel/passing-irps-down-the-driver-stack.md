---
title: Passing IRPs down the Driver Stack
author: windows-driver-content
description: Passing IRPs down the Driver Stack
MS-HAID:
- 'IRPs\_1d986947-a261-4f64-afb9-169c63c1f7f9.xml'
- 'kernel.passing\_irps\_down\_the\_driver\_stack'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 69d912c5-83cf-4651-b379-de6baea8ddd0
keywords: ["IRPs WDK kernel , passing down stack", "passing IRPs down driver stack WDK", "transferring IRPs down driver stack", "I/O stack locations WDK kernel", "stack locations WDK kernel"]
---

# Passing IRPs down the Driver Stack


## <a href="" id="ddk-passing-irps-down-the-driver-stack-kg"></a>


When a driver's dispatch routine receives an IRP, it must call [**IoGetCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff549174) so that it can check its own I/O stack location and determine that any parameters are valid. If the driver cannot satisfy and complete the request itself, it can do one of the following:

-   Pass the IRP on for further processing by lower-level drivers.

-   Create one or more new IRPs and pass them down to lower-level drivers.

### A higher-level driver should pass an I/O request on to a next-lower driver as follows:

1.  If the driver will pass the input IRP on to the next lower-level driver, the dispatch routine should call [**IoSkipCurrentIrpStackLocation**](https://msdn.microsoft.com/library/windows/hardware/ff550355) or [**IoCopyCurrentIrpStackLocationToNext**](https://msdn.microsoft.com/library/windows/hardware/ff548387) to set up the I/O stack location of the next-lower driver.

    If the driver calls [**IoAllocateIrp**](https://msdn.microsoft.com/library/windows/hardware/ff548257) to allocate one or more additional IRPs for lower drivers, the dispatch routine must initialize the next-lower driver's I/O stack location by following the steps that are described in [Processing IRPs in an Intermediate-Level Driver](processing-irps-in-an-intermediate-level-driver.md).

    The dispatch routine can modify some of the parameters in the next-lower driver's I/O stack location for certain requests. For example, a higher-level driver might modify the parameters for a large transfer request when the underlying device has a known limit in transfer capacity, and reuse the IRP to send partial-transfer requests to the underlying device driver.

2.  Call [**IoSetCompletionRoutine**](https://msdn.microsoft.com/library/windows/hardware/ff549679).

    If the dispatch routine is passing a received IRP to the next-lower driver, setting an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine is optional but useful, because the routine can perform such tasks as determining how lower drivers completed the request, reusing the IRP for partial transfers, updating whatever state the driver maintains if it tracks IRPs, and retrying a request that was returned with an error.

    If the dispatch routine has allocated new IRPs, setting an *IoCompletion* routine is required because the routine must release each IRP after lower drivers have completed it.

    For more information about *IoCompletion* routines, see [Completing IRPs](completing-irps.md).

3.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) with each IRP to be processed by lower drivers.

4.  Return an appropriate NTSTATUS value, such as:
    -   STATUS\_PENDING

        The driver usually returns STATUS\_PENDING if the input IRP is an asynchronous request, such as [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) or [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819).

    -   The result of the call to **IoCallDriver**

        The driver frequently returns the result of the call to **IoCallDriver** if the input IRP is a synchronous request, such as [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729).

### A lowest-level device driver passes any IRP that it cannot complete in its dispatch routine on to other driver routines as follows:

1.  Call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) with the input IRP.

2.  Call [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370) to pass on or queue the IRP to the driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, unless the driver manages its own internal IRP queuing, as described in [Driver-Managed IRP Queues](driver-managed-irp-queues.md).

    If the driver does not have a *StartIo* routine but handles cancelable IRPs, it must either register a [*Cancel*](https://msdn.microsoft.com/library/windows/hardware/ff540742) routine or implement a [cancel-safe IRP queue](cancel-safe-irp-queues.md). For more information about *Cancel* routines, see [Canceling IRPs](canceling-irps.md).

3.  Return STATUS\_PENDING.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Passing%20IRPs%20down%20the%20Driver%20Stack%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


