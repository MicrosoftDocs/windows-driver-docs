---
title: Pointer Drawing
description: Pointer Drawing
ms.assetid: 5eaedf04-cbd9-4591-8cff-0087508aa7a9
keywords:
- drawing pointers WDK Windows 2000 display
- display drivers WDK Windows 2000 , pointers
- pointers WDK Windows 2000 display
- monochrome pointers WDK Windows 2000 display
- color pointers WDK Windows 2000 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Pointer Drawing


## <span id="ddk_pointer_drawing_gg"></span><span id="DDK_POINTER_DRAWING_GG"></span>


GDI supports both color pointers and monochrome pointers. The shape of a monochrome pointer is defined by a single bitmap. The width of the bitmap is the same as the width of the pointer on the display, but the bitmap has twice the vertical extent as appears on the display, allowing it to contain two masks.

Calls to the pointer functions are serialized by GDI. This means two different threads in the driver cannot execute the pointer functions simultaneously. There are two possible pointer functions: [**DrvSetPointerShape**](https://msdn.microsoft.com/library/windows/hardware/ff556289) and [**DrvMovePointer**](https://msdn.microsoft.com/library/windows/hardware/ff556248).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Pointer%20Drawing%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




