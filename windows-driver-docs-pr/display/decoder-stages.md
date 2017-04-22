---
title: Decoder Stages
description: Decoder Stages
ms.assetid: 34562b2a-9568-440d-b6ec-dbd1e5004d56
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , video decoding
- Video Acceleration WDK DirectX , video decoding
- VA WDK DirectX , video decoding
- decoding video WDK DirectX VA , decoder stages
- video decoding WDK DirectX VA , decoder stages
- decoder stages WDK DirectX VA
- inverse discrete-cosine transform WDK DirectX VA
- IDCT WDK DirectX VA
- MCP WDK DirectX VA
- motion compensation WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Decoder Stages


## <span id="ddk_decoder_stages_gg"></span><span id="DDK_DECODER_STAGES_GG"></span>


The decoder stages that are depicted in the following figure show the operation of the motion compensation prediction (MCP) and inverse discrete-cosine transform (IDCT) parts of an accelerator. The data indicated as dct\_type is a syntax element that controls the type of IDCT that is performed.

![diagram illustrating decoder stages](images/decstages.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Decoder%20Stages%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




