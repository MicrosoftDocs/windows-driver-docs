---
title: Using IoCompletion Routines
description: Using IoCompletion Routines
ms.assetid: 07a6e930-eef0-4408-9f71-55a827aa558e
keywords: ["IoCompletion routines", "completing IRPs WDK kernel , IoCompletion routines", "completing IRPs WDK kernel , dispatch routines", "dispatch routines WDK kernel , completing IRPs"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Using IoCompletion Routines





Higher-level drivers that monitor on an IRP-specific basis how lower-level drivers carried out particular requests can have one or more [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines. Higher-level drivers that allocate IRPs to send requests to lower drivers must have an *IoCompletion* routine.

A highest-level or intermediate driver's [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376) or [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034) routine is most likely to set an *IoCompletion* routine for an IRP, because lower-level drivers must handle transfer requests asynchronously.

The lowest-level driver in a driver stack cannot register *IoCompletion* routines.

Drivers generally do not register *IoCompletion* routines for IRPs associated with synchronous I/O operations. For instance, a higher-level driver's [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine can allocate an IRP using [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318). In this case, the dispatch routine typically does not register an *IoCompletion* routine, because device control requests are generally handled synchronously. Instead, the driver can allocate and initialize an event object, and its *DispatchDeviceControl* routine can wait for an event to be initialized when it sends on driver-allocated IRPs. Usually, a higher-level driver does not register an *IoCompletion* routine for an IRP allocated with [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330), for the same reason.

This section contains the following topics:

[Registering an IoCompletion Routine](registering-an-iocompletion-routine.md)

[Implementing an IoCompletion Routine](implementing-an-iocompletion-routine.md)

 

 




