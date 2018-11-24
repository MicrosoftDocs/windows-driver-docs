---
title: Introduction to DPCs
description: Introduction to DPCs
ms.assetid: 10e8d0e7-c04a-4dca-853c-74c911f59341
keywords: ["deferred procedure calls WDK kernel", "DPCs WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Introduction to DPCs





Any driver that has an ISR typically also has at least one [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine to complete processing of interrupt-driven I/O operations. A typical lowest-level driver's *DpcForIsr* or *CustomDpc* routine does the following:

-   Finishes handling an I/O operation that the ISR began processing.

-   Dequeues the next IRP so that the driver can begin processing it.

-   Completes the current IRP, if possible.

Sometimes the current IRP cannot be completed because several data transfers are required, or a recoverable error was detected. In these cases, the *DpcForIsr* or *CustomDpc* routine typically reprograms the device for either another transfer or a retry of the last operation.

A *DpcForIsr* or *CustomDpc* routine is called in an arbitrary DPC context at IRQL DISPATCH\_LEVEL. Running at DISPATCH\_LEVEL restricts the set of support routines a *DpcForIsr* or *CustomDpc* routine can call. See [Managing Hardware Priorities](managing-hardware-priorities.md) for more information.

DPC objects and DPCs can also be used with timers. For more information, see [Timer Objects and DPCs](timer-objects-and-dpcs.md).

 

 




