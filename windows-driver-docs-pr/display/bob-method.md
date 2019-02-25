---
title: Bob Method
description: Bob Method
ms.assetid: 3ef4ad25-fe62-4f80-8d0a-d21035d93c1f
keywords:
- DirectX VPE support WDK DirectDraw , displaying interleaved video
- drawing VPEs WDK DirectDraw , displaying interleaved video
- DirectDraw VPEs WDK Windows 2000 display , displaying interleaved video
- video port extensions WDK DirectDraw , displaying interleaved video
- VPEs WDK DirectDraw , displaying interleaved video
- displaying interleaved video
- interleaved video displays WDK video port extensions
- bob WDK DirectDraw
- deinterlacing WDK video port extensions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Bob Method


## <span id="ddk_bob_method_gg"></span><span id="DDK_BOB_METHOD_GG"></span>


The bob method of displaying data shows each field individually (similar to a television) using an overlay. The resulting image is half the normal height, so it must be zoomed 200 percent in the vertical direction using an interpolated overlay stretch. However, if this were all the bob algorithm did, the resulting image would jitter up and down because the odd field and the even field are offset by one line. Adding one line to the overlay start address on the odd fields solves this problem, as long as the vertical stretch is performed using an interpolator.

The bob method produces 60 (NTSC) progressive frames per second and retains all temporal information from an interlaced source. If a video was created with a video camera and the image contains motion, bob is the best low-cost display process for a progressive monitor. The bob method works for all sources of interlaced video data, but the weave method produces a crisper image.

By default, DirectShow uses the bob method for correcting interlaced display.

 

 





