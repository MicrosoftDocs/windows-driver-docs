---
title: Supporting Graphics Output
description: Supporting Graphics Output
keywords:
- GDI WDK Windows 2000 display , graphics output
- graphics drivers WDK Windows 2000 display , output
- drawing WDK GDI , graphics output
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Graphics Output

The particular graphics operations that a driver handles depend upon the drawing surface and the capabilities of the hardware. If the surface is a standard-format *DIB*, GDI will handle all rendering operations not supported by the driver. The driver can hook out any of the [drawing functions](optional-display-driver-functions.md) and implement them to take advantage of hardware support.

For a device-managed surface, a driver must, at a minimum, support the graphics output functions [**DrvCopyBits**](/windows/win32/api/winddi/nf-winddi-drvcopybits), [**DrvTextOut**](/windows/win32/api/winddi/nf-winddi-drvtextout), and [**DrvStrokePath**](/windows/win32/api/winddi/nf-winddi-drvstrokepath). It can optionally support any of the other graphics output functions. Supporting [**DrvBitBlt**](/windows/win32/api/winddi/nf-winddi-drvbitblt), for example, can enhance performance. Some functions require a certain level of capability while others allow the device to indicate its capability by setting the appropriate GCAPS flags in the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure.

All drawing calls to the driver are always single threaded, regardless of the surface type.

The topics that follow describe how a driver can implement the following operations:

[Drawing Lines and Curves](drawing-lines-and-curves.md)

[Drawing and Filling Paths](drawing-and-filling-paths.md)

[Copying Bitmaps](copying-bitmaps.md)

[Halftoning](halftoning.md)

[Image Color Management](image-color-management.md)
