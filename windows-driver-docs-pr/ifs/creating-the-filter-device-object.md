---
title: Creating the Filter Device Object
description: Creating the Filter Device Object
ms.assetid: aca9a2ba-8630-4eb3-9312-a0c6454c3e44
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
- IoCreateDevice
- filter DOs WDK file system
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating the Filter Device Object


## <span id="ddk_creating_the_filter_device_object_if"></span><span id="DDK_CREATING_THE_FILTER_DEVICE_OBJECT_IF"></span>


Call [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) to create a filter device object to attach to a volume or file system stack, as in the following example:

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

In the above code snippet, *DeviceObject* is a pointer to the target device object to which the filter device object will be attached; *newDeviceObject* is a pointer to the filter device object itself.

Setting the *DeviceExtensionSize* parameter to **sizeof**(MYLEGACYFILTER\_DEVICE\_EXTENSION) causes a MYLEGACYFILTER\_DEVICE\_EXTENSION structure to be allocated for the filter device object. The newly created filter device object's **DeviceExtension** member is set to point to this structure. File system filter drivers usually define and allocate memory for a device extension for each filter device object. The structure and contents of the device extension are driver-specific. However, on Microsoft Windows XP and later, filter drivers should define a DEVICE\_EXTENSION structure for filter driver objects that contains at least the following member:

```cpp
PDEVICE_OBJECT AttachedToDeviceObject;
```

In the above call to [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397), setting the *DeviceName* parameter to **NULL** specifies that the filter device object will not be named. Filter device objects are never named. Because a filter device object is attached to a file system or volume driver stack, assigning a name to the filter device object would create a system security hole.

The *DeviceType* parameter must always be set to the same device type as that of the target (file system or filter) device object to which the filter device object is being attached. It is important to propagate the device type in this way, because it is used by the I/O Manager and can be reported back to applications.

**Note**  File systems and file system filter drivers should never set the *DeviceType* parameter to FILE\_DEVICE\_FILE\_SYSTEM. This is not a valid value for this parameter. (The FILE\_DEVICE\_FILE\_SYSTEM constant is intended only for use in defining FSCTL codes.)

 

Another reason why the *DeviceType* parameter is important is that many filters attach only to certain types of file systems. For example, a particular filter may attach to all local disk file systems, but not to CD-ROM file systems or remote file systems. Such filters determine the type of file system by examining the device type of the topmost device object in the file system or volume driver stack. In most cases, the topmost device object in the stack is a filter device object. Thus it is essential that all attached filter device objects have the same device type as that of the underlying file system or volume device object.

 

 




