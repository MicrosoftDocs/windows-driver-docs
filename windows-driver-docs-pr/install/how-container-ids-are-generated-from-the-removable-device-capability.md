---
title: How Container IDs are Generated from Removable Device Capability
description: Describes how container IDs are generated from removable device capability
ms.date: 04/08/2022
---

# How Container IDs are generated from removable device capability

If a [bus driver](../kernel/bus-drivers.md) cannot provide a container ID for a device node (*devnode*) that it is enumerating, the Plug and Play (PnP) manager uses the removable device capability to generate a container ID for all devnodes enumerated for the device. For more information about the removable device capability, see [Overview of the Removable Device Capability](overview-of-the-removable-device-capability.md).

The following heuristic describes how Container IDs are generated from the removable device capability:

1. If the devnode has the removable device capability set to **TRUE**, generate a new container ID for the devnode.

1. If the devnode has the removable device capability set to **FALSE**, inherit the container ID from its parent devnode.

A devnode cannot enumerate child devnodes until it is initialized and its *driver stack* is started. As soon as its container ID is assigned during initialization, the devnode is ready to propagate its container ID down to any of its non-removable children as they are enumerated.

A devnode with the removable device capability set to **TRUE** is considered the topmost (parent) devnode for the device, and a container ID is generated for this devnode.

All the children of this parent devnode inherit the same container ID unless they themselves have their removable device capability set to **TRUE**. In this case, a removable child devnode is assigned a different container ID and becomes the parent devnode of this removable device. All the children of that devnode inherit the same container ID.

For example, suppose that a single-function mouse is connected to the computer through USB. In this case, the USB bus driver detects a new device and detects that it is a USB human interface device (HID). The USB bus driver then creates a USB HID devnode for the device. The HID devnode also detects that the HID device is a mouse and creates a child devnode for a HID-compliant mouse

Applying this heuristic to this example results in the following actions:

1. The USB HID devnode is created. The removable device capability is set to **TRUE** on this devnode because its parent USB hub devnode recognized that it was plugged into an external-facing USB port.

1. A container ID is created for this devnode because it is the topmost devnode of a removable device. As a result, this devnode is considered the parent devnode for the removable device.

1. The HID-compliant mouse devnode is created. The removable device capability is set to **FALSE** on this devnode because its parent USB HID devnode reports all its children as nonremovable. In this case, the HID-compliant mouse devnode inherits the container ID of the parent devnode.

Through this heuristic, the same container ID is assigned to each devnode that belongs to the mouse. The PnP manager successfully grouped the devnodes into a logical device, even when there is no unique identifier for the device.

> [!NOTE]
> The success of this heuristic relies on a specific bus driver that correctly reports the removable device capability for each devnode that it enumerates. The bus driver must ensure that the parent devnode of the device should be set as removable, and its child devnodes should not be set as removable.
