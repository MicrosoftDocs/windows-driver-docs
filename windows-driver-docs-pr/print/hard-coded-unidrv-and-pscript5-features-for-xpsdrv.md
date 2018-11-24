---
title: Hard-Coded UniDrv and PScript5 Features for XPSDrv
description: Hard-Coded UniDrv and PScript5 Features for XPSDrv
ms.assetid: d2922bc4-83d7-40da-adee-15c0810f2321
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hard-Coded UniDrv and PScript5 Features for XPSDrv


When running in XPSDrv mode, all Unidrv or PScript5 hard-coded features are disabled. Unidrv/PScript5 hard-coded features are features that the driver's GPD/PPD file does not specify.

The hard-coded features are disabled in the following manner:

-   The features are not shown in any user interface (UI) for Unidrv or PScript5 core drivers.

-   For the Microsoft Win32 DeviceCapabilities API, the Unidrv or PScript5 driver's **DrvDeviceCapabilities** function does not report the hard-coded features.

-   PrintCapabilities XML do not contain the hard-coded features.

-   Default PrintTickets do not contain settings for the hard-coded features.

The remaining topics in this section further describe the changes in Unidrv/PScript5-based XPSDrv in the preceding areas to disable hard-coded features.

 

 




