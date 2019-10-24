---
title: GPU Scheduler Class
description: GPU Scheduler Class
ms.assetid: 39d38787-588d-483b-9b36-14a3bc16df7c
keywords:
- GPU scheduler class WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPU Scheduler Class


The Windows Display Driver Model (WDDM) does not permit a call into one of the GPU scheduler loader class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

-   [*DxgkDdiBuildPagingBuffer*](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_buildpagingbuffer)

-   [*DxgkDdiPatch*](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_patch)

-   [*DxgkDdiPreemptCommand*](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_preemptcommand)

-   [*DxgkDdiSubmitCommand*](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_submitcommand)

 

 





