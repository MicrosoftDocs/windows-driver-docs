---
title: Triple Buffering
description: Triple Buffering
ms.assetid: 4651f9d2-09fb-4006-8243-403f564414f5
keywords:
- drawing page flips WDK DirectDraw , triple buffering
- DirectDraw flipping WDK Windows 2000 display , triple buffering
- page flipping WDK DirectDraw , triple buffering
- flipping WDK DirectDraw , triple buffering
- triple buffering WDK DirectDraw
- buffers WDK DirectDraw
- surfaces WDK DirectDraw , flipping
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Triple Buffering


## <span id="ddk_triple_buffering_gg"></span><span id="DDK_TRIPLE_BUFFERING_GG"></span>


Increasing the number of buffers that can hold a primary surface increases display performance. It is preferable to have at least three flippable surfaces (some games use five or more). When there are only two surfaces and a page flip occurs, the display delays until the monitor's vertical retrace is finished. The delay is necessary to ensure that the back buffer is not written on before it is finished being displayed. With triple buffering, the third surface is always writable because it is a back buffer and available to draw on immediately (as shown in the following figure). In a game that does not use sprite memory, 3D rendering using triple buffering is 20 to 30 percent faster than double buffering.

![diagram illustrating triple buffering](images/ddfig9.png)

The flipping structures in the preceding figure are the same as those in [Tearing](tearing.md), only now three buffers are used. One buffer is almost always writable (because it is not involved in a flip) so the driver does not have to wait for the display scan to finish before allowing the back buffer to be written to again.

The following is a brief explanation of flipping and blitting in a triple-buffered system, using the labels from the preceding figure. The example begins with surface pixel memory 11 being displayed. This is the primary surface pointed to by the front buffer (**fpVidMem** in the sample code supplied with the Microsoft Windows Driver Development Kit \[DDK\]). At some point, it becomes desirable to blt to the surface at pixel memory 22. Because **fpVidMem** points to the surface beginning at 11 (not 22) and the flip status is false (no flip is occurring on the requested surface), the blt can proceed. The driver locks the surface, writes to it, and then unlocks it. To display that surface, a flip must occur.

The DirectDraw front buffer object can now change **fpVidMem** (the display memory pointer) to make the surface at 22 the primary surface. Because no flip is pending, the display pointers are exchanged (see the bottom half of the preceding figure), and the flip status is set to **TRUE**. The front buffer now points to surface pixel memory 22, the back buffer points to surface pixel memory 33, and the third buffer object points to surface pixel memory 11 (the old primary surface). Unlike with double buffering, DirectDraw is free to write to the back buffer at this time. In other words, DirectDraw can write to surface pixel memory 33 because no flip is pending. This circular flipping process continues endlessly to provide smooth animation and faster game play and video playback for applications that use DirectDraw.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Triple%20Buffering%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




