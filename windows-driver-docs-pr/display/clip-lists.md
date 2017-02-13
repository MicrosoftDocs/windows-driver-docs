---
title: Clip Lists
description: Clip Lists
ms.assetid: 73383093-ab83-4955-b017-cc370009fd0e
keywords: ["surfaces WDK DirectDraw , blitting", "drawing blt WDK DirectDraw , clip lists", "DirectDraw blitting WDK Windows 2000 display , clip lists", "blitting WDK DirectDraw , clip lists", "blt WDK DirectDraw , clip lists", "clip lists WDK DirectDraw", "clipped blts WDK DirectDraw"]
---

# Clip Lists


## <span id="ddk_clip_lists_gg"></span><span id="DDK_CLIP_LISTS_GG"></span>


Clipped blts are never passed to the driver on Microsoft Windows 2000 and later. The **IsClipped** member of [**DD\_BLTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550474) is always **FALSE**, and the clipped list is always **NULL**.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Clip%20Lists%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




