---
title: Path Fill Modes
description: Path Fill Modes
ms.assetid: fa1fb4b9-5ed6-44a2-8a9e-0c1c82f5ea39
keywords:
- GDI WDK Windows 2000 display , paths, fill modes
- graphics drivers WDK Windows 2000 display , paths, fill modes
- drawing WDK GDI , paths, fill modes
- filling paths WDK GDI , fill modes
- paths WDK GDI , fill modes
- FP_ALTERNATEMODE
- FP_WINDINGMODE
- alternate fills WDK GDI
- winding fills WDK GDI
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Path Fill Modes


## <span id="ddk_path_fill_modes_gg"></span><span id="DDK_PATH_FILL_MODES_GG"></span>


The two fill modes defined for paths are *alternate* and *winding*. Both fill modes use an even-odd rule to determine how to fill a closed path.

FP\_ALTERNATEMODE applies the even-odd rule as follows: draw a line from any arbitrary start point in the closed path to some point obviously outside of the closed path. If the line crosses an odd number of path segments, the start point is inside the closed region and is therefore part of the fill area. An even number of crossings means that the point is not in an area to be filled.

FP\_WINDINGMODE considers not only the number of times that the vector crosses segments of the path, but also considers the direction of each segment. The path is considered to be drawn from start to finish, with each segment's direction implied by the order of its specified points: the first vertex of a segment is the "from" point, and the second vertex is the "to" point. Now draw the same arbitrary line described in alternate mode. Starting from zero, add one for every "forward" direction segment that the line crosses, and subtract one for every "reverse" direction segment crossed. (Forward and reverse are based on the dot product of the segment and the arbitrary line.) If the count result is nonzero, then the start point is inside the fill area; a zero count means the point is outside the fill area.

The following figure shows how to apply both rules to the more complex situation of a self-intersecting path.

![diagram illustrating alternate and winding fill modes](images/102-03.png)

In alternate fill mode, point A is inside because ray 1 passes through an odd number of line segments, while points B and C are outside, because rays 2 and 3 pass through an even number of segments. In winding-fill mode, points A and C are inside, because the sum of the forward (positive) and reverse (negative) line segments crossed by their rays, 1 and 3 respectively, is not zero, while point B is outside, because the sum of the forward and reverse line segments that ray 2 crosses is zero.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Path%20Fill%20Modes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




