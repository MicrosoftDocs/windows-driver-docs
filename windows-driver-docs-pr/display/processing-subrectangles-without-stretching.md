---
title: Processing Subrectangles without Stretching
description: Processing Subrectangles without Stretching
ms.assetid: ee59b06c-a3fb-41ac-875e-754d20a5eaa6
keywords:
- deinterlacing WDK DirectX VA , subrectangular processing
- subrectangular processing WDK DirectX VA
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Processing Subrectangles without Stretching


## <span id="ddk_processing_subrectangles_without_stretching_gg"></span><span id="DDK_PROCESSING_SUBRECTANGLES_WITHOUT_STRETCHING_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

In the following two examples, the destination surface is 720 x 576, the coordinates of the target rectangle are {0,0,720,576}, and the background color is solid black.

The first example shows a case in which the video stream and substream rectangles do not intersect.

In this example, the reference video stream and single substream are characterized by the following rectangular coordinates:

-   Video stream coordinates:
    -   Source surface: {0,0,720,480}
    -   Source subrectangle (**rcSrc**): {360,240,720,480}
    -   Destination subrectangle (**rcDest**): {0,0,360,240}
-   Substream coordinates:
    -   Source surface: {0,0,640,576}
    -   Source subrectangle (**rcSrc**): {0,288,320,576}
    -   Destination subrectangle (**rcDest**): {400,0,720,288}

In this example, the bottom-left corner of the video stream is displayed in the top-left corner of the destination surface, and the bottom-right corner of the substream is displayed in the top-right corner of the destination surface. The following diagram shows the output of the combination deinterlacing and substream compositing operation (the hashed regions indicate the subrectangles that are processed).

![diagram illustrating processing subrectangles without intersection](images/trgrect5.png)

The second example shows a case in which the video stream and substream rectangles intersect.

In the second example, the source surface coordinates are the same as in the first example. In this example, the reference video stream and single substream are characterized by the following subrectangular coordinates:

-   Video stream subrectangular coordinates:
    -   Source subrectangle (**rcSrc**): {260,92,720,480}
    -   Destination subrectangle (**rcDest**): {0,0,460,388}
-   Substream subrectangular coordinates:
    -   Source subrectangle (**rcSrc**): {0,0,460,388}
    -   Destination subrectangle (**rcDest**): {260,188,720,576}

In this example, the lower-right corner of the video stream is displayed in the top-left corner of the destination surface, shifted on the X and Y axis by +100. The top-left corner of the substream is displayed in the lower-right corner of the destination surface, shifted on the X and Y axis by -100. The following diagram shows the output of the combination deinterlacing and substream compositing operation.

![diagram illustrating processing subrectangles with intersection](images/trgrect6.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Processing%20Subrectangles%20without%20Stretching%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




