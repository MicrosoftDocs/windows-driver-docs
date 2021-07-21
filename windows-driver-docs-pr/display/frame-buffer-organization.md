---
title: Frame Buffer Organization
description: Frame Buffer Organization
keywords:
- DirectX Video Acceleration WDK Windows 2000 display , video decoding
- Video Acceleration WDK DirectX , video decoding
- VA WDK DirectX , video decoding
- decoding video WDK DirectX VA , frame buffer organization
- video decoding WDK DirectX VA , frame buffer organization
- frame buffer organization WDK DirectX VA
- buffers WDK DirectX VA
- prediction blocks WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Frame Buffer Organization


## <span id="ddk_frame_buffer_organization_gg"></span><span id="DDK_FRAME_BUFFER_ORGANIZATION_GG"></span>


All picture buffers are assumed to have frame-organized buffers as described in the MPEG-2 video specification (sample locations are given as frame coordinates).

It is possible to use an implementation-specific translation layer to convert prediction blocks without loss (see *lossy compression*) that are described in frame coordinates to field coordinates. For example, a single frame motion prediction can be broken into two separate, top and bottom macroblock-portion predictions.

Three video component channels (Y, Cb, Cr) are decoded using interfaces defined for DirectX VA. Motion vectors for the two chrominance components (Cb, Cr) are derived from those sent for the luminance component (Y). The accelerator is responsible for converting any of these motion vectors to different coordinate systems that may be used.

The following figure shows how video data buffering is implemented in the host and accelerator.

![diagram illustrating video data buffering in host and accelerator systems.](images/hostaccsys.png)

 

 





