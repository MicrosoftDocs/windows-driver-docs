---
title: Picture Resampling Control
description: Picture Resampling Control
ms.assetid: 08d74812-3393-4461-91c4-644ecc5ad428
keywords:
- picture resampling WDK DirectX VA
- spatial scalable video coding WDK DirectX VA
- reference picture resampling WDK DirectX VA
- resampling pictures WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Picture Resampling Control


## <span id="ddk_picture_resampling_control_gg"></span><span id="DDK_PICTURE_RESAMPLING_CONTROL_GG"></span>


When the [bDXVA\_Func variable](bdxva-func-variable.md) is equal to 4, the operation specified is picture resampling. This operation is used for purposes such as spatial scalable video coding, reference picture resampling, or resampling for use as an upsampled or display picture.

Picture resampling is performed as specified in H.263 Annex O Spatial Scalability or in H.263 Annex P with clipping at the picture edges, which is the same method of picture resampling as in some forms of Spatial Scalability in MPEG-2 and MPEG-4. This function uses simple two-tap separable filtering.

Note that picture resampling control does not require a connection configuration. Its operation requires only support of the appropriate restricted mode GUID. Because no connection configuration is needed for picture resampling control, no minimal interoperability set must be defined for its operation.

A single buffer type defined in the [**DXVA\_PicResample**](https://msdn.microsoft.com/library/windows/hardware/ff564010) structure controls the resampling process.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Picture%20Resampling%20Control%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




