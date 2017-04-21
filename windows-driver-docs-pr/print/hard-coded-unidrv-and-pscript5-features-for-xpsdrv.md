---
title: Hard-Coded UniDrv and PScript5 Features for XPSDrv
author: windows-driver-content
description: Hard-Coded UniDrv and PScript5 Features for XPSDrv
ms.assetid: d2922bc4-83d7-40da-adee-15c0810f2321
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Hard-Coded UniDrv and PScript5 Features for XPSDrv


When running in XPSDrv mode, all Unidrv or PScript5 hard-coded features are disabled. Unidrv/PScript5 hard-coded features are features that the driver's GPD/PPD file does not specify.

The hard-coded features are disabled in the following manner:

-   The features are not shown in any user interface (UI) for Unidrv or PScript5 core drivers.

-   For the Microsoft Win32 DeviceCapabilities API, the Unidrv or PScript5 driver's **DrvDeviceCapabilities** function does not report the hard-coded features.

-   PrintCapabilities XML do not contain the hard-coded features.

-   Default PrintTickets do not contain settings for the hard-coded features.

The remaining topics in this section further describe the changes in Unidrv/PScript5-based XPSDrv in the preceding areas to disable hard-coded features.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Hard-Coded%20UniDrv%20and%20PScript5%20Features%20for%20XPSDrv%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


