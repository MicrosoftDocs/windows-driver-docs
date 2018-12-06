---
title: Basic Installation Operations
description: Basic Installation Operations
ms.assetid: 9bf1a3e1-6c2a-4f8c-8694-6e859a73d9a6
keywords:
- SetupAPI functions WDK , basic installation operations
- device installation functions WDK SetupAPI
- general Setup functions WDK SetupAPI
- SP_DEVINFO_DATA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Basic Installation Operations





Installers can use the [general Setup functions](https://msdn.microsoft.com/library/windows/hardware/ff544985) and [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299) that are provided by SetupAPI to perform installation operations. These functions allow installers to search INF files for compatible drivers, to display driver choices to the user through selection dialog boxes, and to perform the actual driver installation.

Most of the device installation functions rely on information in the [**SP_DEVINFO_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure to perform installation tasks. Each device is associated with an SP_DEVINFO_DATA structure. You can retrieve a handle (HDEVINFO) to a [device information set](device-information-sets.md) that contains all installed devices in a particular class by using the [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) function. You can use the [**SetupDiCreateDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff550952) function to add a new device to a device information set. You can free all SP_DEVINFO_DATA structures in a device information set by using the [**SetupDiDestroyDeviceInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550996) function. This function also frees any compatible device and class device lists that might have been added to the structure.

By using the [**SetupDiBuildDriverInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550917) function, you can generate a list from which the installer or the user can choose the driver or device to install. **SetupDiBuildDriverInfoList** creates a list of compatible drivers or a list of all devices of a particular class.

Once you have a list of compatible drivers, you can prompt the user to select from the list by using the [**SetupDiSelectDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552115) function. This function displays a dialog box that contains information about each device in the device information set. You can install a selected driver by using the [**SetupDiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552039) function. This function uses information in the driver's INF file to create to any new registry entries required, to set the configuration of the device hardware, and to copy the driver files to the appropriate directories.

An installer might have to examine and set values under the registry key for a device that is about to be installed. You can open the hardware or driver key for a device by using the [**SetupDiCreateDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550973) or [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) function.

You can install a new [device setup class](device-setup-classes.md) by using the [**SetupDiInstallClass**](https://msdn.microsoft.com/library/windows/hardware/ff552024) function. This function installs the new setup class from an INF file that contains an [**INF ClassInstall32 section**](inf-classinstall32-section.md).

You can remove a device from the system by using the [**SetupDiRemoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552097) function. This function deletes the device's registry entries and, if possible, stops the device. If the device cannot be dynamically stopped, the function sets flags that eventually cause the user to be prompted to shut down the system.

 

 





