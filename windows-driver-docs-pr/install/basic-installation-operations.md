---
title: Basic Installation Operations
description: Basic Installation Operations
ms.assetid: 9bf1a3e1-6c2a-4f8c-8694-6e859a73d9a6
keywords: ["SetupAPI functions WDK , basic installation operations", "device installation functions WDK SetupAPI", "general Setup functions WDK SetupAPI", "SP_DEVINFO_DATA"]
---

# Basic Installation Operations


## <a href="" id="ddk-basic-installation-operations-dg"></a>


Installers can use the [general Setup functions](https://msdn.microsoft.com/library/windows/hardware/ff544985) and [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299) that are provided by SetupAPI to perform installation operations. These functions allow installers to search INF files for compatible drivers, to display driver choices to the user through selection dialog boxes, and to perform the actual driver installation.

Most of the device installation functions rely on information in the [**SP\_DEVINFO\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff552344) structure to perform installation tasks. Each device is associated with an SP\_DEVINFO\_DATA structure. You can retrieve a handle (HDEVINFO) to a [device information set](device-information-sets.md) that contains all installed devices in a particular class by using the [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) function. You can use the [**SetupDiCreateDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff550952) function to add a new device to a device information set. You can free all SP\_DEVINFO\_DATA structures in a device information set by using the [**SetupDiDestroyDeviceInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550996) function. This function also frees any compatible device and class device lists that might have been added to the structure.

By using the [**SetupDiBuildDriverInfoList**](https://msdn.microsoft.com/library/windows/hardware/ff550917) function, you can generate a list from which the installer or the user can choose the driver or device to install. **SetupDiBuildDriverInfoList** creates a list of compatible drivers or a list of all devices of a particular class.

Once you have a list of compatible drivers, you can prompt the user to select from the list by using the [**SetupDiSelectDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552115) function. This function displays a dialog box that contains information about each device in the device information set. You can install a selected driver by using the [**SetupDiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552039) function. This function uses information in the driver's INF file to create to any new registry entries required, to set the configuration of the device hardware, and to copy the driver files to the appropriate directories.

An installer might have to examine and set values under the registry key for a device that is about to be installed. You can open the hardware or driver key for a device by using the [**SetupDiCreateDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff550973) or [**SetupDiOpenDevRegKey**](https://msdn.microsoft.com/library/windows/hardware/ff552079) function.

You can install a new [device setup class](device-setup-classes.md) by using the [**SetupDiInstallClass**](https://msdn.microsoft.com/library/windows/hardware/ff552024) function. This function installs the new setup class from an INF file that contains an [**INF ClassInstall32 section**](inf-classinstall32-section.md).

You can remove a device from the system by using the [**SetupDiRemoveDevice**](https://msdn.microsoft.com/library/windows/hardware/ff552097) function. This function deletes the device's registry entries and, if possible, stops the device. If the device cannot be dynamically stopped, the function sets flags that eventually cause the user to be prompted to shut down the system.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Basic%20Installation%20Operations%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




