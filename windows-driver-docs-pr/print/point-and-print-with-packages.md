---
title: Point and Print with Packages
description: Point and Print with Packages
ms.assetid: ea160ffc-fca3-49e4-894d-67bdc65cda38
keywords:
- Point and Print WDK , security
- User Account Control WDK printer
- UAC WDK printer
- driver store WDK printer
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Point and Print with Packages


The package approach to driver installation provides improved security for point and print by checking driver signing during the establishment of a point and print connection.

When a package-aware third-party driver is installed on Windows Vista, Setup automatically copies the driver package into the driver store and then installs the driver from the driver package in the driver store. A driver package that has been copied into the driver store is said to be staged.

Driver packages can be staged without immediately being installed on the system, so that they are available for installation later. Adding a driver package to the driver store, either during installation or separately, requires administrator rights. After a driver package is in the driver store, however, a standard user can install the driver.

Because the driver store is a trusted store, adding a package to the driver store is a privileged operation. A driver can be staged only by an administrator or a standard user who has been granted driver installation rights by the Group Policy for Devices policy.

 

 




