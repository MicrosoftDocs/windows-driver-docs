---
title: When to Complete an IRP in a Dispatch Routine
description: When to Complete an IRP in a Dispatch Routine
ms.assetid: 24159535-927f-490c-9472-05ea565b7ae5
keywords: ["completing IRPs WDK kernel , dispatch routines", "dispatch routines WDK kernel , completing IRPs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# When to Complete an IRP in a Dispatch Routine





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

 

 




