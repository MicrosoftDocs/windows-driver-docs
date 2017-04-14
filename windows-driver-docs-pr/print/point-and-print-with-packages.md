---
title: Point and Print with Packages
author: windows-driver-content
description: Point and Print with Packages
ms.assetid: ea160ffc-fca3-49e4-894d-67bdc65cda38
keywords: ["Point and Print WDK , security", "User Account Control WDK printer", "UAC WDK printer", "driver store WDK printer"]
---

# Point and Print with Packages


The package approach to driver installation provides improved security for point and print by checking driver signing during the establishment of a point and print connection.

When a package-aware third-party driver is installed on Windows Vista, Setup automatically copies the driver package into the driver store and then installs the driver from the driver package in the driver store. A driver package that has been copied into the driver store is said to be staged.

Driver packages can be staged without immediately being installed on the system, so that they are available for installation later. Adding a driver package to the driver store, either during installation or separately, requires administrator rights. After a driver package is in the driver store, however, a standard user can install the driver.

Because the driver store is a trusted store, adding a package to the driver store is a privileged operation. A driver can be staged only by an administrator or a standard user who has been granted driver installation rights by the Group Policy for Devices policy.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Point%20and%20Print%20with%20Packages%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


