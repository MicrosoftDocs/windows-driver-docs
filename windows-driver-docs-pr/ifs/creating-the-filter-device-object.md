---
title: Creating the Filter Device Object
author: windows-driver-content
description: Creating the Filter Device Object
ms.assetid: aca9a2ba-8630-4eb3-9312-a0c6454c3e44
keywords: ["filter drivers WDK file system , attaching filters", "file system filter drivers WDK , attaching filters", "attaching filters to file system or volume", "volumes WDK file system , attaching filters", "IoCreateDevice", "filter DOs WDK file system"]
---

# Creating the Filter Device Object


## <span id="ddk_creating_the_filter_device_object_if"></span><span id="DDK_CREATING_THE_FILTER_DEVICE_OBJECT_IF"></span>


Call [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397) to create a filter device object to attach to a volume or file system stack, as in the following example:

```
status = IoCreateDevice(
          gFileSpyDriverObject,                     //DriverObject
          sizeof(MYLEGACYFILTER_DEVICE_EXTENSION),  //DeviceExtensionSize
          NULL,                                     //DeviceName
          DeviceObject->DeviceType,                 //DeviceType
          0,                                        //DeviceCharacteristics
          FALSE,                                    //Exclusive
          &amp;newDeviceObject);                        //DeviceObject
```

In the above code snippet, *DeviceObject* is a pointer to the target device object to which the filter device object will be attached; *newDeviceObject* is a pointer to the filter device object itself.

Setting the *DeviceExtensionSize* parameter to **sizeof**(MYLEGACYFILTER\_DEVICE\_EXTENSION) causes a MYLEGACYFILTER\_DEVICE\_EXTENSION structure to be allocated for the filter device object. The newly created filter device object's **DeviceExtension** member is set to point to this structure. File system filter drivers usually define and allocate memory for a device extension for each filter device object. The structure and contents of the device extension are driver-specific. However, on Microsoft Windows XP and later, filter drivers should define a DEVICE\_EXTENSION structure for filter driver objects that contains at least the following member:

```
PDEVICE_OBJECT AttachedToDeviceObject;
```

In the above call to [**IoCreateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff548397), setting the *DeviceName* parameter to **NULL** specifies that the filter device object will not be named. Filter device objects are never named. Because a filter device object is attached to a file system or volume driver stack, assigning a name to the filter device object would create a system security hole.

The *DeviceType* parameter must always be set to the same device type as that of the target (file system or filter) device object to which the filter device object is being attached. It is important to propagate the device type in this way, because it is used by the I/O Manager and can be reported back to applications.

**Note**  File systems and file system filter drivers should never set the *DeviceType* parameter to FILE\_DEVICE\_FILE\_SYSTEM. This is not a valid value for this parameter. (The FILE\_DEVICE\_FILE\_SYSTEM constant is intended only for use in defining FSCTL codes.)

 

Another reason why the *DeviceType* parameter is important is that many filters attach only to certain types of file systems. For example, a particular filter may attach to all local disk file systems, but not to CD-ROM file systems or remote file systems. Such filters determine the type of file system by examining the device type of the topmost device object in the file system or volume driver stack. In most cases, the topmost device object in the stack is a filter device object. Thus it is essential that all attached filter device objects have the same device type as that of the underlying file system or volume device object.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Creating%20the%20Filter%20Device%20Object%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


