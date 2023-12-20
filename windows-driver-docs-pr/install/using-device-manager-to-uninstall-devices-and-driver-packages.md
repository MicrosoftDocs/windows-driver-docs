---
title: Using Device Manager to Uninstall Devices and Driver Packages
description: Using Device Manager to Uninstall Devices and Driver Packages
ms.date: 12/20/2023
---

# Using Device Manager to Uninstall Devices and Driver Packages

This page describes how to uninstall a device or driver package on Windows 10 and Windows 11.  Before uninstalling a device, we recommend physically unplugging the device from the system.  If the device is uninstalled before it is unplugged, Windows may rediscover the device and reinstall drivers for it in the time between the uninstall and unplugging the device.

First, open Settings (you can do this using the `Windows+I` keyboard shortcut) and type Remove. Select **Add or remove programs**. If the device or driver package that you wish to remove appears in the list of programs, select uninstall.

If your device or driver package does not appear in the list, you'll need to use Device Manager to uninstall the device.  If that device is the only device using the driver package, then the driver package can also be removed via Device Manager.  To launch Device Manager, select the Start button, type Device Manager, and press Enter.

Then follow these steps:

1. Select the View menu and turn on **Show Hidden Devices**.
1. Expand the node that represents the type of device that you want to uninstall, right-select the device entry for the device you want to uninstall, and select **Uninstall**.
1. On the **Confirm Device Removal** dialog box, if you wish to remove the driver package in addition to uninstalling the device, select the **Delete the driver software for this device** option. When ready to complete the operation, select **OK**.

You may also need to restart the computer.

For more information about uninstalling driver and driver packages, see [How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md).
