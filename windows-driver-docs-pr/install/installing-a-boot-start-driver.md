---
title: Install a Boot-Start Driver
description: Explore how to install a boot-start driver, review notes about installation and setup, and error codes with possible causes.
keywords:
- Device setup WDK device installations, boot drivers
- device installations WDK, boot drivers
- install devices WDK, boot drivers
- boot drivers WDK device installations
- boot driver distribution disks WDK device installations
- distribution disks WDK
- platform-specific distribution disks WDK
- cross-platform distribution disks WDK
- vendor-supplied boot drivers WDK
ms.date: 07/11/2025
ms.topic: install-set-up-deploy
---

# Install a boot-start driver

A *boot-start driver* is a driver for a device that must be installed to start the Microsoft Windows operating system. Most boot-start drivers are included in [driver packages](driver-packages.md) that are "in-the-box" with Windows, and Windows automatically installs these boot-start drivers during first boot of the system. If a boot-start driver for a device isn't included in a driver package "in-the-box" with Windows, a user can install another vendor-supplied driver package for the device.

Driver packages that contain boot-start drivers should be added to the image offline before the image is deployed to a system, whenever possible. For more information, see [Add and remove drivers to an offline Windows image](/windows-hardware/manufacture/desktop/add-and-remove-drivers-to-an-offline-windows-image).

If Windows setup can't locate the target disk or partition to install Windows, then the installation media and Windows image are missing a driver for the disk. You can update the installation media to include a driver package that provides a driver for that disk. For more information, see [Add device drivers to Windows during Windows Setup](/windows-hardware/manufacture/desktop/add-device-drivers-to-windows-during-windows-setup). If you run Windows setup manually, during the disk selection step, you can select **Have Disk** and choose a disk or file location that contains a driver package for the disks.

If Windows fails to start, the error message can indicate that a boot-start driver is missing. The following table describes several error messages and the possible causes.

| Error message | Possible cause |
|--|--|
| _Inaccessible boot device_ | The boot disk is a non-Microsoft mass-storage device that requires a driver that isn't included with Windows. |
| _Setup could not determine your machine type_ | A new Windows Hardware Abstraction Layer (HAL) driver is required. This error doesn't occur on most machines, but it can occur on a high-end server. |
| _Setup could not find any hard drives in your computer_ | The required boot device drivers for the hard drives aren't loaded. |
