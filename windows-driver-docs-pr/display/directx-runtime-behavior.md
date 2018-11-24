---
title: DirectX Runtime Behavior
description: DirectX Runtime Behavior
ms.assetid: 98cfb09c-74ed-4329-b663-5f813a84debe
keywords:
- DirectX runtime rotation WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DirectX Runtime Behavior


Various versions of the Microsoft DirectX runtime handle the following rotation situations on behalf of the driver:

-   The Microsoft DirectDraw runtime automatically fails any attempt to display an overlay while the display is rotated.

-   All versions of the DirectX runtime adjust the scan-line values that are returned while the primary surface is rotated so that the scan-line values cover the entire range up to the height of the resolution. Otherwise, an application that attempts beam chasing might stop responding if it waits for a scan-line value that is greater than the width of the display and that the application would otherwise never receive while in portrait mode.

-   All versions of the DirectX runtime handle all accesses to a rotated primary surface that are made by a windowed-mode device that uses various forms of emulation.

 

 





