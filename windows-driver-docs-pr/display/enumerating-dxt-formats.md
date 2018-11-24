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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Enumerating DXT Formats


## <span id="ddk_enumerating_dxt_formats_gg"></span><span id="DDK_ENUMERATING_DXT_FORMATS_GG"></span>


In Microsoft DirectX, there are two ways for your driver to enumerate pixel formats. The first method enumerates formats that can be used for textures. This method is implemented using the **lpTextureFormats** member of the [**D3DHAL\_GLOBALDRIVERDATA**](https://msdn.microsoft.com/library/windows/hardware/ff545963) structure. The second method enumerates formats that can be used for either DDSCAPS\_OVERLAY surfaces or DDSCAPS\_OFFSCREENPLAIN surfaces. The second method uses the **dwNumFourCCCodes** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure included in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure and the **lpdwFourCC** array that is also included in the DD\_HALINFO structure.

Because DXT formats are primarily intended to be used as textures, your driver enumerates DXT formats only through the first method. There is no need to add DXT formats to the **lpdwFourCC** array.

 

 





