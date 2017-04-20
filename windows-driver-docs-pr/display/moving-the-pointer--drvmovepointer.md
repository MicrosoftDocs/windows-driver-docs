---
title: Moving the Pointer DrvMovePointer
description: Moving the Pointer DrvMovePointer
ms.assetid: cd82cea8-a37e-4e00-9342-9d6491e8c83c
keywords:
- drawing pointers WDK Windows 2000 display
- display drivers WDK Windows 2000 , pointers
- pointers WDK Windows 2000 display
- DrvMovePointer
- moving pointer position
- relocating pointers
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Moving the Pointer: DrvMovePointer


## <span id="ddk_moving_the_pointer_drvmovepointer_gg"></span><span id="DDK_MOVING_THE_POINTER_DRVMOVEPOINTER_GG"></span>


If [**DrvSetPointerShape**](https://msdn.microsoft.com/library/windows/hardware/ff556289) is included in the driver, then [**DrvMovePointer**](https://msdn.microsoft.com/library/windows/hardware/ff556248) must also be supported. This function moves a driver-managed pointer to a new position. Because GDI serializes calls to pointer functions, *DrvMovePointer* is not be called while any thread is drawing in the display driver, unless the GCAPS\_ASYNCMOVE flag has been set in the [**DEVINFO**](https://msdn.microsoft.com/library/windows/hardware/ff552835) structure.

The driver should call [**EngMovePointer**](https://msdn.microsoft.com/library/windows/hardware/ff564977) to have GDI move an engine-managed pointer on the device. The driver requests that GDI manage the cursor by calling [**EngSetPointerShape**](https://msdn.microsoft.com/library/windows/hardware/ff565017).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Moving%20the%20Pointer:%20DrvMovePointer%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




