---
title: Releasing Driver-Allocated Resources
description: Releasing Driver-Allocated Resources
ms.assetid: b286b4b0-54f2-4798-a77b-c08743502552
keywords: ["Unload routines WDK kernel , non-PnP drivers", "non-PnP Unload routine WDK kernel", "releasing driver-allocated resources", "driver-allocated resource releases WDK kernel", "resource releasing WDK kernel"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Releasing Driver-Allocated Resources





The specifics of how a driver uses the registry, sets up system objects and resources in its device extensions, controller extension, or driver-allocated nonpaged pool varies from driver to driver. However, any [*Unload*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine must release the resources a driver is using in stages.

Any driver's *Unload* routine must ensure that no other driver routine is currently using or might shortly be using a particular resource before it releases that resource.

In general, an *Unload* routine releases all driver-allocated resources in the following stages:

1.  If the driver has not already done so, disable interrupts on any physical devices, if possible, and then call [**IoDisconnectInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iodisconnectinterrupt) as soon as interrupts are disabled.

2.  Ensure that no other driver routine can reference the resources that the *Unload* routine intends to release.

    For example, an *Unload* routine must call [**IoStopTimer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostoptimer) if the driver's [*IoTimer*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-io_timer_routine) routine is currently enabled for a particular device object. It must ensure that no thread is waiting for any of the driver's dispatcher objects and that its timer objects are not queued for calls to its [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) routines before it frees the storage for its dispatcher objects. It must call [**KeRemoveQueueDpc**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-keremovequeuedpc) if it has a [*CustomDpc*](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routine that the ISR might have queued, and so on.

    If the driver called [**IoQueueWorkItem**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-ioqueueworkitem), it must ensure that the work item has completed. **IoQueueWorkItem** takes out a reference on the associated device object; the driver cannot be unloaded if any such references remain.

    If the driver called [**PsCreateSystemThread**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-pscreatesystemthread), the *Unload* routine also must cause the driver-created thread to be run so that the thread itself can call [**PsTerminateSystemThread**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-psterminatesystemthread) before the driver is unloaded. A driver cannot release a driver-created system thread by calling [**ZwClose**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) with the *ThreadHandle* returned by **PsCreateSystemThread**.

3.  Release any device-specific resources that the driver allocated. Doing so might involve calling the following system support routines:
    -   [**IoDeleteSymbolicLink**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletesymboliclink) if the [**DriverEntry**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) or [*Reinitialize*](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nc-ntddk-driver_reinitialize) routine called [**IoCreateSymbolicLink**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatesymboliclink) or [**IoCreateUnprotectedSymbolicLink**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreateunprotectedsymboliclink), and [**IoDeassignArcName**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iodeassignarcname) if the driver called [**IoAssignArcName**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioassignarcname).

    -   [**ExFreePool**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool) if **DriverEntry** or any other driver routine called [**ExAllocatePoolWithTag**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag) and the driver has not yet released the allocated memory.

    -   [**MmUnmapIoSpace**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapiospace) if the **DriverEntry** or *Reinitialize* routine called [**MmMapIoSpace**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace).

    -   [**MmFreeNonCachedMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmfreenoncachedmemory) if the **DriverEntry** or *Reinitialize* routine called [**MmAllocateNonCachedMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmallocatenoncachedmemory).

    -   [**MmFreeContiguousMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-mmfreecontiguousmemory) if the **DriverEntry** or *Reinitialize* routine called [**MmAllocateContiguousMemory**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemory).

    -   [**FreeCommonBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_common_buffer) if the **DriverEntry** or *Reinitialize* routine called [**AllocateCommonBuffer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_common_buffer).

    -   [**IoAssignResources**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mmcreatemdl) or [**IoReportResourceUsage**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mmcreatemdl) if the **DriverEntry** or *Reinitialize* routine called one of these support routines or [**HalAssignSlotResources**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)) to claim hardware resources in the configuration registry for itself and/or for its physical devices individually.

4.  Release system objects and resources that the **DriverEntry** or *Reinitialize* routine set up in the device extension of the device objects or in the controller extension of the controller object (if it created one). In particular, the driver must do the following before it attempts to delete the device object ([**IoDeleteDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice)) or controller object ([**IoDeleteController**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iodeletecontroller)):
    -   Call [**IoDisconnectInterrupt**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iodisconnectinterrupt) to free the interrupt object pointer stored in the corresponding device or controller extension.
    -   Call [**ObDereferenceObject**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) with the pointer to the next-lower driver's file object if it called [**IoGetDeviceObjectPointer**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer) and stored this pointer in a device or controller extension.
    -   Call [**IoDetachDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-iodetachdevice) with the pointer to the lower driver's device object if it called [**IoAttachDevice**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevice) or [**IoAttachDeviceToDeviceStack**](https://docs.microsoft.com/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack) and stored this pointer in a device or controller extension.

5.  Free the hardware resources that the **DriverEntry** or *Reinitialize* routine claimed for the driver's physical devices, if any, in the registry under the **\\Registry\\Machine\\Hardware\\ResourceMap** tree.

6.  Remove any names for its devices that the **DriverEntry** or *Reinitialize* routine stored in the registry under the **\\Registry..\\DeviceMap** tree, as well.

After the driver has released device, system, and hardware resources, it can delete its device and controller objects, as described in the following section.

 

 




