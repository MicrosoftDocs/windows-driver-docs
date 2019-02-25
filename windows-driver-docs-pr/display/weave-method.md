---
title: Weave Method
description: Weave Method
ms.assetid: d35a08b6-7221-4e1c-895f-446f23096519
keywords:
- DirectX VPE support WDK DirectDraw , displaying interleaved video
- drawing VPEs WDK DirectDraw , displaying interleaved video
- DirectDraw VPEs WDK Windows 2000 display , displaying interleaved video
- video port extensions WDK DirectDraw , displaying interleaved video
- VPEs WDK DirectDraw , displaying interleaved video
- displaying interleaved video
- interleaved video displays WDK video port extensions
- weave WDK DirectDraw
- deinterlacing WDK video port extensions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Weave Method


## <span id="ddk_weave_method_gg"></span><span id="DDK_WEAVE_METHOD_GG"></span>


The weave method displays data using the hardware video port to interleave the interlaced fields into an overlay surface and then shows both fields at the same time. If this were all the weave algorithm did, however, motion artifacts would appear. The weave algorithm also relies on the MPEG driver to recognize the 3:2 pattern and then undoes it using functions in the kernel-mode video transport. The kernel-mode video transport may cause the hardware video port to discard the repeat fields, causing all field pairs to come from the same frame. The result is full-framed video displayed at 24 frames per second, just as it was originally sampled using film.

Each source-film frame is represented in the NTSC signal by two or three fields. This can be looked at as two A fields that make up the A frame. Each sequence of four film frames is converted to five television frames. Film frames A, B, C, and D become five television frames with the field pattern AA, BB, BC, CD, and DD. When the REPEAT\_FIELD flag is used to encode this pattern in an MPEG stream, the MPEG data payload contains only four frames, but the field order of all five television frames is preserved.

The weave method produces 24 progressive frames per second and retains the full vertical resolution from an interlaced source. If a video was created from film using a 3:2 pulldown, or if it contains no motion, weave is the best affordable display process for a progressive monitor.

 

 





