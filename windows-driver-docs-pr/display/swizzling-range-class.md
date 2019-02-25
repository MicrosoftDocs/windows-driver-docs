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

-   [*DxgkDdiAcquireSwizzlingRange*](https://msdn.microsoft.com/library/windows/hardware/ff559582)

-   [*DxgkDdiReleaseSwizzlingRange*](https://msdn.microsoft.com/library/windows/hardware/ff559786)

 

 





