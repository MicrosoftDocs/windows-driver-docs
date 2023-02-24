---
title: Creating the Control Device Object
description: Creating the Control Device Object
keywords:
- control device objects WDK file system
- CDOs WDK file system
ms.date: 02/23/2023
---

# Creating the Control Device Object

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A legacy file system filter driver's [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine usually begins by creating a *control device object*. The purpose of the control device object is to allow applications to communicate with the filter driver directly, even before the filter is attached to a file system or volume device object.

File systems also create control device objects. When a file system filter driver attaches itself to a file system, rather than an individual file system volume, it does so by attaching itself to the file system's control device object.

The following example creates a control device object:

```cpp
RtlInitUnicodeString(&nameString, MYLEGACYFILTER_FULLDEVICE_NAME);
status = IoCreateDevice(
        DriverObject,                  //DriverObject
        0,                             //DeviceExtensionSize
        &nameString,                   //DeviceName
        FILE_DEVICE_DISK_FILE_SYSTEM,  //DeviceType
        FILE_DEVICE_SECURE_OPEN,       //DeviceCharacteristics
        FALSE,                         //Exclusive
        &gControlDeviceObject);        //DeviceObject

RtlInitUnicodeString(&linkString, MYLEGACYFILTER_DOSDEVICE_NAME);
status = IoCreateSymbolicLink(&linkString, &nameString);
```

Unlike file systems, file system filter drivers aren't required to name their control device objects. A user mode application can't access the filter driver without a device name since a call to [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) isn't valid for control device objects. If a non-**NULL** value is passed in the *DeviceName* parameter, this value becomes the name of the control device object. The [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine can then call the [**IoCreateSymbolicLink**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatesymboliclink) routine, as shown in the preceding code example, to link the object's kernel-mode name to a user-mode name that is visible to applications.

The control device object is the only type of device object that can safely be named, because it's the only device object that isn't attached to a driver stack. Thus, control device objects for file system filter drivers can optionally be named. Control device objects for file systems must be named. Filter device objects should never be named.

The value that is assigned to the *DeviceType* parameter should be one of the device types that are defined in ntifs.h, such as FILE_DEVICE_DISK_FILE_SYSTEM.

If a non-NULL value is passed in the *DeviceName* parameter, the *DeviceCharacteristics* flags must include FILE_DEVICE_SECURE_OPEN. This flag directs the I/O Manager to perform security checks on all open requests that are sent to the control device object. These security checks are made against the ACL for the named device object.

An effective way for a file system filter driver to identify its own control device object in dispatch routines is to compare the device pointer and a previously stored global pointer to the control device object. Thus, the preceding sample stores the *DeviceObject* pointer that was returned by [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) into `gControlDeviceObject`, a globally defined pointer variable.
