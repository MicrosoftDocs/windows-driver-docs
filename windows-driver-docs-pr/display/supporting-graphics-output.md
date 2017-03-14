---
title: Supporting Graphics Output
description: Supporting Graphics Output
ms.assetid: 2ac9b01d-9dca-44b4-9645-9c5eefb2ef1b
keywords: ["GDI WDK Windows 2000 display , graphics output", "graphics drivers WDK Windows 2000 display , output", "drawing WDK GDI , graphics output"]
---

# Supporting Graphics Output


## <span id="ddk_supporting_graphics_output_gg"></span><span id="DDK_SUPPORTING_GRAPHICS_OUTPUT_GG"></span>


The particular graphics operations that a driver handles depend upon the drawing surface and the capabilities of the hardware. If the surface is a standard-format [*DIB*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-independent-bitmap--dib-), GDI will handle all rendering operations not supported by the driver. The driver can hook out any of the [drawing functions](optional-display-driver-functions.md) and implement them to take advantage of hardware support.

For a device-managed surface, a driver must, at a minimum, support the graphics output functions [**DrvCopyBits**](https://msdn.microsoft.com/library/windows/hardware/ff556182), [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277), and [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316). It can optionally support any of the other graphics output functions. Supporting [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180), for example, can enhance performance. Some functions require a certain level of capability while others allow the device to indicate its capability by setting the appropriate GCAPS flags in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure.

All drawing calls to the driver are always single threaded, regardless of the surface type.

The topics that follow describe how a driver can implement the following operations:

[Drawing Lines and Curves](drawing-lines-and-curves.md)

[Drawing and Filling Paths](drawing-and-filling-paths.md)

[Copying Bitmaps](copying-bitmaps.md)

[Halftoning](halftoning.md)

[Image Color Management](image-color-management.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Graphics%20Output%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




