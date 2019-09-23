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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Moving the Pointer: DrvMovePointer


## <span id="ddk_moving_the_pointer_drvmovepointer_gg"></span><span id="DDK_MOVING_THE_POINTER_DRVMOVEPOINTER_GG"></span>


If [**DrvSetPointerShape**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-drvsetpointershape) is included in the driver, then [**DrvMovePointer**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-drvmovepointer) must also be supported. This function moves a driver-managed pointer to a new position. Because GDI serializes calls to pointer functions, *DrvMovePointer* is not be called while any thread is drawing in the display driver, unless the GCAPS\_ASYNCMOVE flag has been set in the [**DEVINFO**](https://docs.microsoft.com/windows/desktop/api/winddi/ns-winddi-tagdevinfo) structure.

The driver should call [**EngMovePointer**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-engmovepointer) to have GDI move an engine-managed pointer on the device. The driver requests that GDI manage the cursor by calling [**EngSetPointerShape**](https://docs.microsoft.com/windows/desktop/api/winddi/nf-winddi-engsetpointershape).

 

 





