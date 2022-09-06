---
title: Install a null driver
description: Provides information about how to install a null driver.
keywords:
- Device setup WDK device installations, null drivers
- device installations WDK, null drivers
- install devices WDK, null drivers
- null drivers WDK device installations
- nonexistent drivers WDK device installations
ms.date: 08/29/2022
---

# Install a null driver

You might install a "null driver" (that is, nonexistent driver) for a device if the device is not used on the machine and should not be started or is capable of executing in *raw mode* (see *RawDeviceOK* in the [DEVICE_CAPABILITIES structure](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities)). To specify a null driver in an INF file, use entries like the following:

```inf
[MyModels]
%MyDeviceDescription% = MyNullInstallSection, ExampleHardwareId

[MyNullInstallSection]
; The install section is typically empty, but can contain entries that
; copy files or modify the registry.

[MyNullInstallSection.Services]
AddService = ,2    ; no value for the service name
```

The hardware ID for the device in the *Models* section should identify the device specifically, using the subsystem vendor ID and whatever other information is relevant.

The operating system will create a device node (*devnode*) for the device, but if the device is not capable of executing in raw mode, the operating system will not start the device because a function driver has not been assigned to it. Note, however, that if the device has a [boot configuration](../kernel/hardware-resources.md#logical-configuration-types-for-resource-lists), those resources will be reserved.
