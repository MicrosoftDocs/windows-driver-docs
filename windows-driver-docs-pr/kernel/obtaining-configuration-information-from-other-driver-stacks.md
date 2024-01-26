---
title: Obtaining Configuration Information from Other Driver Stacks
description: Obtaining Configuration Information from Other Driver Stacks
keywords: ["I/O WDK kernel , device configuration space", "device configuration space WDK I/O", "configuration space WDK I/O", "space WDK I/O", "driver stacks WDK configuration info", "BUS_INTERFACE_STANDARD"]
ms.date: 06/16/2017
---

# Obtaining Configuration Information from Other Driver Stacks





At times you need to obtain information from the configuration space of a device whose driver is on a stack other than the one that your driver is on. For instance, suppose you want to set a bit in the configuration space of a PCI-to-PCI bridge and you do not have a pointer to the PDO of the bridge. Although the operating system enumerates PCI-to-PCI bridges and creates a PDO for every bridge on the system, it does not register device interfaces for these devices. Therefore, you cannot use the device interface mechanism to access the configuration space of these bridges. For more information about device interfaces see [Introduction to Device Interfaces](../install/overview-of-device-interface-classes.md).

One way for a driver to access hardware belonging to other driver stacks is to write a filter driver. To access bridge hardware, for instance, you could design a filter driver that implements the required operations on the bridge's configuration space. You must also provide an INF file that specifies the bridge hardware's possible hardware IDs, so the PnP manager can load the filter driver onto the bridge's driver stack when it detects the device ID of the bridge.

Alternatively, you can install a filter programmatically using **SetupDi<em>Xxx</em>** functions in the co-installer for your device.

The filter driver can then access the bridge using the [**BUS\_INTERFACE\_STANDARD**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_bus_interface_standard) interface.



