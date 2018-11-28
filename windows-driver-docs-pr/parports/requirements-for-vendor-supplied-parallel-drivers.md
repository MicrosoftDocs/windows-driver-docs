---
title: Requirements for Vendor-Supplied Parallel Drivers
description: Requirements for Vendor-Supplied Parallel Drivers
ms.assetid: 2194ad1a-3548-4b67-9268-4245389cf264
keywords:
- vendor-supplied parallel drivers WDK , about vendor-supplied parallel drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements for Vendor-Supplied Parallel Drivers





This section describes Microsoft Windows requirements for vendor-supplied drivers for parallel ports and devices attached to parallel ports.

Vendor-supplied function drivers and bus drivers for parallel ports are not required because the [system-supplied parallel drivers](system-supplied-parallel-drivers.md) provide these functions. The system-supplied parallel drivers provide extensive support for operating parallel ports and devices attached to parallel ports.

Vendor-supplied function drivers for parallel devices attached to parallel ports are optional. The system-supplied parallel drivers provide extensive support for directly controlling a parallel device as a raw device, and for operating a device's parent parallel port.

If a vendor provides a function driver for a parallel device, the driver must support Plug and Play and power management. Microsoft recommends that the driver be a WDM driver.

The following topics describe how a vendor-supplied function driver for a parallel device operates a device and the device's parent parallel port:

[Operating a Parallel Port](operating-a-parallel-port.md)

[Operating a Parallel Device Attached to a Parallel Port](operating-a-parallel-device-attached-to-a-parallel-port.md)

 

 




