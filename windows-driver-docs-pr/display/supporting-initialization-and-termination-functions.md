---
title: Supporting Initialization and Termination Functions
description: Supporting Initialization and Termination Functions
ms.assetid: 306be966-be23-4680-aeda-32e9cb1ac4a9
keywords:
- drawing WDK GDI , initialization
- drawing WDK GDI , initialization, about
- initializing graphics drivers WDK Windows 2000 display
- initializing graphics drivers WDK Windows 2000 display , about
- GDI WDK Windows 2000 display , initialization
- GDI WDK Windows 2000 display , initialization, about
- graphics drivers WDK Windows 2000 display , initialization
- graphics drivers WDK Windows 2000 display , initialization, about
- GDI WDK Windows 2000 display , termination
- graphics drivers WDK Windows 2000 display , termination
- drawing WDK GDI , termination
- terminating graphics drivers WDK GDI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Supporting Initialization and Termination Functions


## <span id="ddk_supporting_initialization_and_termination_functions_gg"></span><span id="DDK_SUPPORTING_INITIALIZATION_AND_TERMINATION_FUNCTIONS_GG"></span>


A graphics driver can support multiple devices and multiple concurrent use of each device. Therefore, initialization and termination occur in three distinct layers, with each layer having its own timing. Initialization occurs in the following order:

1.  [Driver initialization](driver-initialization-and-cleanup.md)

2.  [PDEV initialization](pdev-initialization-and-cleanup.md)

3.  [Surface initialization](enabling-and-disabling-the-surface.md)

Termination occurs in the reverse order.

 

 





