---
title: Handling Stride in AVStream Codecs
description: Handling Stride in AVStream Codecs
ms.assetid: 816a0ddc-8ab8-4259-9842-76f5e4dadee0
keywords:
- AVStream hardware codec support WDK , handling stride
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Stride in AVStream Codecs


When a decoder is connected to a renderer like Enhanced Video Renderer (EVR) or a component that supports Direct3D, the minidriver receives D3D buffers instead of system memory buffers.

Unlike system memory buffers, which must be copied to a D3D surface before rendering, D3D buffers can be displayed directly by the render engine. Therefore, by using D3D buffers instead of system memory buffers, the minidriver saves a copy operation for each buffer.

When a SHED-capable minidriver receives D3D buffers, the D3D surface is locked and a pointer to it is located in [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138).**Data**. The surface stride information is supplied in the [**KS\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567645) extension to KSSTREAM\_HEADER, as shown in the following code example:

```cpp
typedef struct KS_FRAME_INFO {
    ULONG                   ExtendedHeaderSize; // Size of this extended header
    DWORD                   dwFrameFlags;       // Field1, Field2, or Frame
    LONGLONG                PictureNumber;
    LONGLONG                DropCount;

    // The following are only set when you use OverlayMixer
    HANDLE                  hDirectDraw;        // user mode DDraw handle
    HANDLE                  hSurfaceHandle;     // user mode surface handle
    RECT                    DirectDrawRect;     // portion of surface locked
    union {
  LONG               lSurfacePitch;  // Contains surface pitch a.k.a stride
         DWORD              Reserved1;
    };
    // Reserved fields, never reference these
    DWORD                   Reserved2;
    DWORD                   Reserved3;
    DWORD                   Reserved4;
} KS_FRAME_INFO, *PKS_FRAME_INFO;
```

Minidrivers should use the **biWidth** member of the [**KS\_BITMAPINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567305) structure as the surface width.

([**KS\_VIDEOINFOHEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567700).**bmiHeader** is of type KS\_BITMAPINFOHEADER. [**KS\_DATARANGE\_VIDEO**](https://msdn.microsoft.com/library/windows/hardware/ff567628).**VideoInfoHeader** is of type KS\_VIDEOINFOHEADER.)

If KS\_FRAME\_INFO.**lSurfacePitch** has a nonzero value, the minidriver must use **lSurfacePitch** as the width/stride for the buffer that is specified in the related KSSTREAM\_HEADER. Otherwise, the output image appears garbled.

 

 




