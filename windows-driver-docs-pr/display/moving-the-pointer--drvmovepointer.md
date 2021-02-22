---
title: Moving the Pointer DrvMovePointer
description: Moving the Pointer DrvMovePointer
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

If [**DrvSetPointerShape**](/windows/win32/api/winddi/nf-winddi-drvsetpointershape) is included in the driver, then [**DrvMovePointer**](/windows/win32/api/winddi/nf-winddi-drvmovepointer) must also be supported. This function moves a driver-managed pointer to a new position. Because GDI serializes calls to pointer functions, *DrvMovePointer* is not be called while any thread is drawing in the display driver, unless the GCAPS_ASYNCMOVE flag has been set in the [**DEVINFO**](/windows/win32/api/winddi/ns-winddi-devinfo) structure.

The driver should call [**EngMovePointer**](/windows/win32/api/winddi/nf-winddi-engmovepointer) to have GDI move an engine-managed pointer on the device. The driver requests that GDI manage the cursor by calling [**EngSetPointerShape**](/windows/win32/api/winddi/nf-winddi-engsetpointershape).
