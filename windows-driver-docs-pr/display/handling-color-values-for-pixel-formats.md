---
title: Handling Color Values for Pixel Formats
description: Handling Color Values for Pixel Formats
ms.assetid: 53ce6be1-14e1-4ee8-ba29-f198dcdacdaa
keywords:
- color values for pixel formats WDK DirectX 9.0
- pixel format color values WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Color Values for Pixel Formats


## <span id="ddk_handling_color_values_for_pixel_formats_gg"></span><span id="DDK_HANDLING_COLOR_VALUES_FOR_PIXEL_FORMATS_GG"></span>


**This topic applies to DirectX 7.0 and later.**

A display driver must convert input color values for the ARGB and YUV classes of color formats because applications request color-fill and clear operations on surfaces with these formats in a uniform way. However, the driver must directly use the color values from other class formats. For example, applications use A8R8G8B8 as the uniform color value for all surfaces that have at most 8 bits for the alpha (A), red (R), green (G), and blue (B) components; the driver must convert the A8R8G8B8 color to the color value that is specific to the actual ARGB format by copying the bits with the highest significance.

The display driver receives color values when it processes the D3DDP2OP\_CLEAR and D3DDP2OP\_COLORFILL operation codes in its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) function.

The display driver can use the following code to convert color values for the ARGB and YUV class formats:

```cpp
DWORD Convert2N(DWORD Color, DWORD n)
{
    return (Color * (1 << n)) / 256;
}

DWORD CPixel::ConvertFromARGB(D3DCOLOR  InputColor,
                              D3DFORMAT OutputFormat)
{
    DWORD Output = (DWORD) InputColor;
    DWORD Alpha = InputColor >> 24;
    DWORD Red = (InputColor >> 16) & 0x00ff;
    DWORD Green = (InputColor >> 8) & 0x00ff;
    DWORD Blue = InputColor & 0x00ff;
    switch(OutputFormat) {
    case D3DFMT_R8G8B8:
    case D3DFMT_X8R8G8B8:
        Output = InputColor & 0x00ffffff;
        break;

    case D3DFMT_A8R8G8B8:
        Output = InputColor;
        break;

    case D3DFMT_R5G6B5:
        Output = (Convert2N(Red,5) << 11) | 
                    (Convert2N(Green,6) << 5) | 
                    (Convert2N(Blue,5));
        break;

    case D3DFMT_X1R5G5B5:
        Output = (Convert2N(Red,5) << 10) | 
                    (Convert2N(Green,5) << 5) | 
                    (Convert2N(Blue,5));
        break;

    case D3DFMT_A1R5G5B5:
        Output = (Convert2N(Alpha, 1) << 15) | 
                    (Convert2N(Red,5) << 10) | 
                    (Convert2N(Green,5) << 5) | 
                    (Convert2N(Blue,5));
        break;

    case D3DFMT_X4R4G4B4:
        Output = (Convert2N(Red,4) << 8) | 
                    (Convert2N(Green,4) << 4) | 
                    (Convert2N(Blue,4));
        break;

    case D3DFMT_A4R4G4B4:
        Output = (Convert2N(Alpha,4) << 12) |
                    (Convert2N(Red,4) << 8) | 
                    (Convert2N(Green,4) << 4) | 
                    (Convert2N(Blue,4));
        break;

    case D3DFMT_R3G3B2:
        Output = (Convert2N(Red,3) << 5) | 
                    (Convert2N(Green,3) << 2) | 
                    (Convert2N(Blue,2));
        break;

    case D3DFMT_A8R3G3B2:
        Output = (Alpha << 8) |
                    (Convert2N(Red,3) << 5) | 
                    (Convert2N(Green,3) << 2) | 
                    (Convert2N(Blue,2));
        break;

    case D3DFMT_A2B10G10R10:
        Output = (Convert2N(Alpha,2) << 30) |
                    (Convert2N(Red,10)) | 
                    (Convert2N(Green,10) << 10) | 
                    (Convert2N(Blue,10) << 20);
        break;

    case D3DFMT_X8B8G8R8:
        Output = (Convert2N(Red,8)) | 
                    (Convert2N(Green,8) << 8) | 
                    (Convert2N(Blue,8) << 16);
        break;

    case D3DFMT_A8B8G8R8:
        Output = (Alpha << 24) |
                    (Convert2N(Red,8)) | 
                    (Convert2N(Green,8) << 8) | 
                    (Convert2N(Blue,8) << 16);
        break;

#if (DXPIXELVER > 8)
    case D3DFMT_A2R10G10B10:
        Output = (Convert2N(Alpha,2) << 30) |
                    (Convert2N(Red,10) << 20) | 
                    (Convert2N(Green,10) << 10) | 
                    (Convert2N(Blue,10));
        break;
#endif

    case D3DFMT_UYVY:
#if (DXPIXELVER > 8)
    case D3DFMT_R8G8_B8G8:
#endif
        Output = (Red << 24) |
                    (Green << 16) |
                    (Red << 8) |
                    (Blue);
        break;
 
    case D3DFMT_YUY2:
#if (DXPIXELVER > 8)
    case D3DFMT_G8R8_G8B8:
#endif
        Output = (Green << 24) |
                    (Red << 16) |
                    (Blue << 8) |
                    (Red);
        break;

    case MAKEFOURCC(&#39;A&#39;, &#39;Y&#39;, &#39;U&#39;, &#39;V&#39;):
    case MAKEFOURCC(&#39;N&#39;, &#39;V&#39;, &#39;1&#39;, &#39;2&#39;):
    case MAKEFOURCC(&#39;Y&#39;, &#39;V&#39;, &#39;1&#39;, &#39;2&#39;):
    case MAKEFOURCC(&#39;I&#39;, &#39;C&#39;, &#39;M&#39;, &#39;1&#39;):
    case MAKEFOURCC(&#39;I&#39;, &#39;C&#39;, &#39;M&#39;, &#39;2&#39;):
    case MAKEFOURCC(&#39;I&#39;, &#39;C&#39;, &#39;M&#39;, &#39;3&#39;):
    case MAKEFOURCC(&#39;I&#39;, &#39;C&#39;, &#39;M&#39;, &#39;4&#39;):
        Output = InputColor;
        break;
    }
    return Output;
}
```

 

 





