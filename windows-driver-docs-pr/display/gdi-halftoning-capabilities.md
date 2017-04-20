---
title: GDI Halftoning Capabilities
description: GDI Halftoning Capabilities
ms.assetid: 57274fd5-fdf6-4041-b52c-4e409465d159
keywords:
- GDI WDK Windows 2000 display , rendering engine
- graphics drivers WDK Windows 2000 display , rendering engine
- drawing WDK GDI , rendering engine
- rendering engine WDK GDI
- GDI WDK Windows 2000 display , halftoning
- graphics drivers WDK Windows 2000 display , halftoning
- drawing WDK GDI , halftoning
- halftoning WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI Halftoning Capabilities


## <span id="ddk_gdi_halftoning_capabilities_gg"></span><span id="DDK_GDI_HALFTONING_CAPABILITIES_GG"></span>


GDI halftoning produces a quality dither or color-halftone image for printing devices or display devices that do not already have such capabilities built-in. Color halftoning provides:

-   Highest quality color and gray-scale reproduction possible on a given device.

-   Increased visual resolution with a limited set of intensity levels.

-   Improved color correlation between the different output devices.

Traditional analog halftoning is a cellular process that uses a halftoning screen. The halftoning screen is composed of cells of equal sizes, with fixed-cell spacing center-to-center. The fixed-cell spacing accommodates the thickness of the ink, while the size of a dot within each cell can vary to produce the impression of a continuous tone.

On a computer, most printing or screen shading also uses a fixed-cell pixel size. To simulate the variable dot size, a combination of cluster pixels simulates the halftone screen. In Windows NT-based operating systems, GDI includes halftoning default parameters that provide a good first approximation. Additional device-specific information can be added to the system to improve output.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Halftoning%20Capabilities%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




