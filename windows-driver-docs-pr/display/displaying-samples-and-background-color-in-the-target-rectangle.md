---
title: Displaying Samples and Background Color in the Target Rectangle
description: Displaying Samples and Background Color in the Target Rectangle
ms.assetid: 324fa569-4b2e-4ee1-9988-d08020df78e9
keywords:
- DeinterlaceBltEx, target rectangle
- target rectangle WDK DirectX VA
- background color options WDK DirectX VA
- deinterlacing WDK DirectX VA , target rectangle
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





