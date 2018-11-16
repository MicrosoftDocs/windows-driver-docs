---
title: Sharing Processor Resources During Startup from a Low-Power State
description: Sharing Processor Resources During Startup from a Low-Power State
ms.assetid: 2b2e6a1b-7c2d-4f38-9407-a417b75daa6a
ms.localizationpriority: medium
ms.date: 10/17/2018
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

 

 




