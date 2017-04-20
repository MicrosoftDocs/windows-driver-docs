---
title: Alpha-Blend Data Loading
description: Alpha-Blend Data Loading
ms.assetid: d61fbb07-a6b0-4623-bb5b-1c1218f570ae
keywords:
- alpha-blend data loading WDK DirectX VA
- blended pictures WDK DirectX VA , alpha-blend data loading
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Alpha-Blend Data Loading


## <span id="ddk_alpha_blend_data_loading_gg"></span><span id="DDK_ALPHA_BLEND_DATA_LOADING_GG"></span>


When the [bDXVA\_Func variable](bdxva-func-variable.md) is equal to 2, the operation specified is the loading of data specifying an alpha-blending surface to be blended with video data. There are three ways that the alpha-blending data can be loaded:

-   A 16-entry AYUV palette with an index-alpha 4-4 (IA44) or alpha-index 4-4 (AI44) alpha-blending surface

-   A 16-entry AYUV palette with DPXD, Highlight, and DCCMD data

-   An AYUV graphic surface

The [**DXVA\_ConfigAlphaLoad**](https://msdn.microsoft.com/library/windows/hardware/ff563129) structure determines which of these methods is used.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Alpha-Blend%20Data%20Loading%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




