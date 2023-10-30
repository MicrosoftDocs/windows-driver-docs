---
title: Creating the Filter Device Object
description: Creating the Filter Device Object
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
- IoCreateDevice
- filter DOs WDK file system
ms.date: 02/23/2023
---

# Creating the Filter Device Object

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A legacy file system filter driver calls [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) to create a filter device object to attach to a volume or file system stack, as in the following example:

```cpp
status = IoCreateDevice(
          gFileSpyDriverObject,                     //DriverObject
          sizeof(MYLEGACYFILTER_DEVICE_EXTENSION),  //DeviceExtensionSize
          NULL,                                     //DeviceName
          DeviceObject->DeviceType,                 //DeviceType
          0,                                        //DeviceCharacteristics
          FALSE,                                    //Exclusive
          &newDeviceObject);                        //DeviceObject
```

In this code snippet, **DeviceObject** is a pointer to the target device object to which the filter device object will be attached; **newDeviceObject** is a pointer to the filter device object itself.

Setting the **DeviceExtensionSize** parameter to **sizeof**(MYLEGACYFILTER_DEVICE_EXTENSION) causes a MYLEGACYFILTER_DEVICE_EXTENSION structure to be allocated for the filter device object. The newly created filter device object's **DeviceExtension** member is set to point to this structure. File system filter drivers usually define and allocate memory for a device extension for each filter device object. The structure and contents of the device extension are driver-specific. However, on Windows XP and later, filter drivers should define a DEVICE_EXTENSION structure for filter driver objects that contains at least the following member:

```cpp
PDEVICE_OBJECT AttachedToDeviceObject;
```

In the above call to [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice), setting the **DeviceName** parameter to **NULL** specifies that the filter device object shouldn't be named. Filter device objects are never named. Because a filter device object is attached to a file system or volume driver stack, assigning a name to the filter device object would create a system security hole.

The **DeviceType** parameter must always be set to the same device type as the target's (file system or filter) device object to which the filter device object is being attached. It's important to propagate the device type in this way, because it's used by the I/O Manager and can be reported back to applications.

File systems and file system filter drivers should never set the **DeviceType** parameter to FILE_DEVICE_FILE_SYSTEM. This value isn't valid for this parameter. (The FILE_DEVICE_FILE_SYSTEM constant is intended only for use in defining FSCTL codes.)

Another reason why the **DeviceType** parameter is important is that many filters attach only to certain types of file systems. For example, a particular filter may attach to all local disk file systems, but not to CD-ROM file systems or remote file systems. Such filters determine the type of file system by examining the device type of the topmost device object in the file system or volume driver stack. In most cases, the topmost device object in the stack is a filter device object. Thus it's essential that all attached filter device objects have the same device type as the underlying file system or volume device object.
