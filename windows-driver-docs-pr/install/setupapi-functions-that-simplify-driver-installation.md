---
title: SetupAPI Functions that Simplify Driver Installation
description: SetupAPI Functions that Simplify Driver Installation
ms.assetid: 7201b260-6239-4c76-8d48-7e2df9c662cd
keywords: ["SetupAPI functions WDK , simplifying driver installations", "DiInstallDevice", "DiInstallDriver", "DiRollbackDriver", "DiShowUpdateDevice", "InstallSelectedDriver", "UpdateDriverForPlugAndPlayDevices", "PnP WDK device installations , SetupAPI", "Plug and Play WDK device installations , SetupAPI"]
---

# SetupAPI Functions that Simplify Driver Installation


Driver Install Frameworks (DIFx) includes tools that greatly simplify the installation of Plug and Play (PnP) function drivers and class filter drivers. An installation application should use the DIFx tools if they provide the functionality that the installation application requires. Otherwise, an installation application can use the following SetupAPI functions to simplify the installation of a PnP function driver.

### <a href="" id="diinstalldevice--windows-vista-and-later-versions-of-windows-"></a> DiInstallDevice (Windows Vista and later versions of Windows)

The [**DiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544710) function installs a specific driver that is preinstalled in the [driver store](driver-store.md) on a specific device present in the system.

An installation application should only use this function if both of the following are true:

-   The application incorporates more than one device instance of the same type, that is, all the device instances have the same hardware IDs and compatible IDs.

-   The application requires that device-instance-specific drivers be installed on the device instances.

Otherwise, an installation application should use [**DiInstallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff544717) or [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534) to install the driver that is the best match for a device.

A caller can also call **DiInstallDevice** to do the following:

-   Search for a preinstalled driver that is the best match to the device, and if one is not found, display the Found New Hardware wizard for the device.

-   Suppress invoking finish-install pages and finish-install actions.

-   Install a null driver on a specific device.

-   Notify the caller whether a system restart is required to complete the installation.

### <a href="" id="diinstalldriver--windows-vista-and-later-versions-of-windows-"></a> DiInstallDriver (Windows Vista and later versions of Windows)

The [**DiInstallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff544717) function preinstalls a [driver package](driver-packages.md) in the [driver store](driver-store.md) and then installs the driver on all devices present in the system that have a hardware ID or a compatible ID that matches the driver package.

Calling **DiInstallDriver** or [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534) is the simplest way for an installation application to install a new driver for a device. **DiInstallDriver** and **UpdateDriverForPlugAndPlayDevices** perform the same basic installation operations. However **UpdateDriverForPlugAndPlayDevices** supports additional installation options.

By default, **DiInstallDriver** only installs the driver on a device if the driver is a better match to the device than the driver that is currently installed on the device. For information about how Windows selects a driver for device, see [How Windows Selects Drivers](how-setup-selects-drivers.md).

A caller can also call **DiInstallDriver** to do the following:

-   Force the installation of the specified driver regardless of whether the driver is a better match to the device than the driver that is currently installed on the device.

    **Caution**   Forcing the installation of the driver can result in replacing a more compatible or newer driver with a less compatible or older driver.

     

-   Indicate to the caller whether a system restart is required to complete the installation.

### <a href="" id="dirollbackdriver--windows-vista-and-later-versions-of-windows-"></a> DiRollbackDriver (Windows Vista and later versions of Windows)

The [**DiRollbackDriver**](https://msdn.microsoft.com/library/windows/hardware/ff544721) function replaces the driver that is currently installed on a device with the previously installed backup driver that is set for a device. This function is provided primarily to restore a device to a working condition if a device fails after updating the driver for the device. This function performs the same operation that would be performed if a user clicked **Roll Back Driver** on the Driver page for the device in Device Manager.

Windows maintains at most one backup driver for a device. Windows sets a driver as the backup driver for a device immediately after the driver is successfully installed on the device and Windows determines that the device is functioning correctly. However, if a driver does not install successfully on a device or the device does not function correctly after the installation, Windows does not set the driver as the backup driver for the device.

A caller can also call **DiRollbackDriver** to do the following:

-   Suppress the display of any user interface component that is associated with the driver rollback.

-   Indicate to the caller whether a system restart is required to complete the installation.

For more information about driver rollback, see information about Device Manager in Help and Support Center.

### <a href="" id="dishowupdatedevice--windows-vista-and-later-versions-of-windows-"></a> DiShowUpdateDevice (Windows Vista and later versions of Windows)

The [**DiShowUpdateDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544727) function displays the Hardware Update wizard for a specified device present in the system. The Hardware Update wizard will search, as directed by the user, for an updated driver on the user's computer, installation medium, or Windows Update.

A caller can also direct **DiShowUpdateDevice** to indicate to the caller whether a system restart is required to complete the installation.

For more information about how to update device drivers by using Hardware Update wizard, see information about Device Manager in Help and Support Center.

### <a href="" id="installselecteddriver"></a> InstallSelectedDriver

The [**InstallSelectedDriver**](https://msdn.microsoft.com/library/windows/hardware/ff547654) function installs a specific driver that is preinstalled in the [driver store](driver-store.md) on a specific device present in the system. **InstallSelectedDriver** is provided to support the same basic operation that is performed by [**DiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544710)**.**

To maintain compatibility with earlier versions of Windows, Windows Vista and later versions of Windows support **InstallSelectedDriver**. However, starting with Windows Vista, installation applications should call **DiInstallDevice** instead.

**InstallSelectedDriver** does not support all the options that **DiInstallDevice** supports.

### <a href="" id="updatedriverforplugandplaydevices"></a> UpdateDriverForPlugAndPlayDevices

The [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534) function installs the driver on all devices present in the system that have a hardware ID or compatible ID that matches the driver package.

Calling this function or [**DiInstallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff544717) is the simplest way for an installation application to install a new driver that is the best match for devices in the system. The basic operation of **UpdateDriverForPlugAndPlayDevices** is similar to the operation of **DiInstallDriver**. However **UpdateDriverForPlugAndPlayDevices** supports additional installation options.

By default, **UpdateDriverForPlugAndPlayDevices** only installs the driver on a device if the driver is a better match to the device than the driver that is currently installed on a device.

A caller can also optionally call **UpdateDriverForPlugAndPlayDevices** to do the following:

-   Force the installation of the specified driver regardless of whether the driver is a better match to the device than the driver that is currently installed on the device.

    **Caution**   Forcing the installation of the driver can result in replacing a more compatible or newer driver with a less compatible or older driver.

     

-   Suppress copying, renaming, or deleting installation files.

-   Suppress the display of user interface components.

-   Indicate to the caller whether a system restart is required to complete the installation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20SetupAPI%20Functions%20that%20Simplify%20Driver%20Installation%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




