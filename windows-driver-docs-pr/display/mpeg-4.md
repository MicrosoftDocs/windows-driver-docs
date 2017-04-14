---
title: MPEG-4
description: MPEG-4
ms.assetid: 7879acd5-39fe-46b4-a427-43e4ea52315e
keywords: ["MPEG-4 WDK DirectX VA"]
---

# MPEG-4


## <span id="ddk_mpeg_4_gg"></span><span id="DDK_MPEG_4_GG"></span>


MPEG-4 was based heavily on H.263 for progressive-scan coding, and on MPEG-2 for support of interlace and color sampling formats other than 4:2:0. The features that support H.263 and MPEG-2 can be used to support MPEG-4.

MPEG-4 can support a sample accuracy of more than 8 bits. DirectX VA includes a mechanism to support more than 8 bits per pixel using the **bBPPminus1** member of the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure.

**Note**   The features most unique to MPEG-4, such as shape coding, object orientation, face modeling, mesh objects, and sprites, are not supported in DirectX VA.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20MPEG-4%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




