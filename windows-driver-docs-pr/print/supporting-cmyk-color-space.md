---
title: Supporting CMYK Color Space
author: windows-driver-content
description: Supporting CMYK Color Space
ms.assetid: b8ac5f1a-c903-4313-b7de-0335f4c44367
keywords: ["CMYK color space WDK print", "BR_CMYKCOLOR", "XO_FROM_CMYK"]
---

# Supporting CMYK Color Space


## <a href="" id="ddk-supporting-cmyk-color-space-gg"></a>


Regardless of whether color management is being handled by the application, system, driver, or device, a [printer graphics DLL](printer-graphics-dll.md) must indicate whether it supports the [*CMYK*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-cmyk) color space. This is done by setting the GCAPS\_CMYKCOLOR flag in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure. If this flag is set and CMYK profiles are in use, then GDI sends CMYK color data, instead of RGB data, to the printer graphics DLL for bitmaps, brushes, and pens. GDI also sets the following flags:

-   The BR\_CMYKCOLOR flag in the **flColorType** member of the [**BRUSHOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff538261) structure.

-   The XO\_FROM\_CMYK flag in the **flXlate** member of the [**XLATEOBJ**](https://msdn.microsoft.com/library/windows/hardware/ff570634) structure.

Note that if the driver supports CMYK color space, it must also support halftoning. Thus if the driver sets the GCAPS\_CMYKCOLOR flag in DEVINFO, it must also set GCAPS\_HALFTONE.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Supporting%20CMYK%20Color%20Space%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


