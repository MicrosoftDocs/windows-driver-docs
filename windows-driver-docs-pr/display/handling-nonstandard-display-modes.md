---
title: Handling Nonstandard Display Modes
description: Handling Nonstandard Display Modes
ms.assetid: 4a3b0064-46d4-40bb-b49b-ac172012a7b7
keywords: ["nonstandard display modes WDK DirectX 9.0 , handling"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Handling%20Nonstandard%20Display%20Modes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




