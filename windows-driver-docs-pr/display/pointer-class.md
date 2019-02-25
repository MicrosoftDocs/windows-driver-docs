---
title: Pointer Class
description: Pointer Class
ms.assetid: c988535a-d218-48de-bdc2-56a620bbe4a2
keywords:
- pointer class WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Pointer Class


The Windows Display Driver Model (WDDM) does not permit a call into one of the pointer class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

-   [*DxgkDdiSetPointerPosition*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_setpointerposition)

-   [*DxgkDdiSetPointerShape*](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/d3dkmddi/nc-d3dkmddi-dxgkddi_setpointershape)

 

 





