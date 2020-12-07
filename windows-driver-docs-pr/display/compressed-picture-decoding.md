---
title: Compressed Picture Decoding
description: Compressed Picture Decoding
keywords:
- compressed picture decoding WDK DirectX VA
- picture decoding WDK DirectX VA , compressed
- video decoding WDK DirectX VA , compressed pictures
- decoding video WDK DirectX VA , compressed pictures
- compressed picture decoding WDK DirectX VA , about compressed picture decoding
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Compressed Picture Decoding


## <span id="ddk_compressed_picture_decoding_gg"></span><span id="DDK_COMPRESSED_PICTURE_DECODING_GG"></span>


When the [bDXVA\_Func variable](bdxva-func-variable.md) equals 1, the operation specified is compressed picture decoding. The [**DXVA\_ConfigPictureDecode**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_configpicturedecode) structure contains the DirectX VA connection configuration data for compressed picture decoding.

### <span id="Compressed_Picture_Parameters"></span><span id="compressed_picture_parameters"></span><span id="COMPRESSED_PICTURE_PARAMETERS"></span>Compressed Picture Parameters

The parameters that must be sent once for each picture to be decoded are specified in the [**DXVA\_PictureParameters**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_pictureparameters) structure.

 

