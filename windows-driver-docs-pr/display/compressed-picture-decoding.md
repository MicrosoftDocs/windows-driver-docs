---
title: Compressed Picture Decoding
description: Compressed Picture Decoding
ms.assetid: 61633a15-72e4-49a4-9a42-684bde21df9e
keywords: ["compressed picture decoding WDK DirectX VA", "picture decoding WDK DirectX VA , compressed", "video decoding WDK DirectX VA , compressed pictures", "decoding video WDK DirectX VA , compressed pictures", "compressed picture decoding WDK DirectX VA , about compressed picture decoding"]
---

# Compressed Picture Decoding


## <span id="ddk_compressed_picture_decoding_gg"></span><span id="DDK_COMPRESSED_PICTURE_DECODING_GG"></span>


When the [bDXVA\_Func variable](bdxva-func-variable.md) equals 1, the operation specified is compressed picture decoding. The [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure contains the DirectX VA connection configuration data for compressed picture decoding.

### <span id="Compressed_Picture_Parameters"></span><span id="compressed_picture_parameters"></span><span id="COMPRESSED_PICTURE_PARAMETERS"></span>Compressed Picture Parameters

The parameters that must be sent once for each picture to be decoded are specified in the [**DXVA\_PictureParameters**](https://msdn.microsoft.com/library/windows/hardware/ff564012) structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Compressed%20Picture%20Decoding%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




