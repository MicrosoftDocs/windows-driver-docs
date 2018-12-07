---
title: Off-Host IDCT
description: Off-Host IDCT
ms.assetid: 31797487-0c4e-4b8c-801e-f545bd60cc6d
keywords:
- macroblocks WDK DirectX VA , IDCT
- low-level IDCT WDK DirectX VA
- off-host IDCT WDK DirectX VA
- inverse discrete-cosine transform WDK DirectX VA
- IDCT WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Off-Host IDCT


## <span id="_off_host_idct"></span><span id="_OFF_HOST_IDCT"></span>


The transfer of macroblock inverse discrete-cosine transform (IDCT) coefficient data for off-host IDCT processing is done using a buffer of scan index and value information to define and specify the transform equations. Index information is sent as 16-bit words (although only 6-bit quantities are really needed for 8x8 transform blocks). Transform coefficient value information is sent as signed 16-bit words (although only 12 bits are needed for the usual case of 8x8 transform blocks and *BPP* equal to 8).

Transform coefficients are sent in either the [**DXVA\_TCoefSingle**](https://msdn.microsoft.com/library/windows/hardware/ff564060) structure or the [**DXVA\_TCoef4Group**](https://msdn.microsoft.com/library/windows/hardware/ff564053) structure. If the **bConfig4GroupedCoefs** member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure is zero, coefficients are sent individually using DXVA\_TCoefSingle structures. If **bConfig4GroupedCoefs** is 1, coefficients are sent in groups of four using DXVA\_TCoef4Group structures.

 

 





