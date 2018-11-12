---
title: Display Memory
description: Display Memory
ms.assetid: 92092bf2-dc31-4781-82c6-3365df77af99
keywords:
- display memory WDK DirectDraw , about display memory
- drawing memory WDK DirectDraw , about display memory
- DirectDraw memory WDK Windows 2000 display , about memory
- memory WDK DirectDraw , about memory
- drawing memory WDK DirectDraw
- DirectDraw memory WDK Windows 2000 display
- memory WDK DirectDraw
- display memory WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Display Memory


## <span id="ddk_display_memory_gg"></span><span id="DDK_DISPLAY_MEMORY_GG"></span>


In general, allocating as much display memory as possible to DirectDraw increases display performance and allows games and other DirectDraw applications to run faster, with a better quality visual image.

Usually, display cards have the pitch set to the width of the display so that no memory is wasted to the right (conceptually) of the front buffer. This leaves one scratch area at the conceptual bottom that can be used for other surfaces. Memory access is very straightforward in this case because one pointer can reference the entire area of accessible display memory.

If the pitch is greater than the width of the primary surface, memory to the conceptual right of the front buffer is wasted. This has to be reclaimed as a separate rectangular heap, regardless of whether the memory on the card is linear or rectangular. (Even if the memory is linear, some display drivers fix the pitch to speed up the blitter. Rather than rewrite the driver, the memory can simply be reclaimed as a separate heap.)

 

 





