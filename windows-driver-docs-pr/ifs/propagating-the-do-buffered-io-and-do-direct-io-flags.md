---
title: Propagating the DO_BUFFERED_IO and DO_DIRECT_IO Flags
description: Propagating the DO_BUFFERED_IO and DO_DIRECT_IO Flags
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
- DO_BUFFERED_IO
- propagating DO_BUFFERED_IO flag
- DO_DIRECT_IO
- propagating DO_DIRECT_IO flag
ms.date: 02/23/2023
---

# Propagating the DO_BUFFERED_IO and DO_DIRECT_IO Flags

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

After attaching a legacy filter device object to a file system or volume, always set or clear the DO_BUFFERED_IO and DO_DIRECT_IO flags as needed so that they match the values of the next-lower device object on the driver stack. For more information about these flags, see [Methods for Accessing Data Buffers](../kernel/methods-for-accessing-data-buffers.md). The following code snippet shows an example, where **DeviceObject** is a pointer to the device object to which the filter device object has been attached and **myLegacyFilterDeviceObject** is a pointer to the filter device object itself.

```cpp
if (FlagOn( DeviceObject->Flags, DO_BUFFERED_IO )) {
    SetFlag( myLegacyFilterDeviceObject->Flags, DO_BUFFERED_IO );
}
if (FlagOn( DeviceObject->Flags, DO_DIRECT_IO )) {
    SetFlag(myLegacyFilterDeviceObject->Flags, DO_DIRECT_IO );
}
```
