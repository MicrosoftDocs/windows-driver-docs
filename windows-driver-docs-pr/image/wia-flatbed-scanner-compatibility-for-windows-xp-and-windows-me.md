---
title: WIA Flatbed Scanner Compatibility for Windows XP and Windows Me
description: WIA Flatbed Scanner Compatibility for Windows XP and Windows Me
ms.assetid: fc3424fa-3898-4f6a-a611-f81d97db8b1d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Flatbed Scanner Compatibility for Windows XP and Windows Me





The Windows Vista WIA item tree causes some compatibility problems in applications that are written for Windows XP and Windows Me.

To simplify compatibility issues between Windows Vista WIA drivers and applications and older WIA drivers and applications, Windows Vista has an internal compatibility layer. This compatibility layer will allow you to use Windows XP (and Windows Me) drivers and applications with Windows Vista drivers and applications, respectively. On Windows Vista, this translation process is transparent to both the drivers and applications. For more information about this compatibility layer, see [WIA Compatibility Layer](wia-compatibility-layer.md).

However, compatibility for Windows Vista drivers and applications on a Windows XP or Windows Me is more complex. Applications that were written for the version of WIA that existed on those legacy operating systems follow a different set of rules and assumptions. WIA scanner item trees in Windows XP and Windows Me combine the scanner's features onto a single item in the item tree. The root item controls the transfer behavior of that child item. For example, a scanner uses the first child item as the programmable data source and the root item property [**WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT**](https://msdn.microsoft.com/library/windows/hardware/ff551384) (known as WIA\_IPS\_DOCUMENT\_HANDLING\_SELECT in Windows Vista) to switch between flatbed scanning and feeder scanning.

This item-overload approach requires applications to keep track of required WIA properties for important WIA items to help classify a scanner's features. If the WIA\_DPS\_DOCUMENT\_HANDLING\_SELECT property exists on the scanner's root item, the application assumes that the scanner supports scanning from a document feeder. If this property is set to FLATBED, the application assumes that the scanner also supports flatbed platen scanning. As a result, older WIA applications will navigate to the root of a new WIA scanner item tree and will not find any properties that tell them the device's capabilities.

**Note**   The flatbed scanner item must be the first child item in the WIA item tree if other scanning data sources are implemented. This location ensures that Windows XP and Windows Me applications that are able to operate a basic flatbed scanner will automatically find the flatbed scanning functionality of your device. Some applications navigate to the first child item, which used to be the only child item, and assume that it is the flatbed or feeder of the scanner. Implementing the scanner item tree with the flatbed scanner item as the first child item will prevent many backward-compatibility problems.

 

For more information about compatibility, see [WIA Item Property and Location Changes](wia-item-property-and-location-changes.md).

 

 




