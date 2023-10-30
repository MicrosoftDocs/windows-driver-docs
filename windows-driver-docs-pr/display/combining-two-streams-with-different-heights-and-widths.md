---
title: Combining Two Streams with Different Heights and Widths
description: Combining Two Streams with Different Heights and Widths
keywords:
- combining streams WDK DirectX VA
- video streams combined WDK DirectX VA
- streams combined WDK DirectX VA
ms.date: 04/20/2017
---

# Combining Two Streams with Different Heights and Widths

This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.

In the following example, the VMR calls the driver with a video stream and a video substream of different heights as well as widths. The following diagram shows how, in this example, the driver combines the two streams and background color:

:::image type="content" source="images/trgrect3.png" alt-text="Diagram showing the combination of a background color and two video streams with different heights and widths.":::

Note that in the preceding example the driver's **DeinterlaceBltEx** function should only draw the specified background color over the target rectangle, as shown in the following diagram.

:::image type="content" source="images/trgrect4.png" alt-text="Diagram demonstrating the reduction of the output image size while maintaining the target rectangle.":::

In the preceding example, the VMR is directed to reduce the size of the output image horizontally and vertically by a factor of two. The background color should only be displayed in the target rectangle. The driver must not write to pixels in the destination surface that are outside of the target rectangle (hatched in the preceding diagram). In the preceding example, the destination surface is 300x200 pixels, but the target rectangle is {0, 0,150,100}. The source rectangle for the video stream is {0,0,300,150}; the destination rectangle for the video stream is {0,12,150,87}. The substream source rectangle is {0,0,150,200}; the substream destination rectangle is {37,0,112, 100}. Remember that the target rectangle is the bounding rectangle of the video stream and all substreams.
