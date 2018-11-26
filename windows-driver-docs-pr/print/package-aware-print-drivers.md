---
title: Package-Aware Print Drivers
description: Package-Aware Print Drivers
ms.assetid: f2ab38b9-410c-4dd8-bb81-4a8e0e48317a
keywords:
- package-aware print drivers WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Package-Aware Print Drivers


Package-aware print drivers have entries in their INF files that support point and print with packages. These entries, which make it possible for point and print to accommodate print driver dependencies on other files, can be minor and depend on the nature of the driver package.

-   If the files in the driver package are unique and are not listed in other print driver packages, use the **PackageAware** keyword in the INF.

-   If the files in the driver package are shared with files in other print driver packages:
    -   Move the shared files into a separate [core driver](writing-core-drivers.md).
    -   Use the **PackageAware** keyword and the **CoreDriverDependencies** keyword to refer to this separate core driver. This is necessary to avoid file version conflicts during various remote installation scenarios.

This section includes:

[Package-Aware Print Drivers that Do Not Share Files](package-aware-print-drivers-that-do-not-share-files.md)

[Package-Aware Print Drivers that Share Files](package-aware-print-drivers-that-share-files.md)

 

 




