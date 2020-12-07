---
title: Color Control Initialization
description: Color Control Initialization
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


A driver's [*DdControlColor*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_colorcb_colorcontrol) function controls the luminance/brightness controls of an overlay and/or primary surface. To enable color control functionality, the Microsoft DirectDraw HAL must do the following at initialization time:

-   If the overlay and/or primary surface contains color controls, set the DDCAPS2\_COLORCONTROLOVERLAY and/or DDCAPS2\_COLORCONTROLPRIMAY flags in the **dwCaps2** member of the [**DDCORECAPS**](/windows/win32/api/ddrawi/ns-ddrawi-ddcorecaps) structure that is embedded in the [**DD\_HALINFO**](/windows/win32/api/ddrawint/ns-ddrawint-dd_halinfo) structure.

-   The driver must specify a function in the DD\_HALINFO structure that DirectDraw can call to get additional information. This is described in [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo).

-   The [**DdGetDriverInfo**](/windows/win32/api/ddrawint/nc-ddrawint-pdd_getdriverinfo) callback must be called with the GUID\_ColorControlCallbacks GUID specified. The driver must fill in a [**DD\_COLORCONTROLCALLBACKS**](/windows/win32/api/ddrawint/ns-ddrawint-dd_colorcontrolcallbacks) structure with the appropriate driver callbacks and flags set, then copy this structure to the **lpvData** member of the input structure.

 

