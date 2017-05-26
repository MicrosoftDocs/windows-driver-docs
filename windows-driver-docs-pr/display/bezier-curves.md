---
title: Bezier Curves
description: Bezier Curves
ms.assetid: 322ff79b-e5b8-4247-99eb-1aa3779216ef
keywords:
- GDI WDK Windows 2000 display , curves, Bezier
- graphics drivers WDK Windows 2000 display , curves, Bezier
- drawing WDK GDI , curves, Bezier
- cubic splines WDK GDI
- Bezier curves WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bezier Curves


## <span id="ddk_bezier_curves_gg"></span><span id="DDK_BEZIER_CURVES_GG"></span>


Some advanced hardware devices can draw paths containing Bezier curves (cubic splines), which are general-purpose curve primitives. If so, the driver can include support for these curves in the [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316) function.

When GDI must draw a Bezier curve path on a device-managed surface, it will test the GCAPS\_BEZIERS flag (in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure) to determine if it should call [**DrvStrokePath**](https://msdn.microsoft.com/library/windows/hardware/ff556316). If called, this function either performs the requested operation or decides not to handle it, just as it does for geometric wide lines. In the latter case, GDI breaks the request down into simpler operations, for example, by converting curves to line approximations.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Bezier%20Curves%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




