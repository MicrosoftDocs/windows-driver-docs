---
title: Introduction to DPCs
author: windows-driver-content
description: Introduction to DPCs
ms.assetid: 10e8d0e7-c04a-4dca-853c-74c911f59341
keywords: ["deferred procedure calls WDK kernel", "DPCs WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Introduction to DPCs


## <a href="" id="ddk-introduction-to-dpcs-kg"></a>


Any driver that has an ISR typically also has at least one [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine to complete processing of interrupt-driven I/O operations. A typical lowest-level driver's *DpcForIsr* or *CustomDpc* routine does the following:

-   Finishes handling an I/O operation that the ISR began processing.

-   Dequeues the next IRP so that the driver can begin processing it.

-   Completes the current IRP, if possible.

Sometimes the current IRP cannot be completed because several data transfers are required, or a recoverable error was detected. In these cases, the *DpcForIsr* or *CustomDpc* routine typically reprograms the device for either another transfer or a retry of the last operation.

A *DpcForIsr* or *CustomDpc* routine is called in an arbitrary DPC context at IRQL DISPATCH\_LEVEL. Running at DISPATCH\_LEVEL restricts the set of support routines a *DpcForIsr* or *CustomDpc* routine can call. See [Managing Hardware Priorities](managing-hardware-priorities.md) for more information.

DPC objects and DPCs can also be used with timers. For more information, see [Timer Objects and DPCs](timer-objects-and-dpcs.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Introduction%20to%20DPCs%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


