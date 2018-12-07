---
title: Clip Lists
description: Clip Lists
ms.assetid: 73383093-ab83-4955-b017-cc370009fd0e
keywords:
- surfaces WDK DirectDraw , blitting
- drawing blt WDK DirectDraw , clip lists
- DirectDraw blitting WDK Windows 2000 display , clip lists
- blitting WDK DirectDraw , clip lists
- blt WDK DirectDraw , clip lists
- clip lists WDK DirectDraw
- clipped blts WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Clip Lists


## <span id="ddk_clip_lists_gg"></span><span id="DDK_CLIP_LISTS_GG"></span>


Clipped blts are never passed to the driver on Microsoft Windows 2000 and later. The **IsClipped** member of [**DD\_BLTDATA**](https://msdn.microsoft.com/library/windows/hardware/ff550474) is always **FALSE**, and the clipped list is always **NULL**.

 

 





