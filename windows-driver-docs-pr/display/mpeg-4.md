---
title: MPEG-4
description: MPEG-4
keywords:
- MPEG-4 WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MPEG-4


## <span id="ddk_mpeg_4_gg"></span><span id="DDK_MPEG_4_GG"></span>


MPEG-4 was based heavily on H.263 for progressive-scan coding, and on MPEG-2 for support of interlace and color sampling formats other than 4:2:0. The features that support H.263 and MPEG-2 can be used to support MPEG-4.

MPEG-4 can support a sample accuracy of more than 8 bits. DirectX VA includes a mechanism to support more than 8 bits per pixel using the **bBPPminus1** member of the [**DXVA\_PictureParameters**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_pictureparameters) structure.

**Note**   The features most unique to MPEG-4, such as shape coding, object orientation, face modeling, mesh objects, and sprites, are not supported in DirectX VA.

 

 

