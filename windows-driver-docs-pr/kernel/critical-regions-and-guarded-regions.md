---
title: Critical Regions and Guarded Regions
author: windows-driver-content
description: Critical Regions and Guarded Regions
MS-HAID:
- 'Synchro\_0de10dd5-482b-401e-b49e-3bd0343b63c2.xml'
- 'kernel.critical\_regions\_and\_guarded\_regions'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3781498a-45e9-4f24-8fd2-830eed61298c
keywords: ["asynchronous procedure calls WDK kernel", "APCs WDK kernel", "critical regions WDK kernel", "guarded regions WDK kernel"]
---

# Critical Regions and Guarded Regions


A thread that is inside a *critical region* executes with user APCs and normal kernel APCs disabled. A thread inside a *guarded region* runs with all APCs disabled.

### Critical Regions

A driver can enter and exit a critical region as follows:

-   Call [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) to enter a critical region.

-   Call [**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964) to exit a critical region.

Each call to **KeEnterCriticalRegion** must have a matching call to **KeLeaveCriticalRegion**.

### Guarded Regions

A driver can enter and exit a guarded region as follows:

-   Call [**KeEnterGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552028) to enter a guarded region.

-   Call [**KeLeaveGuardedRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552967) to leave a guarded region.

Each call to **KeEnterGuardedRegion** must have a matching call to **KeLeaveGuardedRegion**.

Drivers that were developed for Windows Server 2003 and later versions of Windows can use guarded regions to disable special kernel APCs. Drivers that were developed for earlier operating systems can disable special kernel APCs by raising the current IRQL to APC\_LEVEL by calling [**KeRaiseIrql**](https://msdn.microsoft.com/library/windows/hardware/ff553079). Use [**KeLowerIrql**](https://msdn.microsoft.com/library/windows/hardware/ff552968) to lower the current IRQL to the previous value.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Critical%20Regions%20and%20Guarded%20Regions%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


