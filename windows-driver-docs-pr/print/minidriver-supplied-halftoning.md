---
title: Minidriver-Supplied Halftoning
description: Minidriver-Supplied Halftoning
ms.assetid: 15af499a-c541-4d61-ace3-5a211574674c
keywords:
- minidriver-supplied halftoning WDK Unidrv
- customized halftoning WDK Unidrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Minidriver-Supplied Halftoning





If a specified color format is one for which the number of bits per pixel used for rendering the image (\*DrvBPP) is greater than the bits per pixel supported by the printer (\*DevBPP multiplied by \*DevNumOfPlanes), then you must provide customized halftoning capabilities.

To provide customized halftoning capabilities, you must do the following:

-   Provide a [rendering plug-in](rendering-plug-ins.md) that implements the [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261) method.

-   Include a Halftone\*Feature entry in your GPD file and, for each customized halftoning method, include an \*Option entry describing the halftoning method. (Do not use any of the [option attributes for the halftone feature](option-attributes-for-the-halftone-feature.md).)

-   Include a ColorMode \*Feature entry in your GPD file. For each specified color formatting option, you must include an \*IPCallbackID attribute if you want your **IPrintOemUni::ImageProcessing** method to handle halftoning for that color format.

The following example defines two color formats and four halftoning methods. The example uses [option constraints](option-constraints.md) to specify which halftoning methods Unidrv should allow a user to select for each color format.

```cpp
*Feature: ColorMode
{
    *Option: ColorFormat1
    {
        *Name: "Color Format 1"
        *DevBPP: 1
        *DevNumofPlanes: 4
        *ColorPlaneOrder: LIST (CYAN, MAGENTA, YELLOW, BLACK)
        *DrvBPP: 4
        *Constraints: LIST (Halftone.CustomHalftoneMethod1,
+                           Halftone.CustomHalftoneMethod2)
    }
    *Option: ColorFormat2
    {
        *Name: "Color Format 2"
        *DevBPP: 24
        *DevNumofPlanes: 1
        *DrvBPP: 8
        *IPCallbackID: 100
        *Constraints: LIST (Halftone.StandardHalftoneMethod1,
+                           Halftone.StandardHalftoneMethod2)
    }
}
*Feature: Halftone
{
    *Option: StandardHalftoneMethod1
    {
        *Name: "Standard Halftone Method 1"
    }
    *Option: StandardHalftoneMethod2
    {
        *Name: "Standard Halftone Method 2"
    }
    *Option: CustomHalftoneMethod1
    {
        *Name: "Custom Halftone Method 1"
    }
    *Option: CustomHalftoneMethod2
    {
        *Name: "Custom Halftone Method 2"
    }
}
```

In the example, both the ColorFormat1 and ColorFormat2 ColorMode options represent color formats that Unidrv can handle, as explained in [Handling Color Formats](handling-color-formats.md). For ColorFormat2, an \***IPCallbackID** attribute is specified. If the printer user selects ColorFormat2 as the color format, Unidrv calls the printer's [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261) COM method to handle halftoning. One of the method's parameters is a pointer to the string name representing the currently selected halftoning method.

For more information about halftoning, see [Customized Halftoning](customized-halftoning.md).

 

 




