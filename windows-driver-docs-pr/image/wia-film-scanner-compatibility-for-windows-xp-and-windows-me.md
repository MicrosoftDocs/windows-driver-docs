---
title: WIA Film Scanner Compatibility for Windows XP and Windows Me
author: windows-driver-content
description: WIA Film Scanner Compatibility for Windows XP and Windows Me
ms.assetid: 9f96ef72-2482-435f-b512-b48c12dc1628
---

# WIA Film Scanner Compatibility for Windows XP and Windows Me


## <a href="" id="ddk-wia-film-scanner-compatibility-for-windows-me-and-windows-xp-si"></a>


Film scanning items do *not* exist for Microsoft Windows XP or Windows Me. A film scanner (either a dedicated film scanner or a film scanner attachment on a flatbed scanner) will not be available to a Windows XP WIA application that runs on Windows Vista. The [WIA Compatibility Layer](wia-compatibility-layer.md) that is found in the Windows Vista WIA service handles only flatbed and basic feeder items (WIA\_CATEGORY\_FLATBED and WIA\_CATEGORY\_FEEDER) for Windows Vista devices when they are used with Windows XP applications; film and storage items (WIA\_CATEGORY\_FILM and WIA\_CATEGORY\_FINISHED\_FILE) are not translated.

You can provide rudimentary support for Windows XP WIA applications that run Windows Vista if you implement a flatbed item to mimic the basic functionality of the film item. The default user interface that is presented to the user would be the same as a flatbed scanner, so the application would only receive a single frame. And, even with such a flatbed item, the Windows Vista driver would not work on Windows XP because it provides only limited support for Windows XP applications on Windows Vista.

**Note**   If your scanner also supports flatbed scanning, the WIA flatbed scanner item must be the first WIA child item in the scanner item tree.

 

For more information about Windows XP and Windows Me compatibility, see [WIA Flatbed Scanner Compatibility for Windows Me and Windows XP](wia-flatbed-scanner-compatibility-for-windows-xp-and-windows-me.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA%20Film%20Scanner%20Compatibility%20for%20Windows%20XP%20and%20Windows%20Me%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


