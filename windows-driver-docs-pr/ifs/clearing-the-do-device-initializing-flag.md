---
title: Clearing the DO_DEVICE_INITIALIZING Flag
description: Clearing the DO_DEVICE_INITIALIZING Flag
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
- DO_DEVICE_INITIALIZING
ms.date: 02/23/2023
---

# Clearing the DO_DEVICE_INITIALIZING Flag

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

After attaching a legacy filter device object to a file system or volume, always be sure to clear the DO_DEVICE_INITIALIZING flag on the filter device object. (For more information about this flag, see [**DEVICE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) in the Kernel Reference.) The following example shows how to use the **ClearFlag** macro defined in *ntifs.h* to do so:

```cpp
ClearFlag(NewDeviceObject->Flags, DO_DEVICE_INITIALIZING);
```

When the filter device object is created, [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) sets the DO_DEVICE_INITIALIZING flag on the device object. After the filter is successfully attached, this flag must be cleared. If this flag isn't cleared, no more filter drivers can attach to the filter chain because the call to [**IoAttachDeviceToDeviceStackSafe**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioattachdevicetodevicestacksafe) will fail.

It isn't necessary to clear the DO_DEVICE_INITIALIZING flag on device objects that are created in **DriverEntry**, because the I/O Manager automatically clears it. However, your driver should clear this flag on all other device objects that it creates.
