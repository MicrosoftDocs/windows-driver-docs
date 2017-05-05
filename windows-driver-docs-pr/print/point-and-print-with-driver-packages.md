---
title: Point and Print with Driver Packages
author: windows-driver-content
description: Point and Print with Driver Packages
ms.assetid: 4574d0c3-2ec5-4870-96ac-f828ba8515b3
keywords:
- Point and Print WDK , packages
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Point and Print with Driver Packages


A print client that is connected to a print server can use point and print to copy an entire driver package for installation. The advantages of using point and print with packages are that:

-   All runnable components of the driver are installed on the print client.

-   Driver signing and driver integrity are checked on the print client.

-   Point and print is more trustworthy and can be controlled better by administrators in a managed environment.

The point and print process is different in Windows Vista from earlier versions of Windows because of the introduction of driver packages. Windows Vista uses package installation as the preferred method of driver installation. In versions of Windows earlier than Windows Vista, point and print could install only basic printing functionality on the client.

Driver package installation requires a driver store, which is not available on versions of Windows earlier than Windows Vista. When a client that is running an earlier version of Windows connects to a Windows Vista print server, the print server uses point and print without packages to install the printer on the client computer.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Point%20and%20Print%20with%20Driver%20Packages%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


