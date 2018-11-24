---
title: Handling Nonstandard Display Modes
description: Handling Nonstandard Display Modes
ms.assetid: 4a3b0064-46d4-40bb-b49b-ac172012a7b7
keywords:
- nonstandard display modes WDK DirectX 9.0 , handling
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Nonstandard Display Modes


## <span id="ddk_handling_nonstandard_display_modes_gg"></span><span id="DDK_HANDLING_NONSTANDARD_DISPLAY_MODES_GG"></span>


A DirectX 9.0 driver for a device that supports a nonstandard display mode must also handle the following operations using that nonstandard mode:

-   Flip, blit, lock, and unlock operations that behave the same as with a standard display mode.

-   Calls to the driver's Graphics Device Interface (GDI) functions while the DirectX-primary surface is active.

    The driver should not receive any GDI DDI drawing calls while the DirectX primary is active. However, the driver should handle such drawing without causing the operating system to crash. The driver can provide an implementation for this situation, ignore it by immediately returning success, or fail it. Note that the data from GDI is based on a GDI primary surface format. Therefore, if the driver provides an implementation for this situation, it must convert from the GDI format before drawing to the DirectX-primary surface.

-   Calls to the GDI DDI *DrvDeriveSurface* function against the DirectX-primary surface cannot occur because GDI cannot access the nonstandard display format.

-   Typing "Ctl+Alt+Del" while the DirectX-primary surface is active.

    The kernel specifies the standard primary as the target in a call to the driver's [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) function before any GDI drawing occurs. Therefore, the driver must program the display device to the standard display mode before any GDI drawing. The driver's [*DdDestroySurface*](https://msdn.microsoft.com/library/windows/hardware/ff549281) function for the primary surface is also called. Note that the driver can discard contents of the DirectX-primary surface.

-   Windowed mode and nonstandard formats

    The [Reporting Support for 2D Operations Using Surface Formats](reporting-support-for-2d-operations-using-surface-formats.md) topic describes how the driver specifies that it can perform rendering to and present images from a format that differs from that of the current desktop. This scheme extends naturally to support nonstandard formats; the driver must merely add the enabling flags in the **dwOperations** member of the [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure for the formats.

Private formats and legacy code cannot be used to expose nonstandard desktop formats.

 

 





