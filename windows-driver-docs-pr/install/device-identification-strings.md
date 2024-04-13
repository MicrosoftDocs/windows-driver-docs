---
title: Device Identification Strings
description: The Plug and Play (PnP) manager and other device installation components use device identification strings to identify devices that are installed in a computer.
keywords:
- compatible IDs WDK device installations
- device IDs WDK device installations
- device instance IDs WDK device installations
- driver nodes WDK device installations
- hardware IDs WDK device installations
- instance IDs WDK device installations
- Device setup WDK device installations , device identification strings
- device installations WDK , device identification strings
- installing devices WDK , device identification strings
ms.date: 04/08/2022
---

# Device identification strings

> [!NOTE]
> Device identification strings should not be parsed. They are meant only for string comparisons and should be treated as opaque strings.

The Plug and Play (PnP) manager and other [device installation components](./overview-of-device-and-driver-installation.md) use device identification strings to identify devices that are installed in a computer.

Windows uses the following device identification strings to locate the [driver package](driver-packages.md) that best matches the device. These identification strings are reported by a device's enumerator, a system component that discovers PnP devices based on a PnP hardware standard. These tasks are carried out by [PnP Bus Drivers](../kernel/bus-drivers.md) in partnership with the PnP manager. A device is typically enumerated by its parent bus driver, such as the PCI or PCMCIA bus driver. Some devices are enumerated by a bus filter driver, such as the ACPI Driver.

- [Hardware IDs](hardware-ids.md)

- [Compatible IDs](compatible-ids.md)

Windows tries to find a match for one of the hardware IDs or compatible IDs. For more information about how Windows uses these IDs to match a device to a driver package, and how to specify IDs in an INF file, see [How Windows Selects Drivers](./how-windows-selects-a-driver-for-a-device.md).

In addition to using the preceding IDs to identify devices, the PnP manager uses the following IDs to uniquely identify instances of each device that are installed in a computer:

- [Instance IDs](instance-ids.md)

- [Device instance IDs](device-instance-ids.md)

Starting with Windows 7, the PnP manager uses the [Container ID](container-ids.md) device identification string to group one or more device nodes (devnodes) that were enumerated from each instance of a physical device installed in a computer.

Each enumerator customizes its device IDs, hardware IDs, and compatible IDs to uniquely identify the devices that it enumerates. In addition, each enumerator has its own policy to identify hardware IDs and compatible IDs. For more information about hardware ID and compatible ID formats for most of the system buses, see [Device Identifier Formats](./generic-identifiers.md).
