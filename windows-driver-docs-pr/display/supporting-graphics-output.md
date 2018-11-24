---
title: Supporting Graphics Output
description: Supporting Graphics Output
ms.assetid: 2ac9b01d-9dca-44b4-9645-9c5eefb2ef1b
keywords:
- GDI WDK Windows 2000 display , graphics output
- graphics drivers WDK Windows 2000 display , output
- drawing WDK GDI , graphics output
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





