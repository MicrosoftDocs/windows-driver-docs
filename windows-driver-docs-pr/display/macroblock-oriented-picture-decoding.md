---
title: Macroblock-Oriented Picture Decoding
description: Macroblock-Oriented Picture Decoding
ms.assetid: 7a416992-04d3-4307-83b3-9fb94c17d60e
keywords:
- macroblocks WDK DirectX VA
- compressed picture decoding WDK DirectX VA , macroblock-oriented picture decoding
- picture decoding WDK DirectX VA , compressed
- macroblocks WDK DirectX VA , about macroblock-oriented picture decoding
- video decoding WDK DirectX VA , compressed pictures
- decoding video WDK DirectX VA , compressed pictures
- video decoding WDK DirectX VA , macroblock-oriented picture decoding
- decoding video WDK DirectX VA , macroblock-oriented picture decoding
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Macroblock-Oriented Picture Decoding


## <span id="ddk_macroblock_oriented_picture_decoding_gg"></span><span id="DDK_MACROBLOCK_ORIENTED_PICTURE_DECODING_GG"></span>


The macroblock is a fundamental unit of the video decoding process. A macroblock consists of a rectangular array of luminance (Y) samples and two corresponding arrays of chroma (Cb and Cr) samples. In the established video coding standards, the macroblocks are 16x16 blocks in luminance sample dimensions. If the video is coded in 4:2:0 format, the two chroma arrays each have half the height and half the width of the luma array for the macroblock. If the video is coded in 4:2:2 format, the two chrominance arrays, each have the same height and half the width of the luminance array for the macroblock. If the video is coded in the 4:4:4 format, the two chrominance arrays each have the same size as the luminance array for the macroblock.

A macroblock may be predicted using motion compensation with one or more motion vectors, or may be coded as intra without such prediction. After determining whether the macroblock is predicted or not, the remaining signal refinement, if any, is added in the form of residual difference data blocks. In the established video coding standards, these residual difference data blocks are 8x8, so that four residual difference data blocks are needed to cover a 16x16 luminance macroblock.

 

 





