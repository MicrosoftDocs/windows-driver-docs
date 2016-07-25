---
title: Troubleshooting the Implementation of Container IDs
description: Troubleshooting the Implementation of Container IDs
ms.assetid: 9c992f5a-73b6-4567-977f-1cd92862bf60
keywords: ["container IDs WDK , troubleshooting"]
---

# Troubleshooting the Implementation of Container IDs


If more than one instance of a device in the Devices and Printers user interface (UI) appears when you expect only one, the device does not correctly implement the container ID requirements. This incorrect implementation causes the Plug and Play (PnP) manager to group one or more device nodes ([*devnodes*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) into additional device containers for the device.

In such a case, you should examine the following:

-   Is the removable device capability set correctly for each devnode that is enumerated for the device?

    This is the most common cause of multiple device instances in the Devices and Printers UI. Make sure that each devnode for the device has the removable device capability set appropriately. The top-most, or *parent*, devnode of the device should be reported as removable, and all its children should be reported as not removable. Custom bus driver implementations must correctly assign the removable relationship for devnodes that they enumerate.

    Device Manager is a valuable tool to diagnose these issues. You can examine the complete devnode hierarchy by following these steps:

    1.  Right-click the **My Computer** icon, and then click **Manage** . and select **Device Manager** from the System Tools listed in the resulting display.
    2.  Click **View by connection** from the drop-down menu.
    3.  Locate the devnodes that make up your device. For each devnode, right-click the node, and then click **Properties.**
    4.  On the **Details** tab, in the **Properties** drop-down list, click **Capabilities**.

    If the list of capability values for the devnode contains the CM\_DEVCAP\_REMOVABLE flag, the devnode is marked as removable. The Plug and Play (PnP) manager then creates a new device container for the devnode and its children that cannot be removed.

    For more information about the removable device capability, see [Container IDs Generated from the Removable Device Capability](container-ids-generated-from-the-removable-device-capability.md).

    For more information about Device Manager, see [Using Device Manager](using-device-manager.md).

-   Does the device contain a container ID or other unique identifier in the hardware?

    Make sure that the format of the container ID or unique identifier in the hardware complies with the format requirements for the given bus. For more information, see [Container IDs Generated from a Bus-Specific Unique ID](container-ids-generated-from-a-bus-specific-unique-id.md).

    If devnodes for the device are enumerated by a custom bus driver, check that the bus driver correctly responds to the [**IRP\_MN\_QUERY\_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) request for **BusQueryContainerID**.

-   Is the device concurrently connected to the computer by more than one bus?

    If the device is concurrently connected to the computer by two or more buses, two or more instances of the device can appear in the Devices and Printers UI. These instances can have one or more device instances for each bus to which the device is attached. To resolve this problem, make sure that the device reports a container ID or a device-specific unique identifier, and reports the same value on each bus.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Troubleshooting%20the%20Implementation%20of%20Container%20IDs%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




