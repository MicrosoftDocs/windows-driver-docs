---
title: Plug and Play Manager
description: Plug and Play Manager
ms.date: 11/29/2021
---

# Plug and Play Manager


The Plug and Play (PnP) manager provides the support for PnP functionality in Windows and is responsible for the following PnP-related tasks:

-   Device detection and enumeration while the system is booting

-   Processing addition or removal of devices while the system is running

-   Installing new devices with a matching [driver package](driver-packages.md)

The kernel-mode PnP manager maintains the [Device Tree](../kernel/device-tree.md) that keeps track of the devices in the system. The device tree contains information about the devices present on the system. When the computer starts, the PnP manager builds this tree by using information from drivers and other components, and updates the tree as devices are added or removed.

When a [bus driver](/windows-hardware/drivers/kernel/bus-drivers) detects an arrival or removal of a child device, it reports that to the kernel-mode PnP manager.  If a device arrival is reported and this is a new device, the kernel-mode PnP manager will either directly install a driver package on that device or notify the user-mode PnP manager that a new device is present on the system and must be installed.

When processing devices that have been installed with a driver package, the kernel-mode PnP manager also calls the [*DriverEntry*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) and [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routines of the drivers in a device's [device stack](/windows-hardware/drivers/gettingstarted/device-nodes-and-device-stacks) and sends the [**IRP_MN_START_DEVICE**](../kernel/irp-mn-start-device.md) request to start the device.


 

