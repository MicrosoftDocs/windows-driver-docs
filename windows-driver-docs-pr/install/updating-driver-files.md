---
title: Updating Driver Files
description: Updating Driver Files
ms.assetid: e232abd9-4e51-4fa7-a00c-f5e184706222
keywords: ["Hardware Update Wizard WDK", "updating driver files", "driver file updates WDK", "Device setup WDK device installations , updating existing drivers", "device installations WDK , updating existing drivers", "installing devices WDK , updating existing drivers", "existing driver updates WDK"]
---

# Updating Driver Files


## <a href="" id="ddk-updating-driver-files-dg"></a>


Drivers are updated whenever one of the following occurs:

-   The **Hardware Update Wizard** is run from **Device Manager**.

    **Note**  Starting with Windows Vista, this wizard is now named the **Update Driver Software Wizard**.

     

-   Windows Update is run.

-   Installation software for a device is run.

-   Starting with Windows Vista, you can run the [PnPUtil](https://msdn.microsoft.com/library/windows/hardware/ff550419) tool from an elevated command prompt to install or update the [driver package](driver-packages.md) for the device.

Use the following guidelines when you write installation software and INF files that update existing drivers.

-   Installation software can call [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534), supplying an INF file and a hardware ID, to update drivers for devices that match the hardware ID.

    Starting with Windows Vista, installation software can also call one of the following to update drivers:

    -   [**DiInstallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff544717), which pre-installs a driver and then installs the driver on devices present in the system that the driver supports.
    -   [**DiInstallDevice**](https://msdn.microsoft.com/library/windows/hardware/ff544710), which installs a specified driver from the driver store on a specified device that is present in the system.

    For more information, see [Writing a Device Installation Application](writing-a-device-installation-application.md).

-   When upgrading a driver, class installers and co-installers should not supply finish-install pages in response to [**DIF\_NEWDEVICEWIZARD\_FINISHINSTALL**](https://msdn.microsoft.com/library/windows/hardware/ff543702) unless absolutely necessary. If possible, obtain finish-install information from the settings of the previous installation.

-   To the extent possible, class installers and co-installers should avoid basing behavior on whether they are providing an initial installation or are updating drivers for an already-installed device.

-   Starting with Windows XP, the registry values **CoInstallers32** and **EnumPropPages32** are deleted before the delivery of [**DIF\_REGISTER\_COINSTALLERS**](https://msdn.microsoft.com/library/windows/hardware/ff543715). INF files for earlier operating system versions must explicitly either delete these values or perform a nonappending modify operation on them.

-   Starting with Windows XP, the registry values **UpperFilters** and **LowerFilters** are deleted before the delivery of [**DIF\_INSTALLDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff543692). INF files for earlier operating system versions must explicitly either delete these values or perform a nonappending modify operation on them.

-   Do *not* use [**INF DelFiles directives**](inf-delfiles-directive.md) or [**INF RenFiles directives**](inf-renfiles-directive.md) when updating drivers. Windows cannot guarantee that a particular file is not being used by another device. (Class installers and co-installers can delete or rename files, *if* they can reliably determine that no devices are using the files.)

-   Use the [**INF DelReg directive**](inf-delreg-directive.md) to remove old device-specific registry entries from a previous installation of the device, if the entries are no longer needed. (Do not remove global registry entries.)

-   Do *not* use the [**INF DelService directive**](inf-delservice-directive.md) in an [**INF DDInstall.Services section**](inf-ddinstall-services-section.md) to remove previously installed device/driver services from the target computer. Windows cannot guarantee that a particular service is not being used by another device. (Class installers and co-installers can delete services, *if* they can reliably determine that no devices are using the services.)

-   When updating a class installer, class co-installer, or service DLL, you must give the new version a new file name.

For more information about INF files, see [Creating an INF File](overview-of-inf-files.md) and [INF File Sections and Directives](inf-file-sections-and-directives.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Updating%20Driver%20Files%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




