---
title: Handling Stride in AVStream Codecs
author: windows-driver-content
description: Handling Stride in AVStream Codecs
MS-HAID:
- 'shed\_dg\_fa9bacce-eb13-4fcb-aec4-d945d2ac8dc5.xml'
- 'stream.handling\_stride\_in\_avstream\_codecs'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 816a0ddc-8ab8-4259-9842-76f5e4dadee0
keywords: ["AVStream hardware codec support WDK , handling stride"]
---

# Handling Stride in AVStream Codecs


When a decoder is connected to a renderer like Enhanced Video Renderer (EVR) or a component that supports Direct3D, the minidriver receives D3D buffers instead of system memory buffers.

Unlike system memory buffers, which must be copied to a D3D surface before rendering, D3D buffers can be displayed directly by the render engine. Therefore, by using D3D buffers instead of system memory buffers, the minidriver saves a copy operation for each buffer.

When a SHED-capable minidriver receives D3D buffers, the D3D surface is locked and a pointer to it is located in [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138).**Data**. The surface stride information is supplied in the [**KS\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567645) extension to KSSTREAM\_HEADER, as shown in the following code example:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Handling%20Stride%20in%20AVStream%20Codecs%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


