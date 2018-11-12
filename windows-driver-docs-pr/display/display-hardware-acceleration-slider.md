---
title: Display Hardware Acceleration Slider
description: Display Hardware Acceleration Slider
ms.assetid: af3daa64-196a-4163-872d-713bc4cf0335
keywords:
- display drivers WDK Windows 2000 , debugging
- debugging drivers WDK Windows 2000 display
- hardware acceleration slider WDK Windows 2000 display
- acceleration slider WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Display Hardware Acceleration Slider


## <span id="ddk_display_hardware_acceleration_slider_gg"></span><span id="DDK_DISPLAY_HARDWARE_ACCELERATION_SLIDER_GG"></span>


The **Display Properties** dialog box has a hardware acceleration slider that can be helpful when you debug a display driver. By using the slider, you can set the display hardware acceleration support to one of six levels ranging from level 0 (full acceleration) to level 5 (no acceleration).

To find the hardware acceleration slider in Microsoft Windows XP, open the **Display Properties** dialog box and click the **Settings** tab. Click the **Advanced** button, and then click the **Troubleshoot** tab.

The following list describes the portion of hardware acceleration that is disabled at each level. Any feature that is disabled at a particular level is disabled in all subsequent levels.

<span id="Level_0"></span><span id="level_0"></span><span id="LEVEL_0"></span>**Level 0**  
The slider is in the far right position. Hardware acceleration is fully enabled.

<span id="Level_1"></span><span id="level_1"></span><span id="LEVEL_1"></span>**Level 1**  
Hardware cursor and device-bitmap support are disabled.

<span id="Level_2"></span><span id="level_2"></span><span id="LEVEL_2"></span>**Level 2**  
The following display driver functions are not called. Instead, GDI performs the operations in software.

-   [**DrvStretchBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556302)

-   [**DrvPlgBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556258)

-   [**DrvFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556220)

-   [**DrvStrokeAndFillPath**](https://msdn.microsoft.com/library/windows/hardware/ff556311)

-   [**DrvLineTo**](https://msdn.microsoft.com/library/windows/hardware/ff556245)

-   [**DrvStretchBltROP**](https://msdn.microsoft.com/library/windows/hardware/ff556306)

-   [**DrvTransparentBlt**](https://msdn.microsoft.com/library/windows/hardware/ff557283)

-   [**DrvAlphaBlend**](https://msdn.microsoft.com/library/windows/hardware/ff556176)

-   [**DrvGradientFill**](https://msdn.microsoft.com/library/windows/hardware/ff556236)

<span id="Level_3"></span><span id="level_3"></span><span id="LEVEL_3"></span>**Level 3**  
Microsoft DirectDraw and Direct3D support are disabled.

<span id="Level_4"></span><span id="level_4"></span><span id="LEVEL_4"></span>**Level 4**  
Only the following graphics operations are accelerated.

-   [**DrvTextOut**](https://msdn.microsoft.com/library/windows/hardware/ff557277)

-   [**DrvBitBlt**](https://msdn.microsoft.com/library/windows/hardware/ff556180)

-   [**DrvCopyBits**](https://msdn.microsoft.com/library/windows/hardware/ff556182)

-   [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316)

Also, the following display driver functions are not called.

-   [**DrvSaveScreenBits**](https://msdn.microsoft.com/library/windows/hardware/ff556278)

-   [**DrvEscape**](https://msdn.microsoft.com/library/windows/hardware/ff556217)

-   [**DrvDrawEscape**](https://msdn.microsoft.com/library/windows/hardware/ff556203)

-   [**DrvResetPDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556276)

-   [**DrvSetPixelFormat**](https://msdn.microsoft.com/library/windows/hardware/ff556285)

-   [**DrvDescribePixelFormat**](https://msdn.microsoft.com/library/windows/hardware/ff556190)

-   [**DrvSwapBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff556322)

<span id="Level_5"></span><span id="level_5"></span><span id="LEVEL_5"></span>**Level 5**  
The slider is in the far left position. The panning driver (part of kernel-mode GDI) handles all rendering. GDI calls the display driver's [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) and [**DrvEnableSurface**](https://msdn.microsoft.com/library/windows/hardware/ff556214) functions to create a primary surface and also calls the display driver to set the display mode. The display driver is not called to do any rendering.

Another way to limit display hardware acceleration is to set flags in the **CapabilityOverride** registry entry. For example, setting the 0x2 flag in the **CapabilityOverride** entry is equivalent to placing the hardware acceleration slider at level 3. For a description of the **CapabilityOverride** registry entry, see [Display INF File Sections](display-inf-file-sections.md).

 

 





