---
title: Updating Driver Files
description: Updating Driver Files
keywords:
- Hardware Update Wizard WDK
- updating driver files
- driver file updates WDK
- Device setup WDK device installations , updating existing drivers
- device installations WDK , updating existing drivers
- installing devices WDK , updating existing drivers
- existing driver updates WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating Driver Files





Drivers are updated whenever one of the following occurs:

-   The **Hardware Update Wizard** is run from **Device Manager**.

    **Note**  Starting with Windows Vista, this wizard is now named the **Update Driver Software Wizard**.

     

-   Windows Update is run.

-   Installation software for a device is run.

-   Starting with Windows Vista, you can run the [PnPUtil](../devtest/pnputil.md) tool from an elevated command prompt to install or update the [driver package](driver-packages.md) for the device.

Use the following guidelines when you write installation software and INF files that update existing drivers.

-   Installation software can call [**UpdateDriverForPlugAndPlayDevices**](/windows/win32/api/newdev/nf-newdev-updatedriverforplugandplaydevicesa), supplying an INF file and a hardware ID, to update drivers for devices that match the hardware ID.

    Starting with Windows Vista, installation software can also call one of the following to update drivers:

    -   [**DiInstallDriver**](/windows/win32/api/newdev/nf-newdev-diinstalldrivera), which pre-installs a driver and then installs the driver on devices present in the system that the driver supports.
    -   [**DiInstallDevice**](/windows/win32/api/newdev/nf-newdev-diinstalldevice), which installs a specified driver from the driver store on a specified device that is present in the system.

    For more information, see [Writing a Device Installation Application](writing-a-device-installation-application.md).

-   When upgrading a driver, class installers and co-installers should not supply finish-install pages in response to [**DIF_NEWDEVICEWIZARD_FINISHINSTALL**](./dif-newdevicewizard-finishinstall.md) unless absolutely necessary. If possible, obtain finish-install information from the settings of the previous installation.

-   To the extent possible, class installers and co-installers should avoid basing behavior on whether they are providing an initial installation or are updating drivers for an already-installed device.

-   Starting with Windows XP, the registry values **CoInstallers32** and **EnumPropPages32** are deleted before the delivery of [**DIF_REGISTER_COINSTALLERS**](./dif-register-coinstallers.md). INF files for earlier operating system versions must explicitly either delete these values or perform a nonappending modify operation on them.

-   Starting with Windows XP, the registry values **UpperFilters** and **LowerFilters** are deleted before the delivery of [**DIF_INSTALLDEVICE**](./dif-installdevice.md). INF files for earlier operating system versions must explicitly either delete these values or perform a nonappending modify operation on them.

-   Do *not* use [**INF DelFiles directives**](inf-delfiles-directive.md) or [**INF RenFiles directives**](inf-renfiles-directive.md) when updating drivers. Windows cannot guarantee that a particular file is not being used by another device. (Class installers and co-installers can delete or rename files, *if* they can reliably determine that no devices are using the files.)

-   Use the [**INF DelReg directive**](inf-delreg-directive.md) to remove old device-specific registry entries from a previous installation of the device, if the entries are no longer needed. (Do not remove global registry entries.)

-   Do *not* use the [**INF DelService directive**](inf-delservice-directive.md) in an [**INF DDInstall.Services section**](inf-ddinstall-services-section.md) to remove previously installed device/driver services from the target computer. Windows cannot guarantee that a particular service is not being used by another device. (Class installers and co-installers can delete services, *if* they can reliably determine that no devices are using the services.)

-   When updating a class installer, class co-installer, or service DLL, you must give the new version a new file name.

For more information about INF files, see [Creating an INF File](overview-of-inf-files.md) and [INF File Sections and Directives](./index.md).

