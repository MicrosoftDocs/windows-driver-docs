---
title: Device Tree
description: Device Tree
ms.assetid: 3220389a-06cc-4a43-8164-b785d1a16365
keywords: ["devnodes WDK PnP", "nonpresent devices WDK", "PnP WDK kernel , device trees", "Plug and Play WDK kernel , device trees", "removal relations WDK PnP", "ejection relations WDK PnP", "device trees WDK PnP", "trees WDK PnP", "device nodes WDK PnP", "child devices WDK PnP", "hierarchy WDK PnP", "relationships WDK PnP"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Device Tree





The PnP manager maintains a device tree that keeps track of the devices in the system. The following figure shows the device tree for a sample system configuration.

![sample pnp device tree](images/devtree.png)

The device tree contains information about the devices present on the system. The PnP manager builds this tree when the machine boots, using information from drivers and other components, and updates the tree as devices are added or removed.

Each node of the device tree is called a device node, or [*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode). A devnode consists of the [*device objects*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-object) for the device's drivers, plus internal information maintained by the system. Therefore, there is a devnode for each [*device stack*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-stack).

The PnP manager asks a bus driver for a list of its child devices using an [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) request. The bus driver determines its list of children according to its bus protocol. For example, the [Windows ACPI driver](acpi-driver.md), Acpi.sys, looks in the ACPI namespace, the PCI driver queries PCI configuration space, and a USB hub driver follows the USB bus protocol.

The device tree is hierarchical, with devices on a bus represented as "children" of the bus adapter, controller or other *bus device*. (A bus device is any device to which other physical, logical, or virtual devices can be attached.) You can see the hierarchy of devices in the device tree using Device Manager and choosing the view option that allows you to view devices by connection.

The hierarchy of the device tree reflects the structure in which the devices are attached in the machine. The PnP manager uses this hierarchy as it manages the devices. For example, if a user requests to unplug the USB controller from the machine represented by the previous figure, the PnP manager determines from the device tree that this action would result in three other devices also being unplugged (the USB hub, the joystick, and the camera). When the PnP manager queries the drivers for the USB controller to determine if it is safe to remove the controller, it also queries the drivers of the controller's descendants (the hub, joystick, and camera).

The device tree is dynamic. As devices are added to, and removed from the machine, the PnP manager (together with drivers) maintains a current picture of the devices on the system.

There are other relationships between devices on the machine besides the hierarchical relationships represented in the device tree. These include *removal relations* and *ejection relations*. See the reference page for [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](https://msdn.microsoft.com/library/windows/hardware/ff551670) for more information.

You cannot make any assumptions about the order in which the device tree is built, except that a bus device is configured before any of its child devices. For example, you should not assume that one device on a bus is configured before another device on the bus.

 

 




