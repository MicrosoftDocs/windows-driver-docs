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
ms.date: 04/20/2017
---

# Propagating the FILE\_DEVICE\_SECURE\_OPEN Flag


## <span id="ddk_clearing_the_do_device_initializing_flag_if"></span><span id="DDK_CLEARING_THE_DO_DEVICE_INITIALIZING_FLAG_IF"></span>


After attaching a filter device object to a file system (but not to a volume), always be sure to set the FILE\_DEVICE\_SECURE\_OPEN flag on the filter device object as needed to so that it matches the value of the next-lower device object on the driver stack. (For more information about this flag, see [Specifying Device Characteristics](../kernel/specifying-device-characteristics.md) in the Kernel Architecture Design Guide and [**DEVICE\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) in the Kernel Reference.) An example of this follows:

```cpp
if (FlagOn( DeviceObject->Characteristics, FILE_DEVICE_SECURE_OPEN )) {
    SetFlag(myLegacyFilterDeviceObject->Characteristics, FILE_DEVICE_SECURE_OPEN );
}
```

In the above code snippet, *DeviceObject* is a pointer to the device object to which the filter device object has just been attached; myLegacyFilter *DeviceObject* is a pointer to the filter device object itself.

 

