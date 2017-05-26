---
title: WIA Flatbed Scanner Compatibility for Windows XP and Windows Me
author: windows-driver-content
description: WIA Flatbed Scanner Compatibility for Windows XP and Windows Me
ms.assetid: fc3424fa-3898-4f6a-a611-f81d97db8b1d
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA Flatbed Scanner Compatibility for Windows XP and Windows Me


## <a href="" id="ddk-wia-flatbed-scanner-compatibility-for-windows-me-and-windows-xp-si"></a>


The Windows Vista WIA item tree causes some compatibility problems in applications that are written for Windows XP and Windows Me.

To simplify compatibility issues between Windows Vista WIA drivers and applications and older WIA drivers and applications, Windows Vista has an internal compatibility layer. This compatibility layer will allow you to use Windows XP (and Windows Me) drivers and applications with Windows Vista drivers and applications, respectively. On Windows Vista, this translation process is transparent to both the drivers and applications. For more information about this compatibility layer, see [WIA Compatibility Layer](wia-compatibility-layer.md).

However, compatibility for Windows Vista drivers and applications on a Windows XP or Windows Me is more complex. Applications that were written for the version of WIA that existed on those legacy operating systems follow a different set of rules and assumptions. WIA scanner item trees in Windows XP and Windows Me combine the scanner's features onto a single item in the item tree. The root item controls the transfer behavior of that child item. For example, a scanner uses the first child item as the programmable data source and the root item property [**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](https://msdn.microsoft.com/library/windows/hardware/ff551384) (known as WIA\_IPS\_DOCUMENT\_HANDLING\_SELECT in Windows Vista) to switch between flatbed scanning and feeder scanning.

This item-overload approach requires applications to keep track of required WIA properties for important WIA items to help classify a scanner's features. If the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property exists on the scanner's root item, the application assumes that the scanner supports scanning from a document feeder. If this property is set to FLATBED, the application assumes that the scanner also supports flatbed platen scanning. As a result, older WIA applications will navigate to the root of a new WIA scanner item tree and will not find any properties that tell them the device's capabilities.

**Note**   The flatbed scanner item must be the first child item in the WIA item tree if other scanning data sources are implemented. This location ensures that Windows XP and Windows Me applications that are able to operate a basic flatbed scanner will automatically find the flatbed scanning functionality of your device. Some applications navigate to the first child item, which used to be the only child item, and assume that it is the flatbed or feeder of the scanner. Implementing the scanner item tree with the flatbed scanner item as the first child item will prevent many backward-compatibility problems.

 

For more information about compatibility, see [WIA Item Property and Location Changes](wia-item-property-and-location-changes.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Flatbed%20Scanner%20Compatibility%20for%20Windows%20XP%20and%20Windows%20Me%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


