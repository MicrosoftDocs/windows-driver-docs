---
title: AddDevice Routines in Function or Filter Drivers
description: AddDevice Routines in Function or Filter Drivers
keywords: ["function drivers WDK kernel", "filter drivers WDK kernel", "AddDevice routines WDK kernel , function drivers", "AddDevice routines WDK kernel , filter drivers"]
ms.date: 06/16/2017
---

# AddDevice Routines in Function or Filter Drivers





An [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine in a function or filter driver should take the following steps:

1.  Call [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) to create a functional or filter device object (an FDO or filter DO) for the device being added.

    Do not specify a *DeviceName* for the device object, because doing so bypasses the PnP manager's security. If a user-mode component needs a symbolic link to the device, register a device interface (see the next step below). If a kernel-mode component needs a legacy device name, the driver must name the device object, but naming is not recommended.

    Include FILE\_DEVICE\_SECURE\_OPEN in the *DeviceCharacteristics* parameter. This characteristic directs the I/O manager to perform security checks against the device object for all open requests, including relative opens and trailing file name opens.

2.  \[optional\] Create one or more symbolic links to the device.

    Call [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) to register device functionality and create a symbolic link that applications or system components can use to open the device. The driver should enable the interface by calling [**IoSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacestate) when it handles the [**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md) request. For more information, see [Device Interface Classes](../install/overview-of-device-interface-classes.md).

3.  Store the pointer to the device's PDO in the device extension.

    The PnP manager supplies a pointer to the PDO as the *PhysicalDeviceObject* parameter to *AddDevice*. Drivers use the PDO pointer in calls to routines such as [**IoGetDeviceProperty**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceproperty).

4.  Define flags in the device extension to track certain PnP states of the device, such as device paused, removed, and surprise-removed.

    For example, define one flag to indicate that incoming IRPs should be held while the device is in a paused state. Create a queue for holding IRPs, if the driver does not already have a mechanism for queuing IRPs. See [Queuing and Dequeuing IRPs](queuing-and-dequeuing-irps.md) for more information.

    Also allocate an **IO\_REMOVE\_LOCK** structure in the device extension and call [**IoInitializeRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializeremovelock) to initialize this structure. For more information, see [Using Remove Locks](using-remove-locks.md).

5.  Set the DO\_BUFFERED\_IO or DO\_DIRECT\_IO flag bit in the device object to specify the type of buffering that the I/O manager is to use for I/O requests that are sent to the device stack. Higher-level drivers OR this member with the same value as the next-lower driver in the stack, except possibly for highest-level drivers. For more information, see [Initializing a Device Object](initializing-a-device-object.md).

6.  Set the DO\_POWER\_INRUSH or DO\_POWER\_PAGABLE flag for power management, if necessary. Drivers that are pageable must set the DO\_POWER\_PAGABLE flag. The device object flags are typically set by the bus driver when it creates the PDO for the device. However, higher-level drivers may occasionally need to alter the values of these flags in their *AddDevice* routines when they create the FDO or filter DO. See [Setting Device Object Flags for Power Management](setting-device-object-flags-for-power-management.md) for details.

7.  Create and/or initialize any other software resources the driver uses to manage this device, such as events, spin locks, or other objects. (Hardware resources, such as I/O ports, are configured later, in response to an [**IRP\_MN\_START\_DEVICE**](./irp-mn-start-device.md) request.)

    Because an *AddDevice* routine runs in a system thread context at IRQL = PASSIVE\_LEVEL, any memory allocated with [**ExAllocatePoolWithTag**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exallocatepoolwithtag) for use exclusively during initialization can be from paged pool, as long as the driver does not control the device that holds the system page file. Such a memory allocation must be released with [**ExFreePool**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-exfreepool) before *AddDevice* returns control.

8.  Attach the device object to the device stack ([**IoAttachDeviceToDeviceStack**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioattachdevicetodevicestack)).

    Specify a pointer to the device's PDO in the *TargetDevice* parameter.

    Store the pointer returned by **IoAttachDeviceToDeviceStack**. This pointer, which points to the device object of the next-lower driver for the device, is a required parameter to [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) and [**PoCallDriver**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pocalldriver) when passing IRPs down the device stack.

9.  Clear the DO\_DEVICE\_INITIALIZING flag in the FDO or filter DO with a statement like the following:

    ```cpp
    FunctionalDeviceObject->Flags &= ~DO_DEVICE_INITIALIZING;
    ```

10. Be prepared to handle PnP IRPs for the device (such as [**IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS**](./irp-mn-query-resource-requirements.md) and **IRP\_MN\_START\_DEVICE**).

A driver must not start controlling the device until it receives an **IRP\_MN\_START\_DEVICE** containing the list of hardware resources assigned to the device by the PnP manager.

 

