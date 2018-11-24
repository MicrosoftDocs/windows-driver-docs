---
title: Installing a Null Driver
description: Installing a Null Driver
ms.assetid: 8684eade-3f25-48fe-94e7-a7e76d8072ad
keywords:
- Device setup WDK device installations , null drivers
- device installations WDK , null drivers
- installing devices WDK , null drivers
- null drivers WDK device installations
- nonexistent drivers WDK device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing a Null Driver





You might install a "null driver" (that is, nonexistent driver) for a device if the device is not used on the machine and should not be started. Such devices do not typically exist on a machine, but if they do, you can install a null driver. Additionally, the system installs null drivers for devices that do not have a [function driver](https://msdn.microsoft.com/library/windows/hardware/ff546516), if they are capable of executing in [*raw mode*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raw-mode).

To specify a null driver in an INF file, use entries like the following:

```cpp
:
[MyModels]
%MyDeviceDescription% = MyNullInstallSection, &BadDeviceHardwareID%
:

[MyNullInstallSection]
; The install section is typically empty, but can contain entries that
; copy files or modify the registry.

[MyNullInstallSection.Services]
AddService = ,2    ; no value for the service name
:
```

The hardware ID for the device in the *Models* section should identify the device specifically, using the subsystem vendor ID and whatever other information is relevant.

The operating system will create a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) for the device, but if the device is not capable of executing in raw mode, the operating system will not start the device because a function driver has not been assigned to it. Note, however, that if the device has a [boot configuration](https://msdn.microsoft.com/library/windows/hardware/ff547012#logical-configuration-types-for-resource-lists), those resources will be reserved.

 

 





