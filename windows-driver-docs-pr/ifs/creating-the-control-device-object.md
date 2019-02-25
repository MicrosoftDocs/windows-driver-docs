---
title: Creating the Control Device Object
description: Creating the Control Device Object
ms.assetid: 9f89fd24-59b8-4529-b151-4e91e6334173
keywords:
- control device objects WDK file system
- CDOs WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating the Control Device Object


## <span id="ddk_creating_the_control_device_object_if"></span><span id="DDK_CREATING_THE_CONTROL_DEVICE_OBJECT_IF"></span>


A file system filter driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine usually begins by creating a *control device object*. The purpose of the control device object is to allow applications to communicate with the filter driver directly, even before the filter is attached to a file system or volume device object.

Note that file systems also create control device objects. When a file system filter driver attaches itself to a file system, rather than an individual file system volume, it does so by attaching itself to the file system's control device object.

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

Unlike file systems, file system filter drivers are not required to name their control device objects. A user mode application can not access the filter driver with out a device name since a call to [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549506) is not valid for control device objects. If a non-**NULL** value is passed in the *DeviceName* parameter, this value becomes the name of the control device object. The [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine can then call the [**IoCreateSymbolicLink**](https://msdn.microsoft.com/library/windows/hardware/ff549043) routine, as shown in the preceding code example, to link the object's kernel-mode name to a user-mode name that is visible to applications.

**Note**  The control device object is the only type of device object that can safely be named, because it is the only device object that is not attached to a driver stack. Thus, control device objects for file system filter drivers can optionally be named. Note that control device objects for file systems must be named. Filter device objects should never be named.

 

The value that is assigned to the *DeviceType* parameter should be one of the device types that are defined in ntifs.h, such as FILE\_DEVICE\_DISK\_FILE\_SYSTEM.

If a non-**NULL** value is passed in the *DeviceName* parameter, the *DeviceCharacteristics* flags must include FILE\_DEVICE\_SECURE\_OPEN. This flag directs the I/O Manager to perform security checks on all open requests that are sent to the control device object. These security checks are made against the ACL for the named device object.

An effective way for a file system filter driver to identify its own control device object in dispatch routines is to compare the device pointer and a previously stored global pointer to the control device object. Thus, the preceding sample stores the *DeviceObject* pointer that was returned by [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) into `gControlDeviceObject`, a globally defined pointer variable.

 

 




