---
title: Attaching the Filter Device Object to the Target Device Object
description: Attaching the Filter Device Object to the Target Device Object
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
ms.date: 02/23/2023
---

# Attaching the Filter Device Object to the Target Device Object

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

A legacy file system filter driver calls [**IoAttachDeviceToDeviceStackSafe**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioattachdevicetodevicestacksafe) to attach the filter device object to the filter driver stack for the target file system or volume.

```cpp
devExt = myLegacyFilterDeviceObject->DeviceExtension;

status = IoAttachDeviceToDeviceStackSafe(
           myLegacyFilterDeviceObject,        //SourceDevice
           DeviceObject,                      //TargetDevice
           &devext->AttachedToDeviceObject);  //AttachedToDeviceObject
```

The device object pointer received by the **AttachedToDeviceObject** output parameter can differ from **TargetDevice** if any other filters were already chained above the device object that is pointed to by *(TargetDevice)*.

## Attaching to a File System by Name

Every file system is required to create one or more named control device objects. To attach to a particular file system directly, a file system filter driver passes the name of the appropriate file system control device object to [**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer) to get a device object pointer. The following code snippet shows how to get such a pointer to one of the two control device objects for the RAW file system:

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

If the call to [**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer) succeeds, the file system filter driver can then call [**IoAttachDeviceToDeviceStackSafe**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioattachdevicetodevicestacksafe) to attach to the returned control device object.

In addition to the control device object pointer (**rawDeviceObject**), [**IoGetDeviceObjectPointer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdeviceobjectpointer) returns a pointer to a file object (**fileObject**) that represents the device object in user mode. In the code snippet, the file object isn't needed, so it's closed by calling [**ObDereferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obdereferenceobject). It's important to note that decrementing the reference count on the file object returned by **IoGetDeviceObjectPointer** causes the reference count on the device object to be decremented as well. Thus the **fileObject** and **rawDeviceObject** pointers should both be considered invalid after the above call to **ObDereferenceObject**, unless the reference count on the device object is incremented by another call to [**ObReferenceObject**](/windows-hardware/drivers/ddi/wdm/nf-wdm-obfreferenceobject) before **ObDereferenceObject** is called for the file object.
