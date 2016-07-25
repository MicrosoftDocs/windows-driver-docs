---
title: Installation Component Overview
description: Installation Component Overview
ms.assetid: 29d14a3a-e89a-47ef-bd36-ee3cdcde2cd7
keywords: ["driver packages WDK , installation components", "packages WDK , installation components", "driver installations WDK , information required", "operating systems WDK , driver installation information", "installing drivers WDK , information required", "installing"]
---

# Installation Component Overview


## <a href="" id="ddk-installation-component-overview-pg"></a>


The [Device Installation Overview](overview-of-device-and-driver-installation.md) section provides details on how the Microsoft Windows operating system finds and installs devices and drivers, and on the components involved in such an installation.

To install a device or a driver, the operating system requires the following information at a minimum:

-   The name and version number of each operating system on which the device or drivers are supported

-   The device's setup class GUID and setup class

-   Driver version information

-   The names of the driver files together with their source and destination locations

-   Device-specific information, including [hardware ID](hardware-ids.md) and [compatible IDs](compatible-ids.md)

-   The name of a [catalog (.cat) file](catalog-files.md)

-   Information about how and when to load the services that are provided by each driver (Windows 2000 and later versions of Windows)

All this information can be supplied in an INF file for the device. For most device and driver combinations, an INF file is the only installation component that is required. All devices and drivers require an INF file. For more information, see [Supplying an INF File](supplying-an-inf-file.md).

If your device is involved in booting the system, installation requirements differ. See [Installing a Boot Driver](installing-a-boot-start-driver.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installation%20Component%20Overview%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




