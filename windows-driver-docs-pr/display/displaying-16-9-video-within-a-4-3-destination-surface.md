---
title: Displaying 16 9 Video within a 4 3 Destination Surface
description: Displaying 16 9 Video within a 4 3 Destination Surface
ms.assetid: 8500ec9c-876d-4b94-a58a-2513942305db
keywords:
- displaying 16 9 video
- 4 3 destination surface displays 16 9 video WDK DirectX VA
- 16 9 video on 4 3 destination surface WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Displaying 16:9 Video within a 4:3 Destination Surface


## <span id="ddk_displaying_16_9_video_within_a_4_3_destination_surface_gg"></span><span id="DDK_DISPLAYING_16_9_VIDEO_WITHIN_A_4_3_DESTINATION_SURFACE_GG"></span>


This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.

In the following example, the VMR directs to display a 16:9 video stream within a 4:3 destination surface.

![diagram illustrating 16:9 video within a 4:3 destination surface](images/trgrect.png)

Note that for clarity the preceding example does not contain any video substreams. In the preceding example, the rectangles are as follows:

-   Target rectangle = {0, 0, 640, 480}

-   Video stream:
    -   Source rectangle = {0, 0, 720, 480},
    -   Destination rectangle = {0, 60,640,300}

 

 





