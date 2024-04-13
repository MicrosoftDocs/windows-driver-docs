---
title: Critical Regions and Guarded Regions
description: Critical Regions and Guarded Regions
keywords: ["asynchronous procedure calls WDK kernel", "APCs WDK kernel", "critical regions WDK kernel", "guarded regions WDK kernel"]
ms.date: 06/16/2017
---

# Critical Regions and Guarded Regions


A thread that is inside a *critical region* executes with user APCs and normal kernel APCs disabled. A thread inside a *guarded region* runs with all APCs disabled.

### Critical Regions

A driver can enter and exit a critical region as follows:

-   Call [**KeEnterCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion) to enter a critical region.

-   Call [**KeLeaveCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleavecriticalregion) to exit a critical region.

Each call to **KeEnterCriticalRegion** must have a matching call to **KeLeaveCriticalRegion**.

### Guarded Regions

A driver can enter and exit a guarded region as follows:

-   Call [**KeEnterGuardedRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keenterguardedregion) to enter a guarded region.

-   Call [**KeLeaveGuardedRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleaveguardedregion) to leave a guarded region.

Each call to **KeEnterGuardedRegion** must have a matching call to **KeLeaveGuardedRegion**.

Drivers that were developed for Windows Server 2003 and later versions of Windows can use guarded regions to disable special kernel APCs. Drivers that were developed for earlier operating systems can disable special kernel APCs by raising the current IRQL to APC\_LEVEL by calling [**KeRaiseIrql**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirql). Use [**KeLowerIrql**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kelowerirql) to lower the current IRQL to the previous value.

 

