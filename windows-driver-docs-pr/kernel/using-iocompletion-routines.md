---
title: Using IoCompletion Routines
author: windows-driver-content
description: Using IoCompletion Routines
MS-HAID:
- 'IRPs\_f76da76d-d265-426e-bc15-96ee30337e74.xml'
- 'kernel.using\_iocompletion\_routines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 07a6e930-eef0-4408-9f71-55a827aa558e
keywords: ["IoCompletion routines", "completing IRPs WDK kernel , IoCompletion routines", "completing IRPs WDK kernel , dispatch routines", "dispatch routines WDK kernel , completing IRPs"]
---

# Using IoCompletion Routines


## <a href="" id="ddk-using-iocompletion-routines-kg"></a>


Higher-level drivers that monitor on an IRP-specific basis how lower-level drivers carried out particular requests can have one or more [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines. Higher-level drivers that allocate IRPs to send requests to lower drivers must have an *IoCompletion* routine.

A highest-level or intermediate driver's [*DispatchRead*](https://msdn.microsoft.com/library/windows/hardware/ff543376) or [*DispatchWrite*](https://msdn.microsoft.com/library/windows/hardware/ff544034) routine is most likely to set an *IoCompletion* routine for an IRP, because lower-level drivers must handle transfer requests asynchronously.

The lowest-level driver in a driver stack cannot register *IoCompletion* routines.

Drivers generally do not register *IoCompletion* routines for IRPs associated with synchronous I/O operations. For instance, a higher-level driver's [*DispatchDeviceControl*](https://msdn.microsoft.com/library/windows/hardware/ff543287) routine can allocate an IRP using [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318). In this case, the dispatch routine typically does not register an *IoCompletion* routine, because device control requests are generally handled synchronously. Instead, the driver can allocate and initialize an event object, and its *DispatchDeviceControl* routine can wait for an event to be initialized when it sends on driver-allocated IRPs. Usually, a higher-level driver does not register an *IoCompletion* routine for an IRP allocated with [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330), for the same reason.

This section contains the following topics:

[Registering an IoCompletion Routine](registering-an-iocompletion-routine.md)

[Implementing an IoCompletion Routine](implementing-an-iocompletion-routine.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20IoCompletion%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


