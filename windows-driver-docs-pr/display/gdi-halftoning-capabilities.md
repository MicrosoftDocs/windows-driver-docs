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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Halftoning Capabilities


## <span id="ddk_gdi_halftoning_capabilities_gg"></span><span id="DDK_GDI_HALFTONING_CAPABILITIES_GG"></span>


GDI halftoning produces a quality dither or color-halftone image for printing devices or display devices that do not already have such capabilities built-in. Color halftoning provides:

-   Highest quality color and gray-scale reproduction possible on a given device.

-   Increased visual resolution with a limited set of intensity levels.

-   Improved color correlation between the different output devices.

Traditional analog halftoning is a cellular process that uses a halftoning screen. The halftoning screen is composed of cells of equal sizes, with fixed-cell spacing center-to-center. The fixed-cell spacing accommodates the thickness of the ink, while the size of a dot within each cell can vary to produce the impression of a continuous tone.

On a computer, most printing or screen shading also uses a fixed-cell pixel size. To simulate the variable dot size, a combination of cluster pixels simulates the halftone screen. In Windows NT-based operating systems, GDI includes halftoning default parameters that provide a good first approximation. Additional device-specific information can be added to the system to improve output.

 

 





