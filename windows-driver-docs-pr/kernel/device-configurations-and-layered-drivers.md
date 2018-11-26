---
title: Device Configurations and Layered Drivers
description: For the most common kinds of devices, the Windows Driver Kit (WDK) supplies a sample set of fully functional system drivers.
ms.assetid: 1baaac5a-8eea-42df-bad6-fe620ac32a6c
keywords: ["WDM drivers WDK kernel , configurations", "WDM drivers WDK kernel , layered drivers", "layered drivers WDK kernel", "driver layers WDK WDM", "replacing drivers", "reusable drivers WDK WDM"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Device Configurations and Layered Drivers


For the most common kinds of devices, the Windows Driver Kit (WDK) supplies a sample set of fully functional system drivers. Individual sample drivers can be used as models when developing new drivers for similar kinds of devices. However, the system's drivers had an additional design requirement: to make it easy to develop new device drivers. Consequently, many of the system's drivers have a layered architecture so that certain drivers can be reused to support new drivers for similar devices.




In most cases, the WDK-supplied reusable drivers are WDM drivers that support PnP and handle hardware-independent operations for a system-supplied device-specific lowest-level (PnP bus) driver. In some cases, such as the parallel port and SCSI port drivers, these reusable drivers provide support for higher-level, device-type-specific class drivers. Note that none of the system's reusable drivers precludes the development of new intermediate drivers to be added to a chain of existing drivers.

Where a new (or replacement) driver fits in the chain of drivers for a device depends partly on the hardware configuration of devices in a given Windows platform, and partly on how much support a new driver can get from existing system drivers.

## In this section


-   [Sample Device and Driver Configuration](sample-device-and-driver-configuration.md)
-   [Points to Consider When Adding Drivers](points-to-consider-when-adding-drivers.md)

 

 




