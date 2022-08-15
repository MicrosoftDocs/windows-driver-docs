---
title: Device instance ID
description: A device instance ID is a system-supplied device identification string that uniquely identifies a device in the system.
ms.date: 04/08/2022
---

# Device instance ID

A device instance ID is a system-supplied device identification string that uniquely identifies a device in the system. The Plug and Play (PnP) manager assigns a device instance ID to each device node (*devnode*) in a system's [device tree](../kernel/device-tree.md).

The creation of the device instance ID for a device uses the [bus driver](../kernel/bus-drivers.md) reported [device ID](device-ids.md) value, [instance ID](instance-ids.md) value, and the **UniqueID** member of the [**DEVICE_CAPABILITIES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities) structure as input in order to create the unique device instance ID for this device on the system.

The number of characters of a device instance ID, excluding a NULL-terminator, must be less than `MAX_DEVICE_ID_LEN`. A device instance ID is persistent across system restarts.

The following is an example of an instance ID ("1&08") concatenated to a device ID for a PCI device:

`PCI\VEN_1000&DEV_0001&SUBSYS_00000000&REV_02\1&08`
