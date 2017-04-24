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
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bob Method


## <span id="ddk_bob_method_gg"></span><span id="DDK_BOB_METHOD_GG"></span>


The bob method of displaying data shows each field individually (similar to a television) using an overlay. The resulting image is half the normal height, so it must be zoomed 200 percent in the vertical direction using an interpolated overlay stretch. However, if this were all the bob algorithm did, the resulting image would jitter up and down because the odd field and the even field are offset by one line. Adding one line to the overlay start address on the odd fields solves this problem, as long as the vertical stretch is performed using an interpolator.

The bob method produces 60 (NTSC) progressive frames per second and retains all temporal information from an interlaced source. If a video was created with a video camera and the image contains motion, bob is the best low-cost display process for a progressive monitor. The bob method works for all sources of interlaced video data, but the weave method produces a crisper image.

By default, DirectShow uses the bob method for correcting interlaced display.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Bob%20Method%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




