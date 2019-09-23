---
title: Overlay Class
description: Overlay Class
ms.assetid: 698eb8af-ff9a-4c11-b764-6e5773886aaa
keywords:
- overlay class WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Overlay Class


The Windows Display Driver Model (WDDM) does not permit a call into one of the overlay class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

-   [*DxgkDdiCreateOverlay*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_createoverlay)

-   [*DxgkDdiDestroyOverlay*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_destroyoverlay)

-   [*DxgkDdiFlipOverlay*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_flipoverlay)

-   [*DxgkDdiUpdateOverlay*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_updateoverlay)

 

 





