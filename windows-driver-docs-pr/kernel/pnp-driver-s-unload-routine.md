---
title: PnP Driver's Unload Routine
description: PnP Driver's Unload Routine
ms.assetid: 71b30a84-d3c7-4674-94a6-b99f83567183
keywords: ["Unload routines WDK kernel , PnP drivers", "PnP Unload routine WDK kernel", "Plug and Play Unload routine WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# PnP Driver's Unload Routine





A PnP driver must have an [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine that removes any driver-specific resources, such as memory, threads, and events, that are created by the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. If there are no driver-specific resources to remove, the driver must still have an *Unload* routine but it can simply return.

A driver's *Unload* routine can be called at any time after all the driver's devices have been removed. The PnP manager calls a driver's *Unload* routine in the context of a system thread at IRQL = PASSIVE\_LEVEL.

PnP drivers free device-specific resources and device objects in response to PnP device-removal IRPs. The PnP manager sends these IRPs on behalf of each PnP device it enumerates as well as any root-enumerated legacy devices a driver reports using [**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597).

Consequently, the *Unload* routines of PnP drivers are usually simple, often consisting only of a **return** statement. However, if the driver allocated any driver-wide resources in its **DriverEntry** routine, it must deallocate those resources in its *Unload* routine unless it has already done so. In general, the process of unloading a PnP driver is a synchronous operation.

The I/O manager frees the driver object and any driver object extension that the driver allocated using [**IoAllocateDriverObjectExtension**](https://msdn.microsoft.com/library/windows/hardware/ff548233).

 

 




