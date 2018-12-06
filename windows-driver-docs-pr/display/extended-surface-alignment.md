---
title: Extended Surface Alignment
description: Extended Surface Alignment
ms.assetid: 3a91a826-7f57-4cad-b236-b41178ac3b17
keywords:
- drawing extended surface alignment WDK DirectDraw
- DirectDraw extended surface alignment WDK Windows 2000 display
- surfaces WDK DirectDraw , extended alignment
- extended surface alignment WDK DirectDraw
- heaps WDK DirectDraw
- alignment WDK DirectDraw extended surface
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extended Surface Alignment


## <span id="ddk_extended_surface_alignment_gg"></span><span id="DDK_EXTENDED_SURFACE_ALIGNMENT_GG"></span>


Microsoft DirectDraw supports surface alignment requirements on a per-heap basis. This support was introduced in Microsoft DirectX 5.0. The driver can specify X and Y alignments for rectangular heaps, and pitch and start-offset alignments for linear heaps. These alignments can vary for different surface types.

Some display hardware cannot set its start-of-display offset in an atomic operation. At the beginning of a display period, it is possible for such hardware to latch a new start-of-display offset when the driver is only halfway through setting the value. DirectDraw now allows the driver to specify alignment requirements for visible back buffers. Some hardware may be able to express alignment requirements for potentially visible back buffers that force the start-of-display offset to be a value that requires only one register write. This technique can help avoid the occasional flicker that would otherwise be visible when the primary surface is flipped at a high frequency.

 

 





