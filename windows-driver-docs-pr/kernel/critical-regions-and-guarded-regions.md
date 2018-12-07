---
title: Critical Regions and Guarded Regions
description: Critical Regions and Guarded Regions
ms.assetid: 3781498a-45e9-4f24-8fd2-830eed61298c
keywords: ["asynchronous procedure calls WDK kernel", "APCs WDK kernel", "critical regions WDK kernel", "guarded regions WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
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

 

 




