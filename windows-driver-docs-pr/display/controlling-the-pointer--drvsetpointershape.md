---
title: Controlling the Pointer DrvSetPointerShape
description: Controlling the Pointer DrvSetPointerShape
ms.assetid: 14d782de-5da8-40e9-a3e3-91d2588146e0
keywords:
- drawing pointers WDK Windows 2000 display
- display drivers WDK Windows 2000 , pointers
- pointers WDK Windows 2000 display
- DrvSetPointerShape
- shape of pointer WDK Windows 2000 display
- reshaping pointer WDK Windows 2000 display
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Controlling the Pointer: DrvSetPointerShape


## <span id="ddk_controlling_the_pointer_drvsetpointershape_gg"></span><span id="DDK_CONTROLLING_THE_POINTER_DRVSETPOINTERSHAPE_GG"></span>


If a display driver controls the pointer, then the driver must support [**DrvSetPointerShape**](https://msdn.microsoft.com/library/windows/hardware/ff556289) to allow the pointer shape to be changed. A call to DrvSetPointerShape produces the following results:

1.  The function removes any existing pointer that the driver has drawn on the display.

2.  The function sets the new requested shape, unless it is unable to handle the shape.

3.  The new pointer is displayed at the position indicated by the parameters of the call.

The driver can call [**EngSetPointerShape**](https://msdn.microsoft.com/library/windows/hardware/ff565017) to have GDI manage a software cursor.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Controlling%20the%20Pointer:%20DrvSetPointerShape%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




