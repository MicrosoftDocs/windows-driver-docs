---
title: Installation Component Overview
description: Installation Component Overview
keywords:
- driver packages WDK , installation components
- packages WDK , installation components
- driver installations WDK , information required
- operating systems WDK , driver installation information
- installing drivers WDK , information required
- installing
ms.date: 12/09/2021
---

# Installation Component Overview

The [Device Installation Overview](overview-of-device-and-driver-installation.md) section provides details on how the Microsoft Windows operating system finds and installs driver packages on devices, and on the components involved in such an installation.

To install a driver package on a device, the operating system requires the following information at a minimum:

-   Information about what versions of the operating system the driver package is supported on

-   The setup class GUID and setup class for the driver package

-   Driver package version information

-   The names of the driver files together with their source and destination locations

-   Device-specific information, including [hardware ID](hardware-ids.md) and [compatible IDs](compatible-ids.md), that determines applicability of the driver package

-   The name of a [catalog (.cat) file](catalog-files.md)

-   Information about how and when to load the services that are provided by each driver package (Windows 2000 and later versions of Windows)

All this information can be supplied in an INF file for the device. For most device and driver combinations, an INF file is the only installation component that is required. All driver packages require an INF file. For more information, see [Components of a Driver Package](components-of-a-driver-package.md).

If your device is involved in booting the system, installation requirements differ. See [Installing a Boot Driver](installing-a-boot-start-driver.md).

 

 





