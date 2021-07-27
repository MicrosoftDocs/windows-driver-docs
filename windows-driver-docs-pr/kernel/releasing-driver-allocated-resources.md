---
title: Releasing Driver-Allocated Resources
description: Describes how an Unload routine releases driver-allocated resources in stages.
keywords: ["Unload routines WDK kernel , non-PnP drivers", "non-PnP Unload routine WDK kernel", "releasing driver-allocated resources", "driver-allocated resource releases WDK kernel", "resource releasing WDK kernel"]
ms.date: 07/22/2021
ms.localizationpriority: medium
---

# Releasing Driver-Allocated Resources

The specifics of how a driver uses the registry, sets up system objects and resources in its device extensions, controller extension, or driver-allocated nonpaged pool varies from driver to driver. However, any [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine must release the resources a driver is using in stages.

Any driver's *Unload* routine must ensure that no other driver routine is currently using or might shortly be using a particular resource before it releases that resource.

In general, an *Unload* routine releases all driver-allocated resources in the following stages:

1. If the driver has not already done so, disable interrupts on any physical devices, if possible, and then call [**IoDisconnectInterrupt**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodisconnectinterrupt) as soon as interrupts are disabled.

1. Ensure that no other driver routine can reference the resources that the *Unload* routine intends to release.

    For example, an *Unload* routine must call [**IoStopTimer**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostoptimer) if the driver's [*IoTimer*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_timer_routine) routine is currently enabled for a particular device object. It must ensure that no thread is waiting for any of the driver's dispatcher objects and that its timer objects are not queued for calls to its [*CustomTimerDpc*](using-a-customtimerdpc-routine.md) routines before it frees the storage for its dispatcher objects. It must call [**KeRemoveQueueDpc**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keremovequeuedpc) if it has a [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routine that the ISR might have queued, and so on.

    If the driver called [**IoQueueWorkItem**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioqueueworkitem), it must ensure that the work item has completed. **IoQueueWorkItem** takes out a reference on the associated device object; the driver cannot be unloaded if any such references remain.

    If the driver called [**PsCreateSystemThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-pscreatesystemthread), the *Unload* routine also must cause the driver-created thread to be run so that the thread itself can call [**PsTerminateSystemThread**](/windows-hardware/drivers/ddi/wdm/nf-wdm-psterminatesystemthread) before the driver is unloaded. A driver cannot release a driver-created system thread by calling [**ZwClose**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) with the *ThreadHandle* returned by **PsCreateSystemThread**.

1. Release any device-specific resources that the driver allocated. Doing so might involve calling the following system support routines:

    - [**IoDeleteSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletesymboliclink) if the [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) or [*Reinitialize*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-driver_reinitialize) routine called [**IoCreateSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatesymboliclink) or [**IoCreateUnprotectedSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreateunprotectedsymboliclink), and [**IoDeassignArcName**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iodeassignarcname) if the driver called [**IoAssignArcName**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioassignarcname).

    - [**ExFreePool**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool) if **DriverEntry** or any other driver routine called [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag) and the driver has not yet released the allocated memory.

    - [**MmUnmapIoSpace**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmunmapiospace) if the **DriverEntry** or *Reinitialize* routine called [**MmMapIoSpace**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace).

    - [**MmFreeNonCachedMemory**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmfreenoncachedmemory) if the **DriverEntry** or *Reinitialize* routine called [**MmAllocateNonCachedMemory**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmallocatenoncachedmemory).

    - [**MmFreeContiguousMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmfreecontiguousmemory) if the **DriverEntry** or *Reinitialize* routine called [**MmAllocateContiguousMemory**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmallocatecontiguousmemory).

    - [**FreeCommonBuffer**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_common_buffer) if the **DriverEntry** or *Reinitialize* routine called [**AllocateCommonBuffer**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_common_buffer).

    - [**IoAssignResources**](./mmcreatemdl.md) or [**IoReportResourceUsage**](./mmcreatemdl.md) if the **DriverEntry** or *Reinitialize* routine called one of these support routines or [**HalAssignSlotResources**](/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)) to claim hardware resources in the configuration registry for itself and/or for its physical devices individually.

1. Release system objects and resources that the **DriverEntry** or *Reinitialize* routine set up in the device extension of the device objects or in the controller extension of the controller object (if it created one). In particular, the driver must do the following before it attempts to delete the device object ([**IoDeleteDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice)) or controller object ([**IoDeleteController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-iodeletecontroller)):
    - Call [**IoDisconnectInterrupt**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodisconnectinterrupt) to free the interrupt object pointer stored in the corresponding device or controller extension.
    - Call [**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject) with the pointer to the next-lower driver's file object if it called [**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer) and stored this pointer in a device or controller extension.
    - Call [**IoDetachDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodetachdevice) with the pointer to the lower driver's device object if it called [**IoAttachDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevice) or [**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack) and stored this pointer in a device or controller extension.

1. Free the hardware resources that the **DriverEntry** or *Reinitialize* routine claimed for the driver's physical devices, if any, in the registry under the **\\Registry\\Machine\\Hardware\\ResourceMap** tree.

1. Remove any names for its devices that the **DriverEntry** or *Reinitialize* routine stored in the registry under the **\\Registry..\\DeviceMap** tree, as well.

After the driver has released device, system, and hardware resources, it can delete its device and controller objects, as described in [Releasing Device and Controller Objects](releasing-device-and-controller-objects.md).
