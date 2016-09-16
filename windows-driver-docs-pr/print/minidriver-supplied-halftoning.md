---
title: Minidriver-Supplied Halftoning
author: windows-driver-content
description: Minidriver-Supplied Halftoning
MS-HAID:
- 'nt5gpd\_b1aa78a7-33e1-4cd1-b79e-94580b149c3f.xml'
- 'print.minidriver\_supplied\_halftoning'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 15af499a-c541-4d61-ace3-5a211574674c
keywords: ["minidriver-supplied halftoning WDK Unidrv", "customized halftoning WDK Unidrv"]
---

# Minidriver-Supplied Halftoning


## <a href="" id="ddk-minidriver-supplied-halftoning-gg"></a>


If a specified color format is one for which the number of bits per pixel used for rendering the image (\*DrvBPP) is greater than the bits per pixel supported by the printer (\*DevBPP multiplied by \*DevNumOfPlanes), then you must provide customized halftoning capabilities.

To provide customized halftoning capabilities, you must do the following:

-   Provide a [rendering plug-in](rendering-plug-ins.md) that implements the [**IPrintOemUni::ImageProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff554261) method.

-   Include a Halftone\*Feature entry in your GPD file and, for each customized halftoning method, include an \*Option entry describing the halftoning method. (Do not use any of the [option attributes for the halftone feature](option-attributes-for-the-halftone-feature.md).)

-   Include a ColorMode \*Feature entry in your GPD file. For each specified color formatting option, you must include an \*IPCallbackID attribute if you want your **IPrintOemUni::ImageProcessing** method to handle halftoning for that color format.

The following example defines two color formats and four halftoning methods. The example uses [option constraints](option-constraints.md) to specify which halftoning methods Unidrv should allow a user to select for each color format.

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Minidriver-Supplied%20Halftoning%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


