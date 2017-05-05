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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Color Control Initialization


## <span id="ddk_color_control_initialization_gg"></span><span id="DDK_COLOR_CONTROL_INITIALIZATION_GG"></span>


A driver's [*DdControlColor*](https://msdn.microsoft.com/library/windows/hardware/ff549244) function controls the luminance/brightness controls of an overlay and/or primary surface. To enable color control functionality, the Microsoft DirectDraw HAL must do the following at initialization time:

-   If the overlay and/or primary surface contains color controls, set the DDCAPS2\_COLORCONTROLOVERLAY and/or DDCAPS2\_COLORCONTROLPRIMAY flags in the **dwCaps2** member of the [**DDCORECAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549248) structure that is embedded in the [**DD\_HALINFO**](https://msdn.microsoft.com/library/windows/hardware/ff551627) structure.

-   The driver must specify a function in the DD\_HALINFO structure that DirectDraw can call to get additional information. This is described in [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404).

-   The [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) callback must be called with the GUID\_ColorControlCallbacks GUID specified. The driver must fill in a [**DD\_COLORCONTROLCALLBACKS**](https://msdn.microsoft.com/library/windows/hardware/ff550521) structure with the appropriate driver callbacks and flags set, then copy this structure to the **lpvData** member of the input structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Color%20Control%20Initialization%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




