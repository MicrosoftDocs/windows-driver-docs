---
title: Pointer Drawing
description: Pointer Drawing
keywords:
- drawing pointers WDK Windows 2000 display
- display drivers WDK Windows 2000 , pointers
- pointers WDK Windows 2000 display
- monochrome pointers WDK Windows 2000 display
- color pointers WDK Windows 2000 display
ms.date: 04/20/2017
---

# Pointer Drawing


## <span id="ddk_pointer_drawing_gg"></span><span id="DDK_POINTER_DRAWING_GG"></span>


GDI supports both color pointers and monochrome pointers. The shape of a monochrome pointer is defined by a single bitmap. The width of the bitmap is the same as the width of the pointer on the display, but the bitmap has twice the vertical extent as appears on the display, allowing it to contain two masks.

Calls to the pointer functions are serialized by GDI. This means two different threads in the driver cannot execute the pointer functions simultaneously. There are two possible pointer functions: [**DrvSetPointerShape**](/windows/win32/api/winddi/nf-winddi-drvsetpointershape) and [**DrvMovePointer**](/windows/win32/api/winddi/nf-winddi-drvmovepointer).

 

