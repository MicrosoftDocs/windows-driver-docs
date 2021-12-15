---
title: Handling Stride in AVStream Codecs
description: Handling Stride in AVStream Codecs
keywords:
- AVStream hardware codec support WDK , handling stride
ms.date: 04/20/2017
---

# Handling Stride in AVStream Codecs


When a decoder is connected to a renderer like Enhanced Video Renderer (EVR) or a component that supports Direct3D, the minidriver receives D3D buffers instead of system memory buffers.

Unlike system memory buffers, which must be copied to a D3D surface before rendering, D3D buffers can be displayed directly by the render engine. Therefore, by using D3D buffers instead of system memory buffers, the minidriver saves a copy operation for each buffer.

When a SHED-capable minidriver receives D3D buffers, the D3D surface is locked and a pointer to it is located in [**KSSTREAM\_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header).**Data**. The surface stride information is supplied in the [**KS\_FRAME\_INFO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_frame_info) extension to KSSTREAM\_HEADER, as shown in the following code example:

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

Minidrivers should use the **biWidth** member of the [**KS\_BITMAPINFOHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_bitmapinfoheader) structure as the surface width.

([**KS\_VIDEOINFOHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_videoinfoheader).**bmiHeader** is of type KS\_BITMAPINFOHEADER. [**KS\_DATARANGE\_VIDEO**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-tagks_datarange_video).**VideoInfoHeader** is of type KS\_VIDEOINFOHEADER.)

If KS\_FRAME\_INFO.**lSurfacePitch** has a nonzero value, the minidriver must use **lSurfacePitch** as the width/stride for the buffer that is specified in the related KSSTREAM\_HEADER. Otherwise, the output image appears garbled.

 

