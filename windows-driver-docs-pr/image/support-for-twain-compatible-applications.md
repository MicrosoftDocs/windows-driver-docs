---
title: Support for TWAIN-Compatible Applications
author: windows-driver-content
description: Support for TWAIN-Compatible Applications
ms.assetid: 8135178f-a432-4200-81c3-8e12112637f4
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Support for TWAIN-Compatible Applications


## <a href="" id="ddk-support-for-twain-compatible-applications-si"></a>


In order to support TWAIN applications with private capabilities, WIA drivers can use a technique known as *pass-through* functionality. The pass-through mechanism refers to the way a TWAIN-compatible application communicates with a WIA driver, using the data source manager and the TWAIN compatibility layer as intermediaries. It is important to note that TWAIN capability pass-through is supported only in Windows XP and later operating system versions.

All communication between a TWAIN-compatible application and the WIA driver goes first to the data source manager (*twain\_32.dll*), which in turn calls into the TWAIN compatibility layer (*wiadss.dll*). The TWAIN compatibility layer then calls the **IWiaItemExtras::Escape** method, which calls the **IStiUSD::Escape** method. The TWAIN compatibility layer calls only the **IWiaItemExtras::Escape** method. The driver developer should be concerned only with the device receiving an **IStiUSD::Escape** call. For more information about **IWiaItemExtras::Escape**, see the Microsoft Windows SDK documentation.

**Note**   The purpose of TWAIN pass-through functionality is to provide support to driver writers who are making the transition from TWAIN drivers to WIA drivers. It is not intended for the purpose of adding TWAIN features to a WIA driver. If your WIA driver does not require support for TWAIN, you should not add this functionality to your driver.

 

The following topics are discussed in this section:

[Enabling TWAIN Capability Pass-Through in a WIA Driver](enabling-twain-capability-pass-through-in-a-wia-driver.md)

[Using the IStiUSD Escape Method](using-the-istiusd-escape-method.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Support%20for%20TWAIN-Compatible%20Applications%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


