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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NTSC and Interlaced Data


## <span id="ddk_ntsc_and_interlaced_data_gg"></span><span id="DDK_NTSC_AND_INTERLACED_DATA_GG"></span>


The National Television Systems Committee (NTSC) standard provides a series of 59.94 interlaced fields per second, each separated by 1/59.94 of a second. The scan lines of the even-numbered fields fall spatially halfway between the scan lines of the odd-numbered fields. However, because of the phosphor persistence of the television monitor, two fields are never displayed on a television screen at the same time. The viewer always sees either an even field or an odd field, but never both.

A *frame* in NTSC is an arbitrary grouping of two sequential fields that are completely unrelated. That is, the first field in a frame is no more related to the second field in the same frame than it is to the second field in the previous frame. The Phase Alternation Line (PAL) format and the Sequential Color with Memory (SECAM) standard work identically at about 50 fields per second.

If the video contains high-motion content, the data in the odd field could be different from that in the even field. This does not cause a problem on a television monitor because you are never looking at both fields at the same time and the eye does a good job integrating the data. On a computer, however, this interlaced data is often interleaved into a single buffer and then displayed using progressive scan. This means that both fields are visible at the same time, with a high potential for motion artifacts.

The process of putting video onto a digital video disc (DVD) and then replaying it is complex. Typically, the source material being put on the disk was created for television, so each frame has two fields that are interlaced. Film shot at 24 frames per second (fps), however, must be converted to 59.94 fields per second to be compatible with a television display.

 

 





