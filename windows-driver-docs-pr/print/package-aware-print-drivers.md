---
title: Package-Aware Print Drivers
author: windows-driver-content
description: Package-Aware Print Drivers
MS-HAID:
- 'prtinst\_89404671-55db-483f-be25-a34c9d564c2c.xml'
- 'print.package\_aware\_print\_drivers'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f2ab38b9-410c-4dd8-bb81-4a8e0e48317a
keywords: ["package-aware print drivers WDK"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Package-Aware%20Print%20Drivers%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


