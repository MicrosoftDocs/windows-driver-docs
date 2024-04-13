---
title: Install a Boot-Start Driver
description: Provides information about how to install a boot-start driver.
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
ms.date: 08/29/2022
---

# Install a boot-start driver

A *boot-start driver* is a driver for a device that must be installed to start the Microsoft Windows operating system. Most boot-start drivers are included in [driver packages](driver-packages.md) that are "in-the-box" with Windows, and Windows automatically installs these boot-start drivers during first boot of the system. If a boot-start driver for a device is not included in a driver package that is "in-the-box" with Windows, a user can install an additional vendor-supplied driver package for the device.

When possible, driver packages that contain boot-start drivers should be added to the image offline before the image is deployed to a system. For more information, see [Add and remove drivers to an offline Windows image](/windows-hardware/manufacture/desktop/add-and-remove-drivers-to-an-offline-windows-image).

When running Windows setup on a system, if setup is unable to find the disk or partition you want to install Windows to, this may be because the installation media and Windows image is missing a driver for that disk. You can update the installation media to include a driver package that provides a driver for that disk.  See [Add device drivers to Windows during Windows Setup](/windows-hardware/manufacture/desktop/add-device-drivers-to-windows-during-windows-setup) for more information. If running setup manually, during the disk selection interface, you can also select the "Have Disk" button to select a disk or file location that contains a driver package for the disks on that system.

If Windows fails to start, certain error messages that are displayed can indicate that a boot-start driver is missing. The following table describes several error messages and their possible causes.

| Error message | Possible cause |
|--|--|
| Inaccessible boot device | The boot disk is a third-party mass-storage device that requires a driver that is not included with Windows. |
| Setup could not determine your machine type | A new HAL driver is required. This error does not occur on most machines, but it might occur on a high-end server. |
| Setup could not find any hard drives in your computer | The required boot device drivers for the hard drives are not loaded. |
