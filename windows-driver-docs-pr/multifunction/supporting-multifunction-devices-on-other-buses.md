---
title: Supporting Multifunction Devices on Other Buses
description: Provides information about supporting multifunction devices on other buses.
keywords:
- multifunction devices WDK , other buses
- PnP WDK multifunction devices
- ISA WDK multifunction devices
- USB WDK multifunction devices
- IEEE 1394 WDK multifunction devices
ms.date: 03/17/2023
---

# Supporting Multifunction Devices On Other Buses

For a multifunction device on a PnP ISA, USB, or IEEE 1394 bus, the parent bus driver enumerates the individual functions if the device conforms to the bus standard.

For such a device, the parent bus driver manages the fact that there is more than one device residing at a single bus location. To the rest of the system, the individual functions operate like independent devices.

Vendors of this type of multifunction device must do the following:

- Ensure that the device conforms to the specification for the bus on which the device will reside.

- Provide a PnP function driver for each function of the device.

    Since the system-supplied bus driver handles the multifunction semantics, the function drivers can be the same drivers that are used when the functions are packaged as individual devices.

- Provide an INF file for each function of the device.

    The INF files can be the same files that are used when the functions are packaged as individual devices. The INF files do not need any special multifunction semantics.
