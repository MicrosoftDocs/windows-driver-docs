---
title: Storage Class Driver's GetDescriptor Routine
description: Storage Class Driver's GetDescriptor Routine
ms.assetid: d1ddcfe8-f276-4e45-82b7-0f07f0526c71
keywords: ["GetDescriptor"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Storage%20Class%20Driver's%20GetDescriptor%20Routine%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




