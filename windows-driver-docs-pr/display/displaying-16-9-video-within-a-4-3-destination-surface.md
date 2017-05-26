---
title: Displaying 16 9 Video within a 4 3 Destination Surface
description: Displaying 16 9 Video within a 4 3 Destination Surface
ms.assetid: 8500ec9c-876d-4b94-a58a-2513942305db
keywords:
- displaying 16 9 video
- 4 3 destination surface displays 16 9 video WDK DirectX VA
- 16 9 video on 4 3 destination surface WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Displaying%2016:9%20Video%20within%20a%204:3%20Destination%20Surface%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




