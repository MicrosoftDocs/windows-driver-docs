---
title: Color Control Initialization
description: Color Control Initialization
ms.assetid: dd3afcaa-3da0-4515-8b8d-e7429792be23
keywords:
- drawing WDK DirectDraw , color control initialization
- DirectDraw WDK Windows 2000 display , color control initialization
- color control initialization WDK DirectDraw
- initializing DirectDraw color control
- DdControlColor
- luminance WDK DirectDraw
- brightness WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Color Control Initialization


## <span id="ddk_color_control_initialization_gg"></span><span id="DDK_COLOR_CONTROL_INITIALIZATION_GG"></span>


A driver's [*DdControlColor*](https://msdn.microsoft.com/library/windows/hardware/ff549244) function controls the luminance/brightness controls of an overlay and/or primary surface. To enable color control functionality, the Microsoft DirectDraw HAL must do the following at initialization time:

-   If the overlay and/or primary surface contains color controls, set the DDCAPS2\_COLORCONTROLOVERLAY and/or DDCAPS2\_COLORCONTROLPRIMAY flags in the **dwCaps2** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure that is embedded in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure.

-   The driver must specify a function in the DD\_HALINFO structure that DirectDraw can call to get additional information. This is described in [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404).

-   The [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) callback must be called with the GUID\_ColorControlCallbacks GUID specified. The driver must fill in a [**DD\_COLORCONTROLCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff550521) structure with the appropriate driver callbacks and flags set, then copy this structure to the **lpvData** member of the input structure.

 

 





