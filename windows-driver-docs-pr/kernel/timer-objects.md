---
title: Timer Objects
author: windows-driver-content
description: Any driver can use a timer object within a nonarbitrary thread context to time-out operations in the driver's other routines, or to schedule operations to be performed periodically.
ms.assetid: A4844F19-3BEC-48C0-A5BF-E17CCEEC1601
---

# Timer Objects


Any driver can use a timer object within a nonarbitrary thread context to time-out operations in the driver's other routines, or to schedule operations to be performed periodically. Starting with Windows 2000, timer objects based on the [**KTIMER**](https://msdn.microsoft.com/library/windows/hardware/ff554250) structure are available to use with [**KeSetTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553286) and the other **Ke*Xxx*Timer** routines. Starting with Windows 8.1, timer objects based on the [**EX\_TIMER**](https://msdn.microsoft.com/library/windows/hardware/dn265199) structure are available to use with [**ExSetTimer**](https://msdn.microsoft.com/library/windows/hardware/dn265188) and the other **Ex*Xxx*Timer** routines. Timer objects based on the **KTIMER** and **EX\_TIMER** structures are [kernel dispatcher objects](kernel-dispatcher-objects.md) that are signaled when a timer expires. Timer expiration can be periodic or one-shot (nonperiodic).

This section contains the following topics:

-   [KeXxxTimer Routines, KTIMER Objects, and DPCs](timer-objects-and-dpcs.md)

-   [ExXxxTimer Routines and EX\_TIMER Objects](exxxxtimer-routines-and-ex-timer-objects.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Timer%20Objects%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


