---
title: Initializing a Device Object
description: Initializing a Device Object
ms.assetid: 97820c62-aade-4ae7-92a6-7490d0ad5697
keywords: ["device objects WDK kernel , initializing", "initializing device objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Initializing a Device Object





After [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) returns, giving the caller a pointer to a *DeviceObject* that contains a pointer to the [*device extension*](device-extensions.md), drivers must set up certain fields in the device objects for their respective physical, logical, and/or virtual devices.

**IoCreateDevice** sets the **StackSize** field of a newly created device object to one. A lowest-level driver can ignore this field. When a higher-level driver calls [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300) to attach itself to the next-lower driver, that routine automatically sets the **StackSize** field in the device object to that of the next-lower driver's device object plus one. For some device types, however, the higher-level driver might need to set the **StackSize** field to a greater value, as noted in the device-specific documentation. Setting the stack size ensures that IRPs sent to the higher-level driver will contain a driver-specific I/O stack location, plus the correct number of I/O stack locations for all lower-level drivers in the chain.

**IoCreateDevice** sets the **AlignmentRequirement** field of a newly created device object to the processor's data cache line size minus one, to ensure that buffers used in direct I/O are aligned correctly. After **IoCreateDevice** returns, lowest-level physical device drivers must do the following:

1.  Subtract one from the alignment requirement of the device.

2.  Compare the result of step 1 with the current value of the device object's **AlignmentRequirement**.

3.  If the device's alignment requirement is greater, set **AlignmentRequirement** to the result of step 1. Otherwise, leave the **AlignmentRequirement** value as set by **IoCreateDevice**.

After any higher-level driver chains itself over another driver by calling [**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198), the higher-level driver must set the **AlignmentRequirement** field of its newly created device object to that of the next-lower-level driver's device object. As a general rule, a higher-level driver should not change this value. If a higher-level driver calls [**IoAttachDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548294) or [**IoAttachDeviceToDeviceStack**](https://msdn.microsoft.com/library/windows/hardware/ff548300), those routines automatically set the **AlignmentRequirement** field in the device object to that of the lower-level driver's device object.

[**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198) returns pointers both to the lower-level driver's device object and to the associated file object. Only an FSD (or, possibly, another highest-level driver) can use the returned file object pointer. An intermediate driver that calls **IoGetDeviceObjectPointer** should save this file object pointer so it can be dereferenced by calling [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724) when the driver is unloaded.

After an FSD mounts the volume containing the file object that represents a lower driver's device object, an intermediate driver cannot chain itself between the file system and the lower driver by calling **IoAttachDevice** or **IoAttachDeviceToDeviceStack**. Additionally, an FSD can set the **SectorSize** member of the device object based on the geometry of the underlying volume hardware when a mount occurs. For more information, see [**DEVICE\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff543147).

An intermediate or lowest-level driver also sets a bit in the device object's **Flags** by ORing it either with DO\_DIRECT\_IO or with DO\_BUFFERED\_IO in every device object it creates. Highest-level drivers of logical or virtual devices can avoid setting **Flags** for either buffered or direct I/O if the driver writer decides the additional work involved will pay off in better driver performance. An intermediate driver must set up the **Flags** field of its device object to match that of the next-lower driver's device object.

Setting up a device object **Flags** field with DO\_DIRECT\_IO or DO\_BUFFERED\_IO determines how the I/O manager passes access to user buffers in all data transfer requests subsequently sent to the driver.

The driver can then set any other device-dependent values in the device object. For example, non-WDM drivers for removable-media devices must OR the device object's **Flags** member with DO\_VERIFY\_VOLUME if they detect (or suspect) a change in media during I/O operations. (See [Supporting Removable Media](supporting-removable-media.md) for more information.) Drivers of devices that require inrush power must OR the **Flags** member with DO\_POWER\_INRUSH, and drivers of devices that are not on the system paging path must OR the **Flags** member with DO\_POWER\_PAGABLE. Function and filter drivers must clear the DO\_DEVICE\_INITIALIZING flag.

After initializing the device object, a driver can also initialize any Kernel-defined objects and other system-defined data structures for which it has provided storage in the device extension. Precisely when a driver performs these tasks depends on its device, the type of the object, and/or the nature of the data. In general, any objects or data structures that can persist through PnP start and stop requests can be initialized in the [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. Those that require resource information provided with a PnP [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request, or that might require changes when the device is stopped and/or restarted, should be initialized when the driver handles the **IRP\_MN\_START\_DEVICE** request. For more information about *AddDevice* routines, see [Writing an AddDevice Routine](writing-an-adddevice-routine.md).

 

 




