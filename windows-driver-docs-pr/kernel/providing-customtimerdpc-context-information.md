---
title: Providing CustomTimerDpc Context Information
author: windows-driver-content
description: Providing CustomTimerDpc Context Information
MS-HAID:
- 'Synchro\_a370daba-10cb-4779-8516-5fd979ef9f6b.xml'
- 'kernel.providing\_customtimerdpc\_context\_information'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b4d711fb-63d4-45c6-8054-f934741ce340
keywords: ["timer objects WDK kernel , CustomTimerDpc routines", "CustomTimerDpc", "DeferredContext routine", "context information WDK synchronization", "timer objects WDK kernel , context information"]
---

# Providing CustomTimerDpc Context Information


## <a href="" id="ddk-providing-customtimerdpc-context-information-kg"></a>


The *DeferredContext* pointer passed to [**KeInitializeDpc**](https://msdn.microsoft.com/library/windows/hardware/ff552130) points to a context area where other driver routines, and the *CustomTimerDpc* routine itself, can maintain state. The kernel passes the *DeferredContext* pointer in every call to the DPC routine.

Unlike an *IoTimer* routine, a *CustomTimerDpc* has no particular associations with a driver-created device object. However, a driver can associate a *CustomTimerDpc* routine with a driver-created device object by including a pointer to the device object in its context area.

The context area must be in resident, driver-allocated memory. Usually, this context area is in a device extension, but it can also be in nonpaged pool. If the driver uses a controller object, it can be in a controller extension. The contents of the context area are driver-determined.

If a *CustomTimerDpc* routine shares context information with the driver's ISR, the *CustomTimerDpc* routine must use [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302) to call a *SynchCritSection* routine that accesses the shared context. For more information, see [Using Critical Sections](using-critical-sections.md).

If the *CustomTimerDpc* shares the context information with other non-ISR driver routines, the area at *DeferredContext* must be protected by an executive spin lock. For more information, see [Spin Locks](spin-locks.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Providing%20CustomTimerDpc%20Context%20Information%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


