---
title: Using Device Manager to Uninstall Devices and Driver Packages
description: Using Device Manager to Uninstall Devices and Driver Packages
ms.date: 10/07/2020
ms.localizationpriority: medium
ms.custom: contperf-fy21q2
---

# Using Device Manager to Uninstall Devices and Driver Packages

This page describes how to uninstall a device or driver package on Windows 10.  Before uninstalling a device, it is recommended that the device is unplugged from the system.  If the device is uninstalled before it is unplugged, the operating system may rediscover the device and give it new settings in the time between the uninstall and unplugging the device.

First, open Settings (you can do this using the `Windows+I` keyboard shortcut) and type Remove. Select **Add or remove programs**. If the device or driver package that you wish to remove appears in the list of programs, select uninstall.

If your device or driver package does not appear in the list, then the device can be uninstalled via Device Manager.  If that device is the only device using the driver package, then the driver package can also be removed via Device Manager.  To launch Device Manager, click the Start button, type Device Manager, and press Enter.

Then follow these steps:

1. Click on the View menu and turn on "Show Hidden Devices"
2. Expand the node that represents the type of device that you want to uninstall, right-click the device entry for the device you want to uninstall, and select **Uninstall**.
2. On the **Confirm Device Removal** dialog box, if you wish to remove the driver package in addition to uninstalling the device, select the **Delete the driver software for this device** option. When ready to complete the operation, select **OK**.

With some devices, if the device is still plugged in when it is uninstalled, the device might continue to function until the system has been restarted.

For more information about uninstalling driver and driver packages, see [How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md).
