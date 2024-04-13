---
title: Uninstalling Devices and Driver Packages
description: Uninstalling Devices and Driver Packages
ms.date: 04/20/2017
---

# Uninstalling Devices and Driver Packages


After a device is installed, it might be necessary to uninstall a device or a [driver package](driver-packages.md). For example, an end-user might decide to replace the associated device, or the driver package might have to be uninstalled when a driver is updated.

When you uninstall a device, you must remove the device node (*devnode*) that represents the physical instance of the device in the system.

When you uninstall a [driver package](driver-packages.md), you must complete the following actions:

-   Remove the files that are associated with the [driver package](driver-packages.md) from the [driver store](driver-store.md).

-   Delete the binary files of the driver package.

This section describes how to uninstall devices and driver packages. It is intended for driver developers who want to provide instructions or tools to their customers.

This section includes the following topics:

[How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md)

[Using Device Manager to Uninstall Devices and Driver Packages](using-device-manager-to-uninstall-devices-and-driver-packages.md)

[Using SetupAPI to Uninstall Devices and Driver Packages](using-setupapi-to-uninstall-devices-and-driver-packages.md)



