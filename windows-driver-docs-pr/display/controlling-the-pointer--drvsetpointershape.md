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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Controlling the Pointer: DrvSetPointerShape


## <span id="ddk_controlling_the_pointer_drvsetpointershape_gg"></span><span id="DDK_CONTROLLING_THE_POINTER_DRVSETPOINTERSHAPE_GG"></span>


If a display driver controls the pointer, then the driver must support [**DrvSetPointerShape**](https://msdn.microsoft.com/library/windows/hardware/ff556289) to allow the pointer shape to be changed. A call to DrvSetPointerShape produces the following results:

1.  The function removes any existing pointer that the driver has drawn on the display.

2.  The function sets the new requested shape, unless it is unable to handle the shape.

3.  The new pointer is displayed at the position indicated by the parameters of the call.

The driver can call [**EngSetPointerShape**](https://msdn.microsoft.com/library/windows/hardware/ff565017) to have GDI manage a software cursor.

 

 





