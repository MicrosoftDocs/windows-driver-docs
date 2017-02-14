---
title: Performing Floating-point Operations in DirectDraw
description: Performing Floating-point Operations in DirectDraw
ms.assetid: 2ce638e8-2d32-4692-8093-adb413bfbe52
keywords: ["floating-point operations WDK DirectDraw", "drawing WDK DirectDraw , floating-point operations", "DirectDraw WDK Windows 2000 display , floating-point operations"]
---

# Performing Floating-point Operations in DirectDraw


## <span id="ddk_performing_floating_point_operations_in_directdraw_gg"></span><span id="DDK_PERFORMING_FLOATING_POINT_OPERATIONS_IN_DIRECTDRAW_GG"></span>


DirectDraw driver callback functions must perform all floating-point operations between calls to the GDI-supplied [**EngSaveFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565010) and [**EngRestoreFloatingPointState**](https://msdn.microsoft.com/library/windows/hardware/ff565006) functions. That is, the driver's callback functions must save the floating-point state prior to performing a floating-point operation and must restore the floating-point state when the floating-point operation completes. For more information about floating-point operations, see [Floating-Point Operations in Graphics Driver Functions](floating-point-operations-in-graphics-driver-functions.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Performing%20Floating-point%20Operations%20in%20DirectDraw%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




