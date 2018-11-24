---
title: Support for TWAIN-Compatible Applications
description: Support for TWAIN-Compatible Applications
ms.assetid: 8135178f-a432-4200-81c3-8e12112637f4
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Support for TWAIN-Compatible Applications





In order to support TWAIN applications with private capabilities, WIA drivers can use a technique known as *pass-through* functionality. The pass-through mechanism refers to the way a TWAIN-compatible application communicates with a WIA driver, using the data source manager and the TWAIN compatibility layer as intermediaries. It is important to note that TWAIN capability pass-through is supported only in Windows XP and later operating system versions.

All communication between a TWAIN-compatible application and the WIA driver goes first to the data source manager (*twain\_32.dll*), which in turn calls into the TWAIN compatibility layer (*wiadss.dll*). The TWAIN compatibility layer then calls the **IWiaItemExtras::Escape** method, which calls the **IStiUSD::Escape** method. The TWAIN compatibility layer calls only the **IWiaItemExtras::Escape** method. The driver developer should be concerned only with the device receiving an **IStiUSD::Escape** call. For more information about **IWiaItemExtras::Escape**, see the Microsoft Windows SDK documentation.

**Note**   The purpose of TWAIN pass-through functionality is to provide support to driver writers who are making the transition from TWAIN drivers to WIA drivers. It is not intended for the purpose of adding TWAIN features to a WIA driver. If your WIA driver does not require support for TWAIN, you should not add this functionality to your driver.

 

The following topics are discussed in this section:

[Enabling TWAIN Capability Pass-Through in a WIA Driver](enabling-twain-capability-pass-through-in-a-wia-driver.md)

[Using the IStiUSD Escape Method](using-the-istiusd-escape-method.md)

 

 




