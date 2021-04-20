---
title: Presentation with Multiple Heads
description: Presentation with Multiple Heads
keywords:
- multiple-head hardware WDK DirectX 9.0 , presentation
- presentation WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Presentation with Multiple Heads


## <span id="ddk_presentation_with_multiple_heads_gg"></span><span id="DDK_PRESENTATION_WITH_MULTIPLE_HEADS_GG"></span>


Applications can call the **Present** method either to present contents of back buffers for all heads at once or to present the back buffer for an individual head. For more information about **Present**, see the latest DirectX SDK documentation.

The runtime in turn makes independent sequential calls to the driver's [*DdFlip*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_flip) or [*DdBlt*](/windows/win32/api/ddrawint/nc-ddrawint-pdd_surfcb_blt) function. Because the display mode and refresh rate of each head might be different, these calls are always independent at the DDI level.

 

