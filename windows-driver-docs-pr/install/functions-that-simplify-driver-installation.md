---
title: Functions that Simplify Driver Installation
description: Functions that Simplify Driver Installation
keywords:
- Functions WDK , simplifying driver installations
- DiInstallDevice
- DiInstallDriver
- DiRollbackDriver
- UpdateDriverForPlugAndPlayDevices
- PnP WDK device installations
- Plug and Play WDK device installations
ms.date: 03/11/2022
---

# Functions that Simplify Driver Installation

An installation application can use the following functions to simplify the installation of a PnP [driver package](driver-packages.md).

### <a href="" id="diinstalldevice--windows-vista-and-later-versions-of-windows-"></a> DiInstallDevice (Windows Vista and later versions of Windows)

The [**DiInstallDevice**](/windows/win32/api/newdev/nf-newdev-diinstalldevice) function installs a specific driver package that is preinstalled in the [Driver Store](driver-store.md) on a specific device present in the system.

An installation application should only use this function if both of the following are true:

-   The application incorporates more than one device instance of the same type, that is, all the device instances have the same hardware IDs and compatible IDs.

-   The application requires that device-instance-specific driver packages be installed on the device instances.

Otherwise, an installation application should use [**DiInstallDriver**](/windows/win32/api/newdev/nf-newdev-diinstalldriverw) or [**UpdateDriverForPlugAndPlayDevices**](/windows/win32/api/newdev/nf-newdev-updatedriverforplugandplaydevicesa) to install the driver package that is the best match for a device.

A caller can also call **DiInstallDevice** to do the following:

-   Search for a preinstalled driver package that is the best match for the device.

-   Install a null driver on a specific device.

-   Notify the caller whether a system restart is required to complete the installation.

### <a href="" id="diinstalldriver--windows-vista-and-later-versions-of-windows-"></a> DiInstallDriver (Windows Vista and later versions of Windows)

The [**DiInstallDriver**](/windows/win32/api/newdev/nf-newdev-diinstalldriverw) function preinstalls a [driver package](driver-packages.md) in the [Driver Store](driver-store.md) and then installs the driver package on all devices present in the system that have a hardware ID or a compatible ID that matches the driver package.

Calling **DiInstallDriver** or [**UpdateDriverForPlugAndPlayDevices**](/windows/win32/api/newdev/nf-newdev-updatedriverforplugandplaydevicesa) is the simplest way for an installation application to install a new driver package for a device. **DiInstallDriver** and **UpdateDriverForPlugAndPlayDevices** perform the same basic installation operations. However **UpdateDriverForPlugAndPlayDevices** supports additional installation options.

By default, **DiInstallDriver** only installs the driver package on a device if the driver package is a better match to the device than the driver package that is currently installed on the device. For information about how Windows selects a driver package for device, see [How Windows Selects Drivers](./how-windows-selects-a-driver-for-a-device.md).

A caller can also call **DiInstallDriver** to do the following:

-   Force the installation of the specified driver package regardless of whether the driver package is a better match to the device than the driver package that is currently installed on the device.

    **Caution**   Forcing the installation of the driver package can result in replacing a more compatible or newer driver package with a less compatible or older driver package.

-   Indicate to the caller whether a system restart is required to complete the installation.

### <a href="" id="dirollbackdriver--windows-vista-and-later-versions-of-windows-"></a> DiRollbackDriver (Windows Vista and later versions of Windows)

The [**DiRollbackDriver**](/windows/win32/api/newdev/nf-newdev-dirollbackdriver) function replaces the driver package that is currently installed on a device with the previously installed backup driver package that is set for a device. This function is provided primarily to restore a device to a working condition if a device fails after updating the driver package for the device. This function performs the same operation that would be performed if a user clicked **Roll Back Driver** on the Driver page for the device in Device Manager.

Windows maintains at most one backup driver package for a device. Windows sets a driver package as the backup driver for a device immediately after the driver package is successfully installed on the device and Windows determines that the device is functioning correctly. However, if a driver package does not install successfully on a device or the device does not function correctly after the installation, Windows does not set the driver package as the backup driver for the device.

A caller can also call **DiRollbackDriver** to do the following:

-   Suppress the display of any user interface component that is associated with the driver rollback.

-   Indicate to the caller whether a system restart is required to complete the installation.

For more information about driver package rollback, see information about Device Manager in Help and Support Center.

### <a href="" id="updatedriverforplugandplaydevices"></a> UpdateDriverForPlugAndPlayDevices

The [**UpdateDriverForPlugAndPlayDevices**](/windows/win32/api/newdev/nf-newdev-updatedriverforplugandplaydevicesa) function installs the driver package on all devices present in the system that have a hardware ID or compatible ID that matches the driver package.

Calling this function or [**DiInstallDriver**](/windows/win32/api/newdev/nf-newdev-diinstalldrivera) is the simplest way for an installation application to install a new driver package that is the best match for devices in the system. The basic operation of **UpdateDriverForPlugAndPlayDevices** is similar to the operation of **DiInstallDriver**. However **UpdateDriverForPlugAndPlayDevices** supports additional installation options.

By default, **UpdateDriverForPlugAndPlayDevices** only installs the driver package on a device if the driver package is a better match to the device than the driver package that is currently installed on a device.

A caller can also optionally call **UpdateDriverForPlugAndPlayDevices** to do the following:

-   Force the installation of the specified driver package regardless of whether the driver package is a better match to the device than the driver package that is currently installed on the device.

    **Caution**   Forcing the installation of the driver package can result in replacing a more compatible or newer driver package with a less compatible or older driver package.

-   Suppress copying, renaming, or deleting installation files.

-   Suppress the display of user interface components.

-   Indicate to the caller whether a system restart is required to complete the installation.

