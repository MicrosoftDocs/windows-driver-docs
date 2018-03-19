---
title: Adaptive refresh for playing 24 fps video content
description: When Windows Display Driver Model (WDDM) 1.3 and later drivers play 24 frame per second (fps) video content on 60-Hz monitors, they must implement 48-Hz adaptive refresh to conserve power.
ms.assetid: CFA1AE0F-B591-4C5E-A97B-8D4E4B475167
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Adaptive refresh for playing 24 fps video content


When Windows Display Driver Model (WDDM) 1.3 and later drivers play 24 frame per second (fps) video content on 60-Hz monitors, they must implement 48-Hz adaptive refresh to conserve power. In this scenario the monitor switches from 60 Hz to a 48-Hz refresh rate to play back 24-fps video content.

These are the device driver interfaces (DDIs) that WDDM 1.3 and later drivers must implement for 24-fps playback:

## <span id="Adaptive_refresh_reference"></span><span id="adaptive_refresh_reference"></span><span id="ADAPTIVE_REFRESH_REFERENCE"></span>Adaptive refresh reference


These reference topics describe how to implement this capability in your drivers:

-   [*CheckPresentDurationSupport*](https://msdn.microsoft.com/library/windows/hardware/dn465880) (new)
-   [*pfnCheckPresentDurationSupport(DXGI)*](https://msdn.microsoft.com/library/windows/hardware/dn465886) (new)
-   [**D3DDDIARG\_CHECKPRESENTDURATIONSUPPORT**](https://msdn.microsoft.com/library/windows/hardware/dn465881) (new)
-   [**DXGI\_DDI\_ARG\_CHECKPRESENTDURATIONSUPPORT**](https://msdn.microsoft.com/library/windows/hardware/dn465884) (new)
-   [**DXGKARG\_SETVIDPNSOURCEADDRESS**](https://msdn.microsoft.com/library/windows/hardware/ff559484) (new **Duration** member)
-   [**DXGKARG\_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY**](https://msdn.microsoft.com/library/windows/hardware/hh780296) (new **Duration** member)
-   [**D3DDDI\_DEVICEFUNCS**](https://msdn.microsoft.com/library/windows/hardware/ff544519) (new **pfnCheckPresentDurationSupport** function pointer)
-   [**DXGI1\_3\_DDI\_BASE\_FUNCTIONS**](https://msdn.microsoft.com/library/windows/hardware/dn465883) (new **pfnCheckPresentDurationSupport** function pointer)

 

 





