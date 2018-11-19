---
title: Presentation with Multiple Heads
description: Presentation with Multiple Heads
ms.assetid: 60405ea7-91d5-4deb-9161-8890faa7e897
keywords:
- multiple-head hardware WDK DirectX 9.0 , presentation
- presentation WDK DirectX 9.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Presentation with Multiple Heads


## <span id="ddk_presentation_with_multiple_heads_gg"></span><span id="DDK_PRESENTATION_WITH_MULTIPLE_HEADS_GG"></span>


Applications can call the **Present** method either to present contents of back buffers for all heads at once or to present the back buffer for an individual head. For more information about **Present**, see the latest DirectX SDK documentation.

The runtime in turn makes independent sequential calls to the driver's [*DdFlip*](https://msdn.microsoft.com/library/windows/hardware/ff549306) or [*DdBlt*](https://msdn.microsoft.com/library/windows/hardware/ff549205) function. Because the display mode and refresh rate of each head might be different, these calls are always independent at the DDI level.

 

 





