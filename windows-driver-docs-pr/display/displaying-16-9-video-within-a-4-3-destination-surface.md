---
title: Displaying 16 9 Video within a 4 3 Destination Surface
description: Displaying 16 9 Video within a 4 3 Destination Surface
keywords:
- displaying 16 9 video
- 4 3 destination surface displays 16 9 video WDK DirectX VA
- 16 9 video on 4 3 destination surface WDK DirectX VA
ms.date: 04/20/2017
---

# Displaying 16:9 Video within a 4:3 Destination Surface

This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.

In the following example, the VMR directs to display a 16:9 video stream within a 4:3 destination surface.

:::image type="content" source="images/trgrect.png" alt-text="Diagram illustrating a 16:9 video within a 4:3 destination surface.":::

Note that for clarity the preceding example does not contain any video substreams. In the preceding example, the rectangles are as follows:

* Target rectangle = {0, 0, 640, 480}

* Video stream:
  * Source rectangle = {0, 0, 720, 480},
  * Destination rectangle = {0, 60,640,300}
