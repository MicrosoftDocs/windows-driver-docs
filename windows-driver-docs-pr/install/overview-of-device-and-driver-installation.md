---
title: Overview of Device and Driver Installation
description: Overview of Device and Driver Installation
ms.assetid: 5f29635b-c41b-40d1-8b83-b7f5bc71413b
keywords: ["Device setup WDK device installations , about device installations", "device installations WDK , about device installations", "installing devices WDK , about device installations"]
---

# Overview of Device and Driver Installation


## <a href="" id="ddk-device-installation-overview-dg"></a>


Windows provides components to install devices and drivers. The system-provided device installation components work with vendor-supplied components to install devices.

Windows installs devices when the system restarts and at any time after a system restart when a user plugs in a Plug and Play (PnP) device (or manually installs a non-PnP device). In support of PnP, Windows proceeds with device installation that is based on the devices in the system, instead of structuring installation around the drivers. For example, instead of loading a set of drivers and have those drivers detect the devices that they support, Windows determines the devices that are present in the system and loads and calls the drivers for each device. Drivers such as the ACPI driver and other PnP [bus drivers](https://msdn.microsoft.com/library/windows/hardware/ff540704) help Windows determine which devices are present.

## In this section


-   [How Windows Installs Devices](how-windows-installs-devices.md)
-   [System-provided Device Installation Components](system-provided-device-installation-components.md)
-   [Vendor-provided Device Installation Components](vendor-provided-device-installation-components.md)
-   [Device Installation Files](device-installation-files.md)
-   [Device Installation Types](device-installation-types.md)
-   [How Windows Selects Drivers](how-setup-selects-drivers.md)

For more information about device management and installation, see the [Driver Installation](http://go.microsoft.com/fwlink/p/?linkid=70230) website.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Overview%20of%20Device%20and%20Driver%20Installation%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




