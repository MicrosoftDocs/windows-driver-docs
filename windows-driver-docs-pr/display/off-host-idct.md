---
title: Off-Host IDCT
description: Off-Host IDCT
ms.assetid: 31797487-0c4e-4b8c-801e-f545bd60cc6d
keywords: ["macroblocks WDK DirectX VA , IDCT", "low-level IDCT WDK DirectX VA", "off-host IDCT WDK DirectX VA", "inverse discrete-cosine transform WDK DirectX VA", "IDCT WDK DirectX VA"]
---

# Off-Host IDCT


## <span id="_off_host_idct"></span><span id="_OFF_HOST_IDCT"></span>


The transfer of macroblock inverse discrete-cosine transform (IDCT) coefficient data for off-host IDCT processing is done using a buffer of scan index and value information to define and specify the transform equations. Index information is sent as 16-bit words (although only 6-bit quantities are really needed for 8x8 transform blocks). Transform coefficient value information is sent as signed 16-bit words (although only 12 bits are needed for the usual case of 8x8 transform blocks and *BPP* equal to 8).

Transform coefficients are sent in either the [**DXVA\_TCoefSingle**](https://msdn.microsoft.com/library/windows/hardware/ff564060) structure or the [**DXVA\_TCoef4Group**](https://msdn.microsoft.com/library/windows/hardware/ff564053) structure. If the **bConfig4GroupedCoefs** member of the [**DXVA\_ConfigPictureDecode**](https://msdn.microsoft.com/library/windows/hardware/ff563133) structure is zero, coefficients are sent individually using DXVA\_TCoefSingle structures. If **bConfig4GroupedCoefs** is 1, coefficients are sent in groups of four using DXVA\_TCoef4Group structures.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Off-Host%20IDCT%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




