---
title: Overview of Device and Driver Installation
description: Overview of Device and Driver Installation
ms.assetid: 5f29635b-c41b-40d1-8b83-b7f5bc71413b
keywords:
- Device setup WDK device installations , about device installations
- device installations WDK , about device installations
- installing devices WDK , about device installations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overview of Device and Driver Installation





Windows provides components to install devices and drivers. The [system-provided device installation components](system-provided-device-installation-components.md) work with [vendor-supplied components](vendor-provided-device-installation-components.md) to install devices.

Windows installs devices when the system restarts and at any time after a system restart when a user plugs in a Plug and Play (PnP) device (or manually installs a non-PnP device). In support of PnP, Windows proceeds with device installation that is based on the devices in the system, instead of structuring installation around the drivers. For example, instead of loading a set of drivers and have those drivers detect the devices that they support, Windows determines the devices that are present in the system and loads and calls the drivers for each device. Drivers such as the ACPI driver and other PnP [bus drivers](https://msdn.microsoft.com/library/windows/hardware/ff540704) help Windows determine which devices are present.

## In this section


-   [How Windows Installs Devices](how-windows-installs-devices.md)
-   [System-provided Device Installation Components](system-provided-device-installation-components.md)
-   [Vendor-provided Device Installation Components](vendor-provided-device-installation-components.md)
-   [Device Installation Files](device-installation-files.md)
-   [Device Installation Types](device-installation-types.md)
-   [How Windows Selects Drivers](how-setup-selects-drivers.md)

For more information about device management and installation, see the [Driver Installation](http://go.microsoft.com/fwlink/p/?linkid=70230) website.

 

 





