---
title: Enumerating DXT Formats
description: Enumerating DXT Formats
ms.assetid: 77fc961f-1b94-43c1-b238-86f7d8e96835
keywords:
- drawing compressed textures WDK DirectDraw , enumerating DXT formats
- DirectDraw compressed textures WDK Windows 2000 display , enumerating DXT formats
- compressed texture surfaces WDK DirectDraw , enumerating DXT formats
- surfaces WDK DirectDraw , compressed textures
- textures WDK DirectDraw , compressed
- enumerating DXT formats WDK DirectDraw
- DXT formats WDK DirectDraw
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enumerating DXT Formats


## <span id="ddk_enumerating_dxt_formats_gg"></span><span id="DDK_ENUMERATING_DXT_FORMATS_GG"></span>


In Microsoft DirectX, there are two ways for your driver to enumerate pixel formats. The first method enumerates formats that can be used for textures. This method is implemented using the **lpTextureFormats** member of the [**D3DHAL\_GLOBALDRIVERDATA**](https://msdn.microsoft.com/library/windows/hardware/ff545963) structure. The second method enumerates formats that can be used for either DDSCAPS\_OVERLAY surfaces or DDSCAPS\_OFFSCREENPLAIN surfaces. The second method uses the **dwNumFourCCCodes** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure included in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure and the **lpdwFourCC** array that is also included in the DD\_HALINFO structure.

Because DXT formats are primarily intended to be used as textures, your driver enumerates DXT formats only through the first method. There is no need to add DXT formats to the **lpdwFourCC** array.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Enumerating%20DXT%20Formats%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




