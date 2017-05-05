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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Adaptive%20refresh%20for%20playing%2024%20fps%20video%20content%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




