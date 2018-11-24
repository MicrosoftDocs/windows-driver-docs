---
title: Storage Class Driver's GetDescriptor Routine
description: Storage Class Driver's GetDescriptor Routine
ms.assetid: d1ddcfe8-f276-4e45-82b7-0f07f0526c71
keywords:
- GetDescriptor
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storage Class Driver's GetDescriptor Routine


## <span id="ddk_storage_class_drivers_getdescriptor_routine_kg"></span><span id="DDK_STORAGE_CLASS_DRIVERS_GETDESCRIPTOR_ROUTINE_KG"></span>


For data transfer operations, storage class drivers need configuration information about each HBA driving a bus to which their devices are attached. To get this information, a class driver either calls an internal *GetDescriptor* routine or implements the same functionality in its *StartDevice* routine. (For information about *StartDevice*, see [Handling PnP Start in a Storage Class Driver](handling-pnp-start-in-a-storage-class-driver.md).)

A *GetDescriptor* routine builds and sets up query-property requests ([**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) with [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff560590)) for the port driver to retrieve device and adapter descriptors which the class driver stores in its device extension. The class driver might also set driver-writer-determined flags in the device extension according to the returned descriptor data.

The class driver inspects the returned [**STORAGE\_DEVICE\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566971) data to determine device capabilities (SCSI inquiry data or the non-SCSI equivalent) such as the SCSI device type, whether the device's media (if any) is removable (**RemovableMedia**), whether the device supports multiple outstanding commands (**CommandQueueing**), and various ID strings. The class driver inspects the returned [**STORAGE\_ADAPTER\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff566346) data to determine adapter capabilities, including:

-   The maximum number of bytes a particular HBA can transfer in a single operation (**MaximumTransferLength**).

-   If the HBA can transfer buffered data backed by noncontiguous physical pages (in other words, if it supports scatter/gather), how many noncontiguous physical pages per buffer it can manage, per transfer operation (**MaximumPhysicalPages**).

-   The HBA's alignment requirements for transfers so the class driver can properly set the **AlignmentRequirement** field in its device objects (**AlignmentMask**).

    Applications that send [**IOCTL\_SCSI\_PASS\_THROUGH**](https://msdn.microsoft.com/library/windows/hardware/ff560519) requests also might use this field.

    For more information about setting up **AlignmentRequirement** in device objects, see [Initializing a Device Object](https://msdn.microsoft.com/library/windows/hardware/ff547807).

-   Whether the HBA supports SCSI tagged queuing and/or per-logical-unit internal queues (**CommandQueueing**).

-   Whether the HBA supports synchronous transfers (**AcceleratedTransfer**).

-   Whether the HBA caches data internally (**CachesData**).

The class driver should store this information in the FDO's device extension so its dispatch routines can ensure that all requests sent to the storage port driver conform to the size, number of physical breaks, and alignment requirements of the underlying HBA. For more information about class driver dispatch routines, see [Storage Class Driver's Dispatch Routines](storage-class-driver-s-dispatch-routines.md). For more information about setting up device extensions, see [Setting Up a Storage Class Driver's Device Extension](setting-up-a-storage-class-driver-s-device-extension.md).

 

 




