---
title: Sharing Processor Resources During Startup from a Low-Power State
author: windows-driver-content
description: Sharing Processor Resources During Startup from a Low-Power State
ms.assetid: 2b2e6a1b-7c2d-4f38-9407-a417b75daa6a
---

# Sharing Processor Resources During Startup from a Low-Power State


When a computer is started from a standby or hibernation state (warm startup), drivers should avoid using processor resources for longer than is necessary. Most importantly, deferred procedure call (DPC) routines and code that executes at IRQL &gt;= DISPATCH\_LEVEL should keep their execution times to a minimum. Drivers use DPC routines to help to initialize devices. Drivers might need to run initialization code at DISPATCH\_LEVEL as part of a port-miniport interface contract.

While a DPC routine runs, other threads of lower priority are blocked from running on the same processor. In addition, other DPC routines that are queued and ready to run might be blocked until the current DPC is finished. To enable other threads to run expediently, a typical DPC routine should run for no more than 100 microseconds.

A DPC routine that runs for too long during system startup can delay the initialization of other devices. This delay makes the device initialization phase longer and delays startup completion by the operating system.

Use the following best practices to design your DPC routines:

-   A single DPC routine should not execute for more than 100 microseconds.

-   DPC routines that call the [**KeStallExecutionProcessor**](https://msdn.microsoft.com/library/windows/hardware/ff553295) routine to delay execution must not specify delays of more than 100 microseconds.

-   If a task requires longer than 100 microseconds and executes at DISPATCH\_LEVEL, the DPC routine should end after 100 microseconds and schedule one or more DPC timer routines to complete the task at a later time.

-   Use the performance analysis tools that are documented in the WDK to evaluate the execution times of DPC routines.

For more information about performance analysis tools, see [Measuring System Resume Performance on Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=69964).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Sharing%20Processor%20Resources%20During%20Startup%20from%20a%20Low-Power%20State%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


