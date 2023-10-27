---
title: Combine Video Stream, Substream with Different Aspect Ratios
description: This topic shows how the video stream, video substream, and background color are combined with different aspect ratios.
keywords:
- combining stream and substream WDK DirectX VA
- video stream and substream combined WDK DirectX VA
- substream and video stream combined WDK DirectX VA
- aspect ratios WDK DirectX VA
- streams combined WDK DirectX VA
ms.date: 12/06/2018
ms.custom: seodec18
---

# Combining Video Stream and Substream with Different Aspect Ratios

This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.

In the following example, the VMR calls the driver with a video stream destination rectangle that does not fully cover the destination surface. This example can occur when the VMR presents DVD content where the video stream is in the 4:3 aspect ratio and the subpicture stream is in the 16:9 aspect ratio.

The following diagram shows how, in this example, the video stream, video substream, and background color are combined.

:::image type="content" source="images/trgrect2.png" alt-text="Diagram illustrating the combination of a video stream, video substream, and background color with different aspect ratios.":::

In the preceding example, the rectangles are as follows:

- For the video stream, the source rectangle is {0, 0,720,480} and the destination rectangle is {107, 0, 747,480}.

- For the subpicture stream , the source rectangle is {0, 0,720,480} and the destination rectangle is {0, 0,854,480}.

- The Target Rectangle is also {0, 0,854,480}.

As shown in the preceding example, the left and right edges of the destination surface contain no pixels from the video stream. The driver's **DeinterlaceBltEx** function should interpret pixels that fall outside the video stream's destination rectangle as backgound color because they are combined with the pixels from the subpicture stream.
