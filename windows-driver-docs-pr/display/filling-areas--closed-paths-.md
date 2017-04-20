---
title: Filling Areas (Closed Paths)
description: Filling Areas (Closed Paths)
ms.assetid: 9dda1f0f-90e7-480b-aaeb-cb7781a1fe6c
keywords:
- GDI WDK Windows 2000 display , paths, closed
- graphics drivers WDK Windows 2000 display , paths, closed
- drawing WDK GDI , paths, closed
- filling paths WDK GDI , closed
- paths WDK GDI , closed
- closed paths WDK GDI
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Filling Areas (Closed Paths)


## <span id="ddk_filling_areas__28_closed_paths_29_gg"></span><span id="DDK_FILLING_AREAS__28_CLOSED_PATHS_29_GG"></span>


As in line drawing, pixels for filling are considered to be at integer coordinates. Each scan line in a region is bordered on the left and right by a segment of the path. Pixels that fall between the left and right borders are considered inside the fill region. Pixels that are exactly on the left border are also inside, but those exactly on the right border are excluded. If a top border is exactly horizontal, any pixels exactly on the border are inside while pixels exactly on the lower border are excluded.

The following figure shows how the pixels included in the fill region are determined relative to left and right borders of the region. Stated mathematically, the region is considered to be "closed" on the left and top, and "open" on the right and bottom.

![diagram illustrating determining the pixels included in a fill region](images/fillbdy.png)

The convention described above for the x-axis of the fill region also applies to the y-axis by substituting the left border with the top border and the right border with the bottom border.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Filling%20Areas%20%28Closed%20Paths%29%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




