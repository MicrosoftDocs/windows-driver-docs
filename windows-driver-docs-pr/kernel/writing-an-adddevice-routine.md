---
title: Writing an AddDevice Routine
description: Writing an AddDevice Routine
ms.assetid: 93a272f4-888c-4cc8-b013-c6313c10a8d8
keywords: ["standard driver routines WDK kernel , AddDevice routines", "driver routines WDK kernel , AddDevice routines", "routines WDK kernel , AddDevice routines", "AddDevice routines WDK kernel", "system-space memory allocations WDK kernel", "system resource storage WDK kernel", "storing system resources", "device objects WDK kernel , creating", "device initialization WDK kernel", "initializing devices", "AddDevice routines WDK kernel , about AddDevice routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Writing an AddDevice Routine





Any driver that supports PnP must have an [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine. The *AddDevice* routine creates one or more device objects representing the physical, logical, or virtual devices for which the driver carries out I/O requests. It also attaches the device object to the device stack, so the device stack will contain a device object for each driver associated with the device.

The PnP manager calls a driver's *AddDevice* routine for each device controlled by the driver. *AddDevice* routines are called during system initialization (when devices are first enumerated), and any time a new device is enumerated while the system is running.

This section contains the following topics:

[AddDevice Routines in Function or Filter Drivers](adddevice-routines-in-function-or-filter-drivers.md)

[AddDevice Routines in Bus Drivers](adddevice-routines-in-bus-drivers.md)

[Guidelines for Writing AddDevice Routines](guidelines-for-writing-adddevice-routines.md)

 

 




