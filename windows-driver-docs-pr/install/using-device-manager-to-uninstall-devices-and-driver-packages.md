---
title: Using Device Manager to Uninstall Devices and Driver Packages
description: Learn how to use Device Manager to uninstall devices and driver packages on Windows 10 and Windows 11.
ms.date: 10/31/2025
ai-usage: ai-assisted
ms.topic: how-to
#customer intent: As an administrator or developer, I want to know how to uninstall device drivers
---

# Using Device Manager to uninstall devices and driver packages

This page describes how to uninstall a device or driver package on Windows 10 and Windows 11.

> [!CAUTION]
> Before you uninstall a device, we recommend physically unplugging the device from the system. If the device is uninstalled before it's unplugged, Windows might then rediscover the device and reinstall drivers for it. This reinstallation can happen immediately after the uninstall or upon rebooting the system.

To open the **Apps** page in **Settings**, in the Windows search, enter and select **Add or remove programs**. If the device or driver package that you want to remove appears in the list of programs, you can uninstall it.

If your device or driver package doesn't appear in the list, you need to use Device Manager to uninstall the device. If that device is the only device using the driver package, then you can also remove the driver package by using Device Manager.

Follow these steps:

1. To launch Device Manager, in Windows search, enter and select **Device Manager**.
1. Select the **View** menu and turn on **Show hidden devices**.
1. Expand the node that represents the type of device that you want to uninstall, right-select the device entry for that device, and select **Uninstall device**.
1. In **Confirm Device Removal**, if you want to remove the driver package in addition to uninstalling the device, select the **Delete the driver software for this device** option.
1. Select **OK**.

You might need to restart the computer.

Be sure that you're signed in with an account that has administrative privileges. If you don't have the necessary permissions, the option to delete the driver software might not appear.

For more information, see [How devices and driver packages are uninstalled](how-devices-and-driver-packages-are-uninstalled.md).

## Ensure permanent removal

To ensure that a driver package is permanently removed and not reinstalled automatically, you need to delete the driver package from the [Driver store](./driver-store.md). To do so, use the [pnputil](../devtest/pnputil.md) command. For example, you can use the following command to delete a driver package:

```cmd
pnputil /delete-driver <Published Name> /uninstall
```

This command updates any devices that use the specified driver package to use a different driver package before it removes the specified driver package from the system. If there are no other driver packages on the system that match on the device, the device has no driver package, so it won't function. Be careful before you remove a driver package from the system.

If Windows Update detects that a necessary driver is missing, it can reinstall that driver. You might need to adjust your Windows Update settings to prevent this action.

## Additional considerations

- **System Restore Point**: Before you make any changes, create a system restore point to ensure you can revert back if something goes wrong.
- **Windows Updates**: Ensure your system is up to date. Updates might resolve issues with driver management.

## Related content

- [Delete a driver package from the driver store](./how-devices-and-driver-packages-are-uninstalled.md#delete-a-driver-package-from-the-driver-store)
