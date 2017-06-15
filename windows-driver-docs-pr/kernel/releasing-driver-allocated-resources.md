---
title: Releasing Driver-Allocated Resources
author: windows-driver-content
description: Releasing Driver-Allocated Resources
MS-HAID:
- 'DrvComps\_09d55cac-8c73-403c-adfe-e20a8a4db714.xml'
- 'kernel.releasing\_driver\_allocated\_resources'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b286b4b0-54f2-4798-a77b-c08743502552
keywords: ["Unload routines WDK kernel , non-PnP drivers", "non-PnP Unload routine WDK kernel", "releasing driver-allocated resources", "driver-allocated resource releases WDK kernel", "resource releasing WDK kernel"]
---

# Releasing Driver-Allocated Resources


## <a href="" id="ddk-releasing-driver-allocated-resources-kg"></a>


The specifics of how a driver uses the registry, sets up system objects and resources in its device extensions, controller extension, or driver-allocated nonpaged pool varies from driver to driver. However, any [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine must release the resources a driver is using in stages.

Any driver's *Unload* routine must ensure that no other driver routine is currently using or might shortly be using a particular resource before it releases that resource.

In general, an *Unload* routine releases all driver-allocated resources in the following stages:

1.  If the driver has not already done so, disable interrupts on any physical devices, if possible, and then call [**IoDisconnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff549089) as soon as interrupts are disabled.

2.  Ensure that no other driver routine can reference the resources that the *Unload* routine intends to release.

    For example, an *Unload* routine must call [**IoStopTimer**](https://msdn.microsoft.com/library/windows/hardware/ff550377) if the driver's [*IoTimer*](https://msdn.microsoft.com/library/windows/hardware/ff550381) routine is currently enabled for a particular device object. It must ensure that no thread is waiting for any of the driver's dispatcher objects and that its timer objects are not queued for calls to its [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) routines before it frees the storage for its dispatcher objects. It must call [**KeRemoveQueueDpc**](https://msdn.microsoft.com/library/windows/hardware/ff553169) if it has a [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine that the ISR might have queued, and so on.

    If the driver called [**IoQueueWorkItem**](https://msdn.microsoft.com/library/windows/hardware/ff549466), it must ensure that the work item has completed. **IoQueueWorkItem** takes out a reference on the associated device object; the driver cannot be unloaded if any such references remain.

    If the driver called [**PsCreateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559932), the *Unload* routine also must cause the driver-created thread to be run so that the thread itself can call [**PsTerminateSystemThread**](https://msdn.microsoft.com/library/windows/hardware/ff559959) before the driver is unloaded. A driver cannot release a driver-created system thread by calling [**ZwClose**](https://msdn.microsoft.com/library/windows/hardware/ff566417) with the *ThreadHandle* returned by **PsCreateSystemThread**.

3.  Release any device-specific resources that the driver allocated. Doing so might involve calling the following system support routines:
    -   [**IoDeleteSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549085) if the [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) or [*Reinitialize*](https://msdn.microsoft.com/library/windows/hardware/ff561022) routine called [**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043) or [**IoCreateUnprotectedSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549050), and [**IoDeassignArcName**](https://msdn.microsoft.com/library/windows/hardware/ff549076) if the driver called [**IoAssignArcName**](https://msdn.microsoft.com/library/windows/hardware/ff548282).

    -   [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590) if **DriverEntry** or any other driver routine called [**ExAllocatePoolWithTag**](https://msdn.microsoft.com/library/windows/hardware/ff544520) and the driver has not yet released the allocated memory.

    -   [**MmUnmapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff556387) if the **DriverEntry** or *Reinitialize* routine called [**MmMapIoSpace**](https://msdn.microsoft.com/library/windows/hardware/ff554618).

    -   [**MmFreeNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554516) if the **DriverEntry** or *Reinitialize* routine called [**MmAllocateNonCachedMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554479).

    -   [**MmFreeContiguousMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554503) if the **DriverEntry** or *Reinitialize* routine called [**MmAllocateContiguousMemory**](https://msdn.microsoft.com/library/windows/hardware/ff554460).

    -   [**FreeCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff546511) if the **DriverEntry** or *Reinitialize* routine called [**AllocateCommonBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff540575).

    -   [**IoAssignResources**](https://msdn.microsoft.com/library/windows/hardware/ff548285) or [**IoReportResourceUsage**](https://msdn.microsoft.com/library/windows/hardware/ff549616) if the **DriverEntry** or *Reinitialize* routine called one of these support routines or [**HalAssignSlotResources**](https://msdn.microsoft.com/library/windows/hardware/ff546580) to claim hardware resources in the configuration registry for itself and/or for its physical devices individually.

4.  Release system objects and resources that the **DriverEntry** or *Reinitialize* routine set up in the device extension of the device objects or in the controller extension of the controller object (if it created one). In particular, the driver must do the following before it attempts to delete the device object ([**IoDeleteDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549083)) or controller object ([**IoDeleteController**](https://msdn.microsoft.com/library/windows/hardware/ff549078)):
    -   Call [**IoDisconnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff549089) to free the interrupt object pointer stored in the corresponding device or controller extension.
    -   Call [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) with the pointer to the next-lower driver's file object if it called [**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198) and stored this pointer in a device or controller extension.
    -   Call [**IoDetachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff549087) with the pointer to the lower driver's device object if it called [**IoAttachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548294) or [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) and stored this pointer in a device or controller extension.

5.  Free the hardware resources that the **DriverEntry** or *Reinitialize* routine claimed for the driver's physical devices, if any, in the registry under the **\\Registry\\Machine\\Hardware\\ResourceMap** tree.

6.  Remove any names for its devices that the **DriverEntry** or *Reinitialize* routine stored in the registry under the **\\Registry..\\DeviceMap** tree, as well.

After the driver has released device, system, and hardware resources, it can delete its device and controller objects, as described in the following section.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Releasing%20Driver-Allocated%20Resources%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


