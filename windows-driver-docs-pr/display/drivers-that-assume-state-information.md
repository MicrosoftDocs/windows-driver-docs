---
title: Drivers That Assume State Information
description: Drivers That Assume State Information
ms.assetid: c4dfb701-c547-4e94-8fd8-05571508137c
keywords:
- surfaces WDK DirectDraw , blitting
- drawing blt WDK DirectDraw , state information
- DirectDraw blitting WDK Windows 2000 display , state information
- blitting WDK DirectDraw , state information
- blt WDK DirectDraw , state information
- states WDK DirectDraw
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Drivers That Assume State Information


## <span id="ddk_drivers_that_assume_state_information_gg"></span><span id="DDK_DRIVERS_THAT_ASSUME_STATE_INFORMATION_GG"></span>


Most display drivers set up the state of the blitter when they do an operation. However, some display drivers expect the blitter to be in a known state. For example, some display drivers assume that the origin is set to do a standard blt rather than a transparent blt, and so on. In these cases, the state has to be reset after DirectDraw uses it.

Blts between two surfaces can be accomplished either with a fixed origin or with a separate origin for source and destination surfaces. If the display driver expects the origin to remain constant and DirectDraw changes it to access a secondary surface, the old pointer must be saved and restored when the operation is finished.

If this forces DirectDraw to wait while operations are being done so it can restore registers to their previous state, performance suffers. This is because DirectDraw's speed comes from being asynchronous.

Care must be taken in these cases to minimize the changes being made to the display state. Moving the origin in this scenario also wastes room on the stack that could otherwise be used for passing parameters.

 

 





