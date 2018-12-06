---
title: Alpha-Blend Data Loading
description: Alpha-Blend Data Loading
ms.assetid: d61fbb07-a6b0-4623-bb5b-1c1218f570ae
keywords:
- alpha-blend data loading WDK DirectX VA
- blended pictures WDK DirectX VA , alpha-blend data loading
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Alpha-Blend Data Loading


## <span id="ddk_alpha_blend_data_loading_gg"></span><span id="DDK_ALPHA_BLEND_DATA_LOADING_GG"></span>


When the [bDXVA\_Func variable](bdxva-func-variable.md) is equal to 2, the operation specified is the loading of data specifying an alpha-blending surface to be blended with video data. There are three ways that the alpha-blending data can be loaded:

-   A 16-entry AYUV palette with an index-alpha 4-4 (IA44) or alpha-index 4-4 (AI44) alpha-blending surface

-   A 16-entry AYUV palette with DPXD, Highlight, and DCCMD data

-   An AYUV graphic surface

The [**DXVA\_ConfigAlphaLoad**](https://msdn.microsoft.com/library/windows/hardware/ff563129) structure determines which of these methods is used.

 

 





