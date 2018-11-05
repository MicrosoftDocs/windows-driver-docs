---
title: Synchronization Issues for Display Drivers
description: Synchronization Issues for Display Drivers
ms.assetid: 7d87e963-02c3-4da2-9dbd-ca14bde2867b
keywords:
- display drivers WDK Windows 2000 , synchronization
- synchronization WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronization Issues for Display Drivers


Microsoft advises that the display driver not call any GDI functions while holding a lock. It is especially important that the display driver not call any of the following functions while holding a mutex. Doing so can lead to a deadlock.

-   BRUSHOBJ\_hGetColorTransform

-   BRUSHOBJ\_pvAllocRbrush

-   BRUSHOBJ\_pvGetRbrush

-   BRUSHOBJ\_ulGetBrushColor

-   CLIPOBJ\_bEnum

-   CLIPOBJ\_cEnumStart

-   CLIPOBJ\_ppoGetPath

-   EngAcquireSemaphore

-   EngAllocMem

-   EngAllocPrivateUserMem

-   EngAllocUserMem

-   EngAlphaBlend

-   EngAssociateSurface

-   EngBitBlt

-   EngCheckAbort

-   EngComputeGlyphSet

-   EngControlSprites

-   EngCopyBits

-   EngCreateBitmap

-   EngCreateClip

-   EngCreateDeviceBitmap

-   EngCreateDeviceSurface

-   EngCreateDriverObj

-   EngCreateEvent

-   EngCreatePalette

-   EngCreatePath

-   EngCreateSemaphore

-   EngCreateWnd

-   EngDeleteClip

-   EngDeleteDriverObj

-   EngDeleteEvent

-   EngDeletePalette

-   EngDeletePath

-   EngDeleteSafeSemaphore

-   EngDeleteSemaphore

-   EngDeleteSurface

-   EngDeleteWnd

-   EngDxIoctl

-   EngEraseSurface

-   EngFillPath

-   EngFntCacheAlloc

-   EngFntCacheFault

-   EngFntCacheLookUp

-   EngFreeMem

-   EngFreeModule

-   EngFreePrivateUserMem

-   EngFreeUserMem

-   EngGetType1FontList

-   EngGradientFill

-   EngHangNotification

-   EngInitializeSafeSemaphore

-   EngLineTo

-   EngLoadImage

-   EngLoadModule

-   EngLoadModuleForWrite

-   EngLockDirectDrawSurface

-   EngLockDriverObj

-   EngLockSurface

-   EngMapEvent

-   EngMapFile

-   EngMapFontFileFD

-   EngMarkBandingSurface

-   EngModifySurface

-   EngMovePointer

-   EngNineGrid

-   EngPaint

-   EngPlgBlt

-   EngQueryPalette

-   EngReleaseSemaphore

-   EngSetPointerShape

-   EngStretchBlt

-   EngStretchBltROP

-   EngStrokeAndFillPath

-   EngStrokePath

-   EngTextOut

-   EngTransparentBlt

-   EngUnloadImage

-   EngUnlockDirectDrawSurface

-   EngUnlockDriverObj

-   EngUnlockSurface

-   EngUnmapEvent

-   EngUnmapFile

-   EngUnmapFontFile

-   EngUnmapFontFileFD

-   EngWaitForSingleObject

-   FONTOBJ\_cGetAllGlyphHandles

-   FONTOBJ\_cGetGlyphs

-   FONTOBJ\_pifi

-   FONTOBJ\_pjOpenTypeTablePointer

-   FONTOBJ\_pQueryGlyphAttrs

-   FONTOBJ\_pvTrueTypeFontFile

-   FONTOBJ\_pxoGetXform

-   FONTOBJ\_vGetInfo

-   HeapVidMemAllocAligned

-   PALOBJ\_cGetColors

-   PATHOBJ\_bEnumClipLines

-   PATHOBJ\_bMoveTo

-   PATHOBJ\_bPolyBezierTo

-   PATHOBJ\_vEnumStartClipLines

-   PATHOBJ\_vGetBounds

-   STROBJ\_bEnum

-   VidMemFree

-   WNDOBJ\_bEnum

-   WNDOBJ\_cEnumStart

-   WNDOBJ\_vSetConsumer

-   XFORMOBJ\_bApplyXform

-   XFORMOBJ\_iGetFloatObjXform

-   XFORMOBJ\_iGetXform

-   XLATEOBJ\_cGetPalette

-   XLATEOBJ\_hGetColorTransform

-   XLATEOBJ\_iXlate

-   XLATEOBJ\_piVector

 

 





