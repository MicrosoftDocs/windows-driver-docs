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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filling Areas (Closed Paths)


## <span id="ddk_filling_areas__28_closed_paths_29_gg"></span><span id="DDK_FILLING_AREAS__28_CLOSED_PATHS_29_GG"></span>


As in line drawing, pixels for filling are considered to be at integer coordinates. Each scan line in a region is bordered on the left and right by a segment of the path. Pixels that fall between the left and right borders are considered inside the fill region. Pixels that are exactly on the left border are also inside, but those exactly on the right border are excluded. If a top border is exactly horizontal, any pixels exactly on the border are inside while pixels exactly on the lower border are excluded.

The following figure shows how the pixels included in the fill region are determined relative to left and right borders of the region. Stated mathematically, the region is considered to be "closed" on the left and top, and "open" on the right and bottom.

![diagram illustrating determining the pixels included in a fill region](images/fillbdy.png)

The convention described above for the x-axis of the fill region also applies to the y-axis by substituting the left border with the top border and the right border with the bottom border.

 

 





