---
title: Point and Print with Driver Packages
description: Point and Print with Driver Packages
ms.assetid: 4574d0c3-2ec5-4870-96ac-f828ba8515b3
keywords:
- Point and Print WDK , packages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Point and Print with Driver Packages


A print client that is connected to a print server can use point and print to copy an entire driver package for installation. The advantages of using point and print with packages are that:

-   All runnable components of the driver are installed on the print client.

-   Driver signing and driver integrity are checked on the print client.

-   Point and print is more trustworthy and can be controlled better by administrators in a managed environment.

The point and print process is different in Windows Vista from earlier versions of Windows because of the introduction of driver packages. Windows Vista uses package installation as the preferred method of driver installation. In versions of Windows earlier than Windows Vista, point and print could install only basic printing functionality on the client.

Driver package installation requires a driver store, which is not available on versions of Windows earlier than Windows Vista. When a client that is running an earlier version of Windows connects to a Windows Vista print server, the print server uses point and print without packages to install the printer on the client computer.

 

 




