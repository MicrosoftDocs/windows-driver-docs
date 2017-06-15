---
title: When to Complete an IRP in a Dispatch Routine
author: windows-driver-content
description: When to Complete an IRP in a Dispatch Routine
MS-HAID:
- 'IRPs\_6314289f-b703-409e-89c9-66c7193cc045.xml'
- 'kernel.when\_to\_complete\_an\_irp\_in\_a\_dispatch\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 24159535-927f-490c-9472-05ea565b7ae5
keywords: ["completing IRPs WDK kernel , dispatch routines", "dispatch routines WDK kernel , completing IRPs"]
---

# When to Complete an IRP in a Dispatch Routine


## <a href="" id="ddk-when-to-complete-an-irp-in-a-dispatch-routine-kg"></a>


Usually, drivers do not complete IRPs in their dispatch routines unless the parameters for the given request are invalid or, in a device driver, unless the particular **IRP\_MJ\_*XXX*** requires no device I/O operations.

Every driver in a chain of layered drivers can check the validity of parameters in its own I/O stack location, for each IRP received by the driver's dispatch routines. Completing IRPs with invalid parameters in the dispatch routine of the highest possible driver improves I/O throughput for any chain of drivers and for the system overall.

A dispatch routine in a higher-level driver should either complete an IRP or pass it on for processing by lower drivers, according to the following guidelines:

-   If the dispatch routine determines that any parameters in its own I/O stack location are invalid, it should complete that IRP immediately with an appropriate error status, such as STATUS\_INVALID\_PARAMETER.

-   If the IRP contains the function code [**IRP\_MJ\_CLEANUP**](https://msdn.microsoft.com/library/windows/hardware/ff550718), the [*DispatchCleanup*](https://msdn.microsoft.com/library/windows/hardware/ff543233) routine must complete every IRP currently queued to the target device object, for the file object specified in the driver's I/O stack location, and complete the cleanup IRP.

    A cleanup request indicates that an application is being terminated or has closed a file handle for the file object that represents the driver's device object. When the *DispatchCleanup* routine returns, usually the driver's [*DispatchClose*](https://msdn.microsoft.com/library/windows/hardware/ff543255) routine is called next.

-   Otherwise, a higher-level driver can satisfy the request only by passing it on to the next-lower driver.

A dispatch routine in a lowest-level driver should complete an IRP according to the following guidelines:

-   If the dispatch routine determines that any parameters in its own I/O stack location are invalid, or if the driver does not support the IRP, it should complete that IRP immediately with an appropriate error status. In such cases the driver must not complete the IRP with a status value of STATUS\_SUCCESS.

    Usually, any higher-level driver has already checked the parameters for a requested operation, but lowest-level device drivers should perform their own parameters checks as well.

-   If the IRP contains the function code **IRP\_MJ\_CLEANUP**, the *DispatchCleanup* routine must complete every IRP currently queued to the target device object, for the given file object in the driver's I/O stack location, and then complete the cleanup IRP.

    A cleanup request indicates that an application is being terminated or has closed a file handle for the file object that represents the driver's device object. When the *DispatchCleanup* routine returns, usually the driver's *DispatchClose* routine is called next.

-   If the request requires no device I/O operation, the dispatch routine should satisfy the request and complete the IRP.

    For example, a driver might save the current mode of its device in the device extension, particularly if it seldom changes device modes after initialization. Its [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine could then satisfy a request that queried the current device mode by returning this stored information.

Otherwise, the dispatch routine must call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422), queue the IRP to other driver routines for further processing, and return STATUS\_PENDING.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20When%20to%20Complete%20an%20IRP%20in%20a%20Dispatch%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


