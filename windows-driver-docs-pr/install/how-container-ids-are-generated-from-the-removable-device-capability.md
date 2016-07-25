---
title: How Container IDs are Generated from the Removable Device Capability
description: How Container IDs are Generated from the Removable Device Capability
ms.assetid: 493a9473-4989-4557-b2b2-efa0e2a8b24e
---

# How Container IDs are Generated from the Removable Device Capability


If a bus driver cannot provide a container ID for a device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) that it is enumerating, the Plug and Play (PnP) manager uses the removable device capability to generate a container ID for all devnodes enumerated for the device. For more information about the removable device capability, see [Overview of the Removable Device Capability](overview-of-the-removable-device-capability.md).

The following heuristic describes how Container IDs are generated from the removable device capability:

1.  If the devnode has the removable device capability set to **TRUE**, generate a new container ID for the devnode.

2.  If the devnode has the removable device capability set to **FALSE**, inherit the container ID from its parent devnode.

A devnode cannot enumerate child devnodes until it is initialized and its [*driver stack*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-stack) is started. As soon as its container ID is assigned during initialization, the devnode is ready to propagate its container ID down to any of its nonremovable children as they are enumerated.

A devnode with the removable device capability set to **TRUE** is considered the topmost (parent) devnode for the device, and a container ID is generated for this devnode.

All the children of this parent devnode inherit the same container ID unless they themselves have their removable device capability set to **TRUE**. In this case, a removable child devnode is assigned a different container ID and becomes the parent devnode of this removable device. All the children of that devnode inherit the same container ID.

For example, suppose that a single-function mouse is connected to the computer through USB. In this case, the USB bus driver detects a new device and detects that it is a USB human interface device (HID). The USB bus driver then creates a USB HID devnode for the device. The HID devnode also detects that the HID device is a mouse and creates a child devnode for a HID-compliant mouse

Applying this heuristic to this example results in the following actions:

1.  The USB HID devnode is created. The removable device capability is set to **TRUE** on this devnode because its parent USB hub devnode recognized that it was plugged into an external-facing USB port.

2.  A container ID is created for this devnode because it is the topmost devnode of a removable device. As a result, this devnode is considered the parent devnode for the removable device.

3.  The HID-compliant mouse devnode is created. The removable device capability is set to **FALSE** on this devnode because its parent USB HID devnode reports all its children as nonremovable. In this case, the HID-compliant mouse devnode inherits the container ID of the parent devnode.

Through this heuristic, the same container ID is assigned to each devnode that belongs to the mouse. The PnP manager successfully grouped the devnodes into a logical device, even when there is no unique identifier for the device.

**Note**  The success of this heuristic relies on a specific bus driver that correctly reports the removable device capability for each devnode that it enumerates. The bus driver must ensure that the parent devnode of the device should be set as removable, and its child devnodes should not be set as removable.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20How%20Container%20IDs%20are%20Generated%20from%20the%20Removable%20Device%20Capability%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




