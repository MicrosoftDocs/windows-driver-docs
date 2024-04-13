---
title: Clip Lists
description: Clip Lists
keywords:
- surfaces WDK DirectDraw , blitting
- drawing blt WDK DirectDraw , clip lists
- DirectDraw blitting WDK Windows 2000 display , clip lists
- blitting WDK DirectDraw , clip lists
- blt WDK DirectDraw , clip lists
- clip lists WDK DirectDraw
- clipped blts WDK DirectDraw
ms.date: 04/20/2017
---

# Clip Lists


## <span id="ddk_clip_lists_gg"></span><span id="DDK_CLIP_LISTS_GG"></span>


Clipped blts are never passed to the driver on Microsoft Windows 2000 and later. The **IsClipped** member of [**DD\_BLTDATA**](/windows/win32/api/ddrawint/ns-ddrawint-dd_bltdata) is always **FALSE**, and the clipped list is always **NULL**.

 

