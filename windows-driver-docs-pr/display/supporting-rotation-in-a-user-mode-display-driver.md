---
title: Supporting Rotation in a User-Mode Display Driver
description: Supporting Rotation in a User-Mode Display Driver
ms.assetid: fb80e875-26d4-4928-9268-2c6b36bb5d20
keywords: ["user-mode display drivers WDK Windows Vista , rotation", "rotation WDK display", "surface rotation WDK display"]
---

# Supporting Rotation in a User-Mode Display Driver


A user-mode display driver supports rotation differently, depending on many factors. For example, the user-mode display driver must behave differently for full-screen devices than it does for windowed devices. Also, the primary surfaces are created differently based on whether the desktop window manager (DWM) is running, the graphics adapter supports Microsoft DirectX 9L, or the DirectX 9L application is rotation-aware.

The following topics describe how a user-mode display driver supports rotation for different situations:

[Windowed-Mode Behavior](windowed-mode-behavior.md)

[Full-Screen-Mode Behavior](full-screen-mode-behavior.md)

[DirectX Runtime Behavior](directx-runtime-behavior.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Supporting%20Rotation%20in%20a%20User-Mode%20Display%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




