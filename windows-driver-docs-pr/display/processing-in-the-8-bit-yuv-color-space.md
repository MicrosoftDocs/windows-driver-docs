---
title: Processing in the 8-bit YUV Color Space
description: Processing in the 8-bit YUV Color Space
ms.assetid: fbf62dc6-b5bf-43f6-baa8-c6d1cee80f9b
keywords:
- ProcAmp WDK DirectX VA , YUV color space
- YUV formats WDK DirectX VA
- Y processing WDK DirectX VA
- UV processing WDK DirectX VA
- color space conversions WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing in the 8-bit YUV Color Space


## <span id="ddk_processing_in_the_8_bit_yuv_color_space_gg"></span><span id="DDK_PROCESSING_IN_THE_8_BIT_YUV_COLOR_SPACE_GG"></span>


Working in the YUV color space simplifies the calculations involved for ProcAmp adjustment control of a video stream.

### <span id="Y_Processing"></span><span id="y_processing"></span><span id="Y_PROCESSING"></span>Y Processing

To perform ProcAmp adjustment for the Y component, subtract 16 from the Y value to position the black level at zero. This removes the DC offset so that adjusting the contrast does not vary the black level. Because Y values might be less than 16, negative Y values should be supported at this point. Contrast is adjusted by multiplying the YUV pixel values by a constant. If U and V are not adjusted, a color shift will result whenever the contrast is changed. The brightness property value is added (or subtracted) from the contrast adjusted Y values; this is done to avoid introducing a DC offset due to adjusting the contrast. Finally, the value 16 is added to reposition the black level at 16.

The following equation summarizes the steps described in the previous paragraph. C is the contrast value and B is the brightness value.

```cpp
Y&#39; = ((Y - 16) x C) + B + 16
```

### <span id="UV_Processing"></span><span id="uv_processing"></span><span id="UV_PROCESSING"></span>UV Processing

To perform ProcAmp adjustment for the U and V components, subtract 128 from both U and V values to position the range around zero. The hue property is implemented by mixing the U and V values together as shown in the following equations. H is the desired hue angle:

```cpp
U&#39; = (U-128) x Cos(H) + (V-128) x Sin(H)
V&#39; = (V-128) x Cos(H) - (U-128) x Sin(H)
```

Saturation is adjusted by multiplying U' and V' by a pair of constants, and then by adding 128 to each. The combined processing of hue and saturation on the UV data is shown in the following equations. H is the desired hue angle, C is the contrast value, and S is the saturation value:

```cpp
U&#39;&#39; = (((U-128) x Cos(H) + (V-128) x Sin(H)) x C x S) + 128
V&#39;&#39; = (((V-128) x Cos(H) - (U-128) x Sin(H)) x C x S) + 128
```

 

 





