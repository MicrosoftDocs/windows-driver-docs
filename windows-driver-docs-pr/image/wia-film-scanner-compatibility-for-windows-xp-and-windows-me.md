---
title: WIA Film Scanner Compatibility for Windows XP and Windows Me
description: WIA Film Scanner Compatibility for Windows XP and Windows Me
ms.assetid: 9f96ef72-2482-435f-b512-b48c12dc1628
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WIA Film Scanner Compatibility for Windows XP and Windows Me





Film scanning items do *not* exist for Microsoft Windows XP or Windows Me. A film scanner (either a dedicated film scanner or a film scanner attachment on a flatbed scanner) will not be available to a Windows XP WIA application that runs on Windows Vista. The [WIA Compatibility Layer](wia-compatibility-layer.md) that is found in the Windows Vista WIA service handles only flatbed and basic feeder items (WIA\_CATEGORY\_FLATBED and WIA\_CATEGORY\_FEEDER) for Windows Vista devices when they are used with Windows XP applications; film and storage items (WIA\_CATEGORY\_FILM and WIA\_CATEGORY\_FINISHED\_FILE) are not translated.

You can provide rudimentary support for Windows XP WIA applications that run Windows Vista if you implement a flatbed item to mimic the basic functionality of the film item. The default user interface that is presented to the user would be the same as a flatbed scanner, so the application would only receive a single frame. And, even with such a flatbed item, the Windows Vista driver would not work on Windows XP because it provides only limited support for Windows XP applications on Windows Vista.

**Note**   If your scanner also supports flatbed scanning, the WIA flatbed scanner item must be the first WIA child item in the scanner item tree.

 

For more information about Windows XP and Windows Me compatibility, see [WIA Flatbed Scanner Compatibility for Windows Me and Windows XP](wia-flatbed-scanner-compatibility-for-windows-xp-and-windows-me.md).

 

 




