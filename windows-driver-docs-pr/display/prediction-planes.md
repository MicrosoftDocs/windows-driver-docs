---
title: Prediction Planes
description: Prediction Planes
ms.assetid: 967d52d1-c4e1-4a81-a1ad-40a09040c3a8
keywords:
- decoding video WDK DirectX VA , macroblock prediction
- video decoding WDK DirectX VA , macroblock prediction
- prediction planes WDK DirectX VA
- macroblocks WDK DirectX VA , prediction
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Prediction Planes


## <span id="ddk_prediction_planes_gg"></span><span id="DDK_PREDICTION_PLANES_GG"></span>


The following figure illustrates the conceptual macroblock prediction planes that exist prior to forming the final prediction.

![diagram illustrating plane example for field macroblock prediction](images/m2planes.png)

MPEG-2 has two planes: forward and backward (bidirectional prediction), or same-parity and opposite-parity (dual-prime). The forward reference plane consists of blocks from the closest previous I or P picture. The backward reference plane consists of blocks from the closest future I or P picture.

In the cases of MPEG-1 and MPEG-2, prediction planes are combined by averaging between the corresponding block pixel values of the two prediction planes and rounding each up to the nearest integer. More sophisticated prediction schemes, such as H.263's overlapped block motion compensated (OBMC) prediction, have three planes.

 

 





