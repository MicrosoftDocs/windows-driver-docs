---
title: NTSC and Interlaced Data
description: NTSC and Interlaced Data
ms.assetid: 216b6219-aeb8-4e8a-8ac4-cd4d25a93e13
keywords:
- interlaced video WDK video port extensions
- DirectX VPE support WDK DirectDraw , interlaced video
- drawing VPEs WDK DirectDraw , interlaced video
- DirectDraw VPEs WDK Windows 2000 display , interlaced video
- video port extensions WDK DirectDraw , interlaced video
- VPEs WDK DirectDraw , interlaced video
- NTSC WDK video port extensions
- scan lines WDK video port extensions
- frames WDK video port extensions
- National Television Systems Committee WDK VPEs
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# NTSC and Interlaced Data


## <span id="ddk_ntsc_and_interlaced_data_gg"></span><span id="DDK_NTSC_AND_INTERLACED_DATA_GG"></span>


The National Television Systems Committee (NTSC) standard provides a series of 59.94 interlaced fields per second, each separated by 1/59.94 of a second. The scan lines of the even-numbered fields fall spatially halfway between the scan lines of the odd-numbered fields. However, because of the phosphor persistence of the television monitor, two fields are never displayed on a television screen at the same time. The viewer always sees either an even field or an odd field, but never both.

A *frame* in NTSC is an arbitrary grouping of two sequential fields that are completely unrelated. That is, the first field in a frame is no more related to the second field in the same frame than it is to the second field in the previous frame. The Phase Alternation Line (PAL) format and the Sequential Color with Memory (SECAM) standard work identically at about 50 fields per second.

If the video contains high-motion content, the data in the odd field could be different from that in the even field. This does not cause a problem on a television monitor because you are never looking at both fields at the same time and the eye does a good job integrating the data. On a computer, however, this interlaced data is often interleaved into a single buffer and then displayed using progressive scan. This means that both fields are visible at the same time, with a high potential for motion artifacts.

The process of putting video onto a digital video disc (DVD) and then replaying it is complex. Typically, the source material being put on the disk was created for television, so each frame has two fields that are interlaced. Film shot at 24 frames per second (fps), however, must be converted to 59.94 fields per second to be compatible with a television display.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20NTSC%20and%20Interlaced%20Data%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




