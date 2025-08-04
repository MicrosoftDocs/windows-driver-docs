---
title: How Devices and Driver Packages are Uninstalled
description: Explore procedures for uninstalling devices and driver packages, including uninstalling a specific device or a device and all devices below the node in the device tree.
ms.date: 07/11/2025
ms.topic: concept-article
---

# How devices and driver packages are uninstalled

This article describes options for uninstalling a device and removing a driver package from the [driver store](driver-store.md).

## Uninstall a device or multiple devices

You can remove the device node (*devnode*) that represents a physical device by using one of the following procedures:

* **Uninstall a specific device only**: Use a device installation application that calls the [SetupAPI](setupapi.md) interface [SetupDiCallClassInstaller](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller) function with the [DIF_REMOVE](./dif-remove.md) request.

* **Uninstall a device and any devices below the specific node in the device tree**: Use a device installation application that calls the [DiUninstallDevice](/windows/win32/api/newdev/nf-newdev-diuninstalldevice) function.

When you uninstall a device, the Plug and Play (PnP) manager removes the association between the driver binary files and the device. The device remains in the kernel PnP tree and the [driver package](driver-packages.md) remains in the [driver store](driver-store.md).

If the PnP manager re-enumerates the device, the PnP manager handles the device as a new instance and installs the driver package from the driver store. A common scenario is when you unplug a device and then plug it back in.

For information on how an end user can uninstall a device, see [Using Device Manager to uninstall devices and driver packages](using-device-manager-to-uninstall-devices-and-driver-packages.md).

## Delete a driver package from the driver store

The process of deleting a [driver package](driver-packages.md) from the [driver store](driver-store.md) involves two tasks:

1. Ensure no devices are installed with the driver package.

1. Remove the driver package from the driver store.

You can complete both tasks in a single step by using one of the following procedures:

- **Windows 10 version 1607 and later**: Run the `pnputil /delete-driver <example.inf> /uninstall` command in a Command Prompt window. For more information, see [PnPUtil command syntax](../devtest/pnputil-command-syntax.md).

- **Windows 10 version 1703 and later**: The device installation application can call the [DiUninstallDriverW](/windows/win32/api/newdev/nf-newdev-diuninstalldriverw) function.

- **Windows 10 version 1511 and earlier**: Identify all devices currently installed with the driver package and update them so they don't depend on the driver package. Complete the task by using one of the following procedures:

   - Install a different driver package on the device.

   - Use the [DiInstallDevice](/windows/win32/api/newdev/nf-newdev-diinstalldevice) function with the `DIIDFLAG_INSTALLNULLDRIVER` flag and install the null driver on the device.

   - [Uninstall the device](#uninstall-a-device-or-multiple-devices), as described in this article.

   After you update all installed devices, the device installation application calls the [SetupUninstallOEMInf](/windows/win32/api/setupapi/nf-setupapi-setupuninstalloeminfa) function and removes the driver package.

The delete process removes associated metadata from the PnP manager's internal database and deletes related INF files (_.inf_) from the system INF directory.

After the driver package is removed, the package is no longer available for installation on a device. If you want to reinstall the package, download the driver package again from the original source, such as Windows Update.

> [!CAUTION]
> If you manually delete the [driver package](driver-packages.md) from the [driver store](driver-store.md), the system might display unpredictable behavior.
