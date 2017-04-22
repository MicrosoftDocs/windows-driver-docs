---
title: Multiple Session Copy Protection
description: Multiple Session Copy Protection
ms.assetid: f6ac9854-3326-48da-9153-1eec596a157b
keywords:
- copy protection WDK video miniport , multiple session
- multiple session copy protection WDK video miniport
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Multiple Session Copy Protection


## <span id="ddk_multiple_session_copy_protection_gg"></span><span id="DDK_MULTIPLE_SESSION_COPY_PROTECTION_GG"></span>


The miniport driver of a device that has copy protection can optionally support multiple simultaneous copy protection sessions. To do so, the miniport driver should do the following:

-   Return a unique copy protection key in **dwCPKey** for each copy protection activation.

-   Keep copy protection enabled until all sessions have been temporarily turned off (through VP\_CP\_CMD\_CHANGE) or deactivated (VP\_CP\_CMD\_DEACTIVATE). For example, the miniport driver could increment or decrement a reference count every time copy protection is activated (VP\_CP\_CMD\_ACTIVATE) or deactivated/turned off, disabling copy protection entirely only when the reference count is zero.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multiple%20Session%20Copy%20Protection%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




