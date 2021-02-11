---
title: How Devices and Driver Packages are Uninstalled
description: How Devices and Driver Packages are Uninstalled
ms.date: 10/07/2020
ms.localizationpriority: medium
ms.custom: contperf-fy21q2
---

# How Devices and Driver Packages are Uninstalled

This page describes how software uninstalls a device and removes a driver package from the [driver store](driver-store.md).

## Uninstalling the Device

To remove the device node (*devnode*) that represents a physical device, use one of the following:

* To uninstall only the specified device, use a device installation application that calls the [SetupAPI](setupapi.md) function [**SetupDiCallClassInstaller**](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller) with a request of [**DIF_REMOVE**](./dif-remove.md).

* To uninstall the specified device and any devices below it in the device tree, use a device installation application that calls the [**DiUninstallDevice**](/windows/win32/api/newdev/nf-newdev-diuninstalldevice) function.

When a device is uninstalled using one of these methods, the Plug and Play (PnP) manager removes the association between the driver binary files and the device.

The device remains in the kernel PnP tree and the [driver package](driver-packages.md) remains in the [driver store](driver-store.md). If the PnP manager re-enumerates the device (for example if the device is unplugged and then plugged in again), the PnP manager treats it as a new device instance and installs the driver package from the driver store.

For info on how an end user can uninstall a device, see  [Using Device Manager to Uninstall Devices and Driver Packages](using-device-manager-to-uninstall-devices-and-driver-packages.md).

## Deleting a Driver Package from the Driver Store

To delete a [driver package](driver-packages.md) from the [driver store](driver-store.md), do one of the following:

* From the command prompt, use `pnputil /delete-driver <example.inf> /uninstall`. For info on PnPUtil commands, see [PnPUtil Command Syntax](../devtest/pnputil-command-syntax.md).
* On Windows 10, version 1703 or later, a device installation application can call [**DiUninstallDriverW**](/windows/win32/api/newdev/nf-newdev-diuninstalldriverw).
* On earlier versions of Windows, a device installation application should first issue a [**DIF_REMOVE**](./dif-remove.md) request or call the [**DiUninstallDevice**](/windows/win32/api/newdev/nf-newdev-diuninstalldevice) function to uninstall all devices and then call [**SetupUninstallOEMInf**](/windows/win32/api/setupapi/nf-setupapi-setupuninstalloeminfa) to remove the driver.

Deleting a driver package from the driver store removes associated metadata from the PnP manager's internal database and deletes related INF files from the system INF directory.

After the driver package has been removed, it is no longer available to be installed on a device. To reinstall, download the driver again from the original source, such as Windows Update.

Manually deleting the [driver package](driver-packages.md) from the [driver store](driver-store.md) may result in unpredictable behavior.
