---
title: Stretching Subrectangles
description: Stretching Subrectangles
ms.assetid: c8642ea4-67e9-4a15-9636-8d7efbfd8c9e
keywords:
- deinterlacing WDK DirectX VA , subrectangular processing
- subrectangular processing WDK DirectX VA
- stretching WDK Windows 2000 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Stretching Subrectangles


## <span id="ddk_stretching_subrectangles_gg"></span><span id="DDK_STRETCHING_SUBRECTANGLES_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

In the following example, the destination surface is 720 x 480, the coordinates of the target rectangle are {0,0,720,480}, and the background color is solid black.

The source surface of the video stream is 360 x 240, with the following source and destination subrectangles:

-   Source subrectangle (**rcSrc**): {180,120,360,240}

-   Destination subrectangle (**rcDest**): {0,0,360,240}

The source surface of the single substream is 360 x 240, with the following source and destination subrectangles:

-   Source subrectangle (**rcSrc**): {0,0,180,120}

-   Destination subrectangle (**rcDest**): {360,240,720,480}

The following diagram shows the output of the combination deinterlacing and substream compositing operation.

![diagram illustrating stretching subrectangles](images/trgrect7.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Stretching%20Subrectangles%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




