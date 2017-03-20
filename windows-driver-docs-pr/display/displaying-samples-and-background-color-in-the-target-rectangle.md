---
title: Displaying Samples and Background Color in the Target Rectangle
description: Displaying Samples and Background Color in the Target Rectangle
ms.assetid: 324fa569-4b2e-4ee1-9988-d08020df78e9
keywords: ["DeinterlaceBltEx, target rectangle", "target rectangle WDK DirectX VA", "background color options WDK DirectX VA", "deinterlacing WDK DirectX VA , target rectangle"]
---

# Displaying Samples and Background Color in the Target Rectangle


## <span id="ddk_displaying_samples_and_background_color_in_the_target_rectangle_gg"></span><span id="DDK_DISPLAYING_SAMPLES_AND_BACKGROUND_COLOR_IN_THE_TARGET_RECTANGLE_GG"></span>


This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.

The VMR on Windows Server 2003 SP1 and later and Windows XP SP2 and later can specify target rectangle and background color to determine how the video stream and substreams are displayed.

The VMR specifies a target rectangle to identify the location within the destination surface to which your driver should direct output. The coordinates of the source rectangles are always specified as absolute locations within the source surface; likewise, the coordinates of the destination rectangles and target rectangle are always specified as absolute locations within the destination surface. Typically, the source and destination rectangles for the video stream and substreams are the same size as the source and destination surfaces; however, this is not always the case. For more information, see [Processing Subrectangles](processing-subrectangles.md).

The following topics show how to display various samples with background color in the target rectangle:

[Displaying 16:9 Video within a 4:3 Destination Surface](displaying-16-9-video-within-a-4-3-destination-surface.md)

[Combining Video Stream and Substream with Different Aspect Ratios](combining-video-stream-and-substream-with-different-aspect-ratios.md)

[Combining Two Streams with Different Heights and Widths](combining-two-streams-with-different-heights-and-widths.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Displaying%20Samples%20and%20Background%20Color%20in%20the%20Target%20Rectangle%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




