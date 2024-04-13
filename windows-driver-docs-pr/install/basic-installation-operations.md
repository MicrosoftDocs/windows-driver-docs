---
title: Basic Installation Operations
description: Basic Installation Operations
keywords:
- SetupAPI functions WDK , basic installation operations
- device installation functions WDK SetupAPI
- SP_DEVINFO_DATA
ms.date: 03/11/2022
---

# Basic Installation Operations

Installers can use the [device installation functions](/previous-versions/ff541299(v=vs.85)) that are provided by SetupAPI to perform installation operations. These functions allow installers to search INF files for compatible drivers, to display driver choices to the user through selection dialog boxes, and to perform the actual driver installation.

Most of the device installation functions rely on information in the [**SP_DEVINFO_DATA**](/windows/win32/api/setupapi/ns-setupapi-sp_devinfo_data) structure to perform installation tasks. Each device is associated with an SP_DEVINFO_DATA structure. You can retrieve a handle (HDEVINFO) to a [device information set](device-information-sets.md) that contains all installed devices in a particular class by using the [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) function. You can free all SP_DEVINFO_DATA structures in a device information set by using the [**SetupDiDestroyDeviceInfoList**](/windows/win32/api/setupapi/nf-setupapi-setupdidestroydeviceinfolist) function. This function also frees any compatible device and class device lists that might have been added to the structure.

By using the [**SetupDiBuildDriverInfoList**](/windows/win32/api/setupapi/nf-setupapi-setupdibuilddriverinfolist) function, you can generate a list from which the installer or the user can choose the driver or device to install. **SetupDiBuildDriverInfoList** creates a list of compatible drivers or a list of all devices of a particular class.

An installer might have to examine and set values under the registry key for a device that is about to be installed. You can open the hardware or driver key for a device by using the [**SetupDiCreateDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdicreatedevregkeya) or [**SetupDiOpenDevRegKey**](/windows/win32/api/setupapi/nf-setupapi-setupdiopendevregkey) function.

You can install a new [device setup class](./overview-of-device-setup-classes.md) by using the [**SetupDiInstallClass**](/windows/win32/api/setupapi/nf-setupapi-setupdiinstallclassa) function. This function installs the new setup class from an INF file that contains an [**INF ClassInstall32 section**](inf-classinstall32-section.md).

You can remove a device from the system by using the [**SetupDiCallClassInstaller**](/windows/win32/api/setupapi/nf-setupapi-setupdicallclassinstaller) function with a DI_FUNCTION parameter of DIF_REMOVE. This function deletes the device's registry entries and, if possible, stops the device. If the device cannot be dynamically stopped, the function sets flags that eventually cause the user to be prompted to restart the system.

 

