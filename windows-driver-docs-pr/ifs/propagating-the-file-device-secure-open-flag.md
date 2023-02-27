---
title: Propagating the FILE_DEVICE_SECURE_OPEN Flag
description: Propagating the FILE_DEVICE_SECURE_OPEN Flag
keywords:
- filter drivers WDK file system , attaching filters
- file system filter drivers WDK , attaching filters
- attaching filters to file system or volume
- volumes WDK file system , attaching filters
- FILE_DEVICE_SECURE_OPEN
- propagating FILE_DEVICE_SECURE_OPEN flag
ms.date: 02/23/2023
---

# Propagating the FILE_DEVICE_SECURE_OPEN Flag

> [!NOTE]
> For optimal reliability and performance, use [file system minifilter drivers](./filter-manager-concepts.md) with Filter Manager support instead of legacy file system filter drivers. To port your legacy driver to a minifilter driver, see [Guidelines for Porting Legacy Filter Drivers](guidelines-for-porting-legacy-filter-drivers.md).

After attaching a legacy filter device object to a file system (but not to a volume), always set the FILE_DEVICE_SECURE_OPEN flag on the filter device object such that it matches the value of the next-lower device object on the driver stack. For more information about this flag, see [Specifying Device Characteristics](../kernel/specifying-device-characteristics.md) and [**DEVICE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object). An example follows, where **DeviceObject** is a pointer to the device object to which the filter device object has been attached; **myLegacyFilterDeviceObject** is a pointer to the filter device object itself.

```cpp
if (FlagOn( DeviceObject->Characteristics, FILE_DEVICE_SECURE_OPEN )) {
    SetFlag(myLegacyFilterDeviceObject->Characteristics, FILE_DEVICE_SECURE_OPEN );
}
```
