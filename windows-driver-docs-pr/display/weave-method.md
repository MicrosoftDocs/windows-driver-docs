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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Weave Method


## <span id="ddk_weave_method_gg"></span><span id="DDK_WEAVE_METHOD_GG"></span>


The weave method displays data using the hardware video port to interleave the interlaced fields into an overlay surface and then shows both fields at the same time. If this were all the weave algorithm did, however, motion artifacts would appear. The weave algorithm also relies on the MPEG driver to recognize the 3:2 pattern and then undoes it using functions in the kernel-mode video transport. The kernel-mode video transport may cause the hardware video port to discard the repeat fields, causing all field pairs to come from the same frame. The result is full-framed video displayed at 24 frames per second, just as it was originally sampled using film.

Each source-film frame is represented in the NTSC signal by two or three fields. This can be looked at as two A fields that make up the A frame. Each sequence of four film frames is converted to five television frames. Film frames A, B, C, and D become five television frames with the field pattern AA, BB, BC, CD, and DD. When the REPEAT\_FIELD flag is used to encode this pattern in an MPEG stream, the MPEG data payload contains only four frames, but the field order of all five television frames is preserved.

The weave method produces 24 progressive frames per second and retains the full vertical resolution from an interlaced source. If a video was created from film using a 3:2 pulldown, or if it contains no motion, weave is the best affordable display process for a progressive monitor.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Weave%20Method%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




