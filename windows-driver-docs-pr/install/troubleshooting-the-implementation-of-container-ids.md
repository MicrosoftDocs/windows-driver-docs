---
title: Troubleshooting the Implementation of Container IDs
description: Troubleshooting the Implementation of Container IDs
ms.assetid: 9c992f5a-73b6-4567-977f-1cd92862bf60
keywords:
- container IDs WDK , troubleshooting
ms.date: 04/20/2017
ms.localizationpriority: medium
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

    If the list of capability values for the devnode contains the CM_DEVCAP_REMOVABLE flag, the devnode is marked as removable. The Plug and Play (PnP) manager then creates a new device container for the devnode and its children that cannot be removed.

    For more information about the removable device capability, see [Container IDs Generated from the Removable Device Capability](container-ids-generated-from-the-removable-device-capability.md).

    For more information about Device Manager, see [Using Device Manager](using-device-manager.md).

-   Does the device contain a container ID or other unique identifier in the hardware?

    Make sure that the format of the container ID or unique identifier in the hardware complies with the format requirements for the given bus. For more information, see [Container IDs Generated from a Bus-Specific Unique ID](container-ids-generated-from-a-bus-specific-unique-id.md).

    If devnodes for the device are enumerated by a custom bus driver, check that the bus driver correctly responds to the [**IRP_MN_QUERY_ID**](https://msdn.microsoft.com/library/windows/hardware/ff551679) request for **BusQueryContainerID**.

-   Is the device concurrently connected to the computer by more than one bus?

    If the device is concurrently connected to the computer by two or more buses, two or more instances of the device can appear in the Devices and Printers UI. These instances can have one or more device instances for each bus to which the device is attached. To resolve this problem, make sure that the device reports a container ID or a device-specific unique identifier, and reports the same value on each bus.

 

 





