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

-   [*DxgkDdiBuildPagingBuffer*](https://msdn.microsoft.com/library/windows/hardware/ff559587)

-   [*DxgkDdiPatch*](https://msdn.microsoft.com/library/windows/hardware/ff559737)

-   [*DxgkDdiPreemptCommand*](https://msdn.microsoft.com/library/windows/hardware/ff559741)

-   [*DxgkDdiSubmitCommand*](https://msdn.microsoft.com/library/windows/hardware/ff560790)

 

 





