---
title: PnP Driver's Unload Routine
author: windows-driver-content
description: PnP Driver's Unload Routine
ms.assetid: 71b30a84-d3c7-4674-94a6-b99f83567183
keywords: ["Unload routines WDK kernel , PnP drivers", "PnP Unload routine WDK kernel", "Plug and Play Unload routine WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PnP Driver's Unload Routine


## <a href="" id="ddk-a-pnp-driver-s-unload-routine-kg"></a>


A PnP driver must have an [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine that removes any driver-specific resources, such as memory, threads, and events, that are created by the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. If there are no driver-specific resources to remove, the driver must still have an *Unload* routine but it can simply return.

A driver's *Unload* routine can be called at any time after all the driver's devices have been removed. The PnP manager calls a driver's *Unload* routine in the context of a system thread at IRQL = PASSIVE\_LEVEL.

PnP drivers free device-specific resources and device objects in response to PnP device-removal IRPs. The PnP manager sends these IRPs on behalf of each PnP device it enumerates as well as any root-enumerated legacy devices a driver reports using [**IoReportDetectedDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549597).

Consequently, the *Unload* routines of PnP drivers are usually simple, often consisting only of a **return** statement. However, if the driver allocated any driver-wide resources in its **DriverEntry** routine, it must deallocate those resources in its *Unload* routine unless it has already done so. In general, the process of unloading a PnP driver is a synchronous operation.

The I/O manager frees the driver object and any driver object extension that the driver allocated using [**IoAllocateDriverObjectExtension**](https://msdn.microsoft.com/library/windows/hardware/ff548233).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20PnP%20Driver's%20Unload%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


