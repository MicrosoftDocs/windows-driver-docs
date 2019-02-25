---
title: Picture Resampling Control
description: Picture Resampling Control
ms.assetid: 08d74812-3393-4461-91c4-644ecc5ad428
keywords:
- picture resampling WDK DirectX VA
- spatial scalable video coding WDK DirectX VA
- reference picture resampling WDK DirectX VA
- resampling pictures WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Picture Resampling Control


## <span id="ddk_picture_resampling_control_gg"></span><span id="DDK_PICTURE_RESAMPLING_CONTROL_GG"></span>


When the [bDXVA\_Func variable](bdxva-func-variable.md) is equal to 4, the operation specified is picture resampling. This operation is used for purposes such as spatial scalable video coding, reference picture resampling, or resampling for use as an upsampled or display picture.

Picture resampling is performed as specified in H.263 Annex O Spatial Scalability or in H.263 Annex P with clipping at the picture edges, which is the same method of picture resampling as in some forms of Spatial Scalability in MPEG-2 and MPEG-4. This function uses simple two-tap separable filtering.

Note that picture resampling control does not require a connection configuration. Its operation requires only support of the appropriate restricted mode GUID. Because no connection configuration is needed for picture resampling control, no minimal interoperability set must be defined for its operation.

A single buffer type defined in the [**DXVA\_PicResample**](https://msdn.microsoft.com/library/windows/hardware/ff564010) structure controls the resampling process.

 

 





