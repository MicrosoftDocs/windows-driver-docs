---
title: Overview of Removable Device Capability
description: Overview of the removable device capability
ms.date: 04/08/2022
---

# Overview of removable device capability

Removable device capability is a bit (**Removable**) that [bus drivers](../kernel/bus-drivers.md) set in the [**DEVICE_CAPABILITIES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_capabilities) structure in response to the [**IRP_MN_QUERY_CAPABILITIES**](../kernel/irp-mn-query-capabilities.md) function code for a specified device node (*devnode*).

Bus drivers set the removable device capability for a devnode when the devnode and all its child devnodes make up a device that can be physically removed, disconnected, or unplugged from its parent devnode while the computer is running. Typically, a devnode should be marked as removable if it is the topmost devnode in a devnode topology.

Setting the removable device capability correctly on a devnode is important. If a bus driver cannot provide a container ID for a devnode that it is enumerating, the Plug and Play (PnP) manager uses the removable device capability to generate a container ID for all devnodes enumerated for the device.

For example, suppose that a single-function device, such as a mouse, is connected to the computer through USB. In this case, the USB bus driver detects the new device, detects that it is a USB human interface device (HID), and creates a USB HID devnode for the device. The HID devnode also detects that the HID device is a mouse and creates a child devnode for a HID-compliant mouse. At this point, the mouse is installed and is functional on the computer. Both of the new devnodes use independent *driver stacks*.

As a general rule, the topmost (parent) devnode of the device should be set as removable, while each of its child devnodes should not be set as removable. In the previous example, the USB bus driver sets the **Removable** bit to **TRUE** for the USB HID devnode, and sets the **Removable** bit to **FALSE** for the child HID-compliant mouse devnode.

The following Device Manager screen shot shows the devnode topology for a generic USB mouse, and shows which devnodes of the mouse are marked as removable.

![screen shot of device manager window showing devnode topology for a usb mouse.](images/containerid-2.png)
