---
title: Using Device Manager to Uninstall Devices and Driver Packages
description: Using Device Manager to Uninstall Devices and Driver Packages
ms.date: 09/17/2024
ai-usage: ai-assisted
---

# Using Device Manager to Uninstall Devices and Driver Packages

This page describes how to uninstall a device or driver package on Windows 10 and Windows 11.

> [!CAUTION]
> Before uninstalling a device, we recommend physically unplugging the device from the system.  If the device is uninstalled before it is unplugged, Windows may subsequently rediscover the device and reinstall drivers for it. This can happen immediately after the uninstall or upon rebooting the system.

First, open Settings (you can do this using the `Windows+I` keyboard shortcut) and type Remove. Select **Add or remove programs**. If the device or driver package that you wish to remove appears in the list of programs, select uninstall.

If your device or driver package does not appear in the list, you'll need to use Device Manager to uninstall the device.  If that device is the only device using the driver package, then the driver package can also be removed via Device Manager.  To launch Device Manager, select the Start button, type Device Manager, and press Enter.

Then follow these steps:

1. Select the View menu and turn on **Show Hidden Devices**.
1. Expand the node that represents the type of device that you want to uninstall, right-select the device entry for the device you want to uninstall, and select **Uninstall device**.
1. On the **Confirm Device Removal** dialog box, if you wish to remove the driver package in addition to uninstalling the device, select the **Delete the driver software for this device** option. When ready to complete the operation, select **OK**. If this option does not appear, see [Deleting a Driver Package from the Driver Store](./how-devices-and-driver-packages-are-uninstalled.md#deleting-a-driver-package-from-the-driver-store) for additional information.

You may also need to restart the computer.

For more information about uninstalling driver and driver packages, see [How Devices and Driver Packages are Uninstalled](how-devices-and-driver-packages-are-uninstalled.md).

## Ensuring Permanent Removal

To ensure that a driver is permanently removed and not reinstalled automatically, you need to delete the driver from the Windows driver repository (DriverStore). This can be done using the `pnputil` command. For example, you can use the following command to delete a driver:

   ```shell
   pnputil /delete-driver <Published Name> /uninstall /force
   ```

Note that this command deletes a driver package even if it is in use by devices, and also disables a device even if it provides critical system functionality.

Also be aware that Windows Update may also reinstall drivers if it detects that a necessary driver is missing. You may need to adjust your Windows Update settings to prevent this.
