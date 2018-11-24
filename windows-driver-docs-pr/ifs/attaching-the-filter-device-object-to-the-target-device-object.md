---
title: Attaching the Filter Device Object to the Target Device Object
description: Attaching the Filter Device Object to the Target Device Object
ms.assetid: 1df293db-417a-4fee-afb8-06ab527331fb
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching the Filter Device Object to the Target Device Object


## <span id="ddk_attaching_the_filter_device_object_to_the_target_device_object_if"></span><span id="DDK_ATTACHING_THE_FILTER_DEVICE_OBJECT_TO_THE_TARGET_DEVICE_OBJECT_IF"></span>


Call [**IoAttachDeviceToDeviceStackSafe**](https://msdn.microsoft.com/library/windows/hardware/ff548236) to attach the filter device object to the filter driver stack for the target file system or volume.

```cpp
devExt = myLegacyFilterDeviceObject->DeviceExtension;

status = IoAttachDeviceToDeviceStackSafe(
           myLegacyFilterDeviceObject,        //SourceDevice
           DeviceObject,                      //TargetDevice
           &devext->AttachedToDeviceObject);  //AttachedToDeviceObject
```

Note that the device object pointer received by the *AttachedToDeviceObject* output parameter can differ from *TargetDevice* if any other filters were already chained above the device object that is pointed to by *TargetDevice*.

### <span id="Attaching_to_a_File_System_by_Name"></span><span id="attaching_to_a_file_system_by_name"></span><span id="ATTACHING_TO_A_FILE_SYSTEM_BY_NAME"></span>Attaching to a File System by Name

Every file system is required to create one or more named control device objects. To attach to a particular file system directly, a file system filter driver passes the name of the appropriate file system control device object to [**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198) to get a device object pointer. The following code snippet shows how to get such a pointer to one of the two control device objects for the RAW file system:

```cpp
RtlInitUnicodeString(&nameString, L"\\Device\\RawDisk");

status = IoGetDeviceObjectPointer(
            &nameString,                    //ObjectName
            FILE_READ_ATTRIBUTES,           //DesiredAccess
            &fileObject,                    //FileObject
            &rawDeviceObject);              //DeviceObject

if (NT_SUCCESS(status)) {
            ObDereferenceObject(fileObject);
}
```

If the call to [**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198) succeeds, the file system filter driver can then call [**IoAttachDeviceToDeviceStackSafe**](https://msdn.microsoft.com/library/windows/hardware/ff548236) to attach to the returned control device object.

**Note**   In addition to the control device object pointer (*rawDeviceObject*), [**IoGetDeviceObjectPointer**](https://msdn.microsoft.com/library/windows/hardware/ff549198) returns a pointer to a file object (*fileObject*) that represents the device object in user mode. In the code snippet above, the file object is not needed, so it is closed by calling [**ObDereferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff557724). It is important to note that decrementing the reference count on the file object returned by **IoGetDeviceObjectPointer** causes the reference count on the device object to be decremented as well. Thus the *fileObject* and *rawDeviceObject* pointers should both be considered invalid after the above call to **ObDereferenceObject**, unless the reference count on the device object is incremented by an additional call to [**ObReferenceObject**](https://msdn.microsoft.com/library/windows/hardware/ff558678) before **ObDereferenceObject** is called for the file object.

 

 

 




