---
title: Swizzling Range Class
description: Swizzling Range Class
ms.assetid: 2f5d5b91-ebd8-4242-8719-8a21bc3e9888
keywords:
- swizzling range class WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Swizzling Range Class


The Windows Display Driver Model (WDDM) does not permit a call into one of the swizzling range class functions in a reentrant fashion. That is, at the most, one thread can be running within one of the following functions at a given time:

-   [*DxgkDdiAcquireSwizzlingRange*](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_acquireswizzlingrange)

-   [*DxgkDdiReleaseSwizzlingRange*](https://docs.microsoft.com/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_releaseswizzlingrange)

 

 





