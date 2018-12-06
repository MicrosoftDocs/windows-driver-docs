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

-   [*DxgkDdiCreateOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff559616)

-   [*DxgkDdiDestroyOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff559642)

-   [*DxgkDdiFlipOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff559655)

-   [*DxgkDdiUpdateOverlay*](https://msdn.microsoft.com/library/windows/hardware/ff560804)

 

 





