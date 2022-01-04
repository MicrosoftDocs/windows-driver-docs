---
title: Loading Highlight Data
description: Loading Highlight Data
keywords:
- alpha-blend data loading WDK DirectX VA
- blended pictures WDK DirectX VA , alpha-blend data loading
- highlighted rectangular area WDK DirectX VA
- rectangular highlighted area WDK DirectX VA
ms.date: 04/20/2017
---

# Loading Highlight Data


## <span id="ddk_loading_highlight_data_gg"></span><span id="DDK_LOADING_HIGHLIGHT_DATA_GG"></span>


The [**DXVA\_Highlight**](/windows-hardware/drivers/ddi/dxva/ns-dxva-_dxva_highlight) structure specifies a highlighted rectangular area of a subpicture, and is used along with DCCMD data and a DPXD surface to create an alpha-blending surface. The highlight data is formatted in a manner compatible with the DVD ROM specification. For further clarification of DVD subpicture definition and data field interpretation, see *DVD Specifications for Read-Only Disk: Part 3 - Video Specification (v. 1.11, May 1999)*.

 

