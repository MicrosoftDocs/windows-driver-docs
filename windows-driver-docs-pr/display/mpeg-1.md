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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MPEG-1


## <span id="ddk_mpeg_1_gg"></span><span id="DDK_MPEG_1_GG"></span>


The MPEG-1 video standard is titled ISO/IEC 11172-2. This standard was developed after H.261 and borrowed significantly from it. The MPEG-1 standard does not have a loop filter. Instead, it uses a simple half-sample filter that represents a finer accuracy of movement between frames than the full-sample accuracy supported by H.261.

Two additional prediction modes, bidirectional and backward prediction, were added. These prediction modes require one additional reference frame to be buffered. The bidirectional prediction mode averages forward-predicted and backward-predicted prediction blocks. The arithmetic for averaging forward and backward prediction blocks is similar to that for creating a half-sampled interpolated prediction block. The basic structure is otherwise the same as H.261.

 

 





