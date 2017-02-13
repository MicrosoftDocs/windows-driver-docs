---
title: Synchronization Issues for Display Drivers
description: Synchronization Issues for Display Drivers
ms.assetid: 7d87e963-02c3-4da2-9dbd-ca14bde2867b
keywords: ["display drivers WDK Windows 2000 , synchronization", "synchronization WDK Windows 2000 display"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Synchronization%20Issues%20for%20Display%20Drivers%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




