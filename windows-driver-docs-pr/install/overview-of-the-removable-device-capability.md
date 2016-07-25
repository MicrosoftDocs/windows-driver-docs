---
title: Overview of the Removable Device Capability
description: Overview of the Removable Device Capability
ms.assetid: c6dfb2ac-89a5-40fd-ae9a-1f2800af9ef8
---

# Overview of the Removable Device Capability


The removable device capability is a bit (**Removable**) that bus drivers set in the [**DEVICE\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff543095) structure in response to the [**IRP\_MN\_QUERY\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff551664) function code for a specified device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)).

Bus drivers set the removable device capability for a devnode when the devnode and all its child devnodes make up a device that can be physically removed, disconnected, or unplugged from its parent devnode while the computer is running. Typically, a devnode should be marked as removable if it is the topmost devnode in a devnode topology.

Setting the removable device capability correctly on a devnode is important. If a bus driver cannot provide a container ID for a devnode that it is enumerating, the Plug and Play (PnP) manager uses the removable device capability to generate a container ID for all devnodes enumerated for the device.

For example, suppose that a single-function device, such as a mouse, is connected to the computer through USB. In this case, the USB bus driver detects the new device, detects that it is a USB human interface device (HID), and creates a USB HID devnode for the device. The HID devnode also detects that the HID device is a mouse and creates a child devnode for a HID-compliant mouse. At this point, the mouse is installed and is functional on the computer. Both of the new devnodes use independent [*driver stacks*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-driver-stack).

As a general rule, the topmost (parent) devnode of the device should be set as removable, while each of its child devnodes should not be set as removable. In the previous example, the USB bus driver sets the **Removable** bit to **TRUE** for the USB HID devnode, and sets the **Removable** bit to **FALSE** for the child HID-compliant mouse devnode.

The following Device Manager screen shot shows the devnode topology for a generic USB mouse, and shows which devnodes of the mouse are marked as removable.

![screen shot of device manager window showing devnode topology for a usb mouse](images/containerid-2.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Overview%20of%20the%20Removable%20Device%20Capability%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




