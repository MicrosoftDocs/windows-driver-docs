---
title: Mode Indicator and Anamorphic Format
description: Mode Indicator and Anamorphic Format
ms.assetid: b297c62e-3b7e-47de-95a5-c25e8fc5ad56
keywords:
- DirectX VPE support WDK DirectDraw , displaying interleaved video
- drawing VPEs WDK DirectDraw , displaying interleaved video
- DirectDraw VPEs WDK Windows 2000 display , displaying interleaved video
- video port extensions WDK DirectDraw , displaying interleaved video
- VPEs WDK DirectDraw , displaying interleaved video
- displaying interleaved video
- interleaved video displays WDK video port extensions
- anamorphic format WDK DirectDraw
- bob WDK DirectDraw
- weave WDK DirectDraw
- edge-adaptive filtering WDK DirectDraw
- mode indicators WDK DirectDraw
- irregular 3 2 pattern WDK DirectDraw
- REPEAT_FIELD
- automatic display changes WDK DirectDraw
- deinterlacing WDK video port extensions
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mode Indicator and Anamorphic Format


## <span id="ddk_mode_indicator_and_anamorphic_format_gg"></span><span id="DDK_MODE_INDICATOR_AND_ANAMORPHIC_FORMAT_GG"></span>


Good driver design calls for a combination of bob, weave, and edge-adaptive filtering. Motion-detection circuitry can dynamically control the degree to which each technique is used on a pixel-by-pixel basis. Unfortunately, display logic to accomplish this is difficult to implement unless some additional data is made available. With the increasing availability of large computer-grade displays, the operating system needs this additional data to assure that basic graphics circuitry can reliably deliver an optimal picture.

In the world of DVD, it can be expected that many formats will be combined on one disk. There might be 24-frames per second film edited to 525/60 video, and then edited to 30-frames per second film. Each time such an edit takes place, it potentially changes how the data is best displayed. The current DVD specification does not ensure good performance for handling this mix of formats in a display system.

Another possible scenario is the display of a film where the REPEAT\_FIELD flag is irregular or absent because of an error. When the encoder tries to interpret an irregular 3:2 pattern, it attempts to reacquire synchronization, but this can be messy. It is entirely possible for a display that follows the REPEAT\_FIELD flag to change from weave mode to bob mode, or vice versa, literally in the middle of a shot. This would look bad to the viewer.

A good way to display a film that has an occasional 3:2 pattern irregularity is to switch from weave mode to bob mode and back at the shot cuts that surround the irregularity. In other cases, it may be best to specifically identify the first field pair of a new pattern and maintain weave mode.

One can imagine many content scenarios. Some automatic display schemes work better than others depending on the particular content involved. It is likely that only some content providers will see a need to guarantee optimal results on the widest range of playback platforms. DirectShow gives these content authors a method for judging the impact of display mode on their titles and transmits their preferences.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Mode%20Indicator%20and%20Anamorphic%20Format%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




