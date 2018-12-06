---
title: Installation Component Overview
description: Installation Component Overview
ms.assetid: 29d14a3a-e89a-47ef-bd36-ee3cdcde2cd7
keywords:
- driver packages WDK , installation components
- packages WDK , installation components
- driver installations WDK , information required
- operating systems WDK , driver installation information
- installing drivers WDK , information required
- installing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installation Component Overview





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

 

 





