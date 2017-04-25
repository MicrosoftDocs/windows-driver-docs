---
title: Displaying Interleaved Video with VPE
description: Displaying Interleaved Video with VPE
ms.assetid: f78ccefb-77e3-43a4-88ad-d98c69259da9
keywords:
- DirectX VPE support WDK DirectDraw , displaying interleaved video
- drawing VPEs WDK DirectDraw , displaying interleaved video
- DirectDraw VPEs WDK Windows 2000 display , displaying interleaved video
- video port extensions WDK DirectDraw , displaying interleaved video
- VPEs WDK DirectDraw , displaying interleaved video
- displaying interleaved video
- interleaved video displays WDK video port extensions
- interlaced video WDK video port extensions
- deinterlacing WDK video port extensions
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Displaying Interleaved Video with VPE


## <span id="ddk_displaying_interleaved_video_with_vpe_gg"></span><span id="DDK_DISPLAYING_INTERLEAVED_VIDEO_WITH_VPE_GG"></span>


Many methods exist for deinterlacing. Professional television producers use devices such as line doublers when deinterlacing for large-size rear-projection display, and effects systems with motion-adaptive filters when creating zooms and slow-motion sequences.

Two simple methods are available for displaying interlace on a progressive computer monitor: [bob](bob-method.md) and [weave](weave-method.md). These terms are used here for simplicity, because computer and television industry terms are different.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Displaying%20Interleaved%20Video%20with%20VPE%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




