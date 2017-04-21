---
title: MPEG-1
description: MPEG-1
ms.assetid: be4db8ea-98fa-4693-a2ff-888499e97f38
keywords:
- MPEG-1 WDK DirectX VA
- backward prediction WDK DirectX VA
- bidirectional prediction WDK DirectX VA
- prediction blocks WDK DirectX VA
- backward-predicted prediction blocks WDK DirectX VA
- forward-predicted prediction blocks WDK DirectX VA
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MPEG-1


## <span id="ddk_mpeg_1_gg"></span><span id="DDK_MPEG_1_GG"></span>


The MPEG-1 video standard is titled ISO/IEC 11172-2. This standard was developed after H.261 and borrowed significantly from it. The MPEG-1 standard does not have a loop filter. Instead, it uses a simple half-sample filter that represents a finer accuracy of movement between frames than the full-sample accuracy supported by H.261.

Two additional prediction modes, bidirectional and backward prediction, were added. These prediction modes require one additional reference frame to be buffered. The bidirectional prediction mode averages forward-predicted and backward-predicted prediction blocks. The arithmetic for averaging forward and backward prediction blocks is similar to that for creating a half-sampled interpolated prediction block. The basic structure is otherwise the same as H.261.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20MPEG-1%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




